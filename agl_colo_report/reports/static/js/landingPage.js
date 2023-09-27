// landingpage.js

// Import other scripts
import { getCookie } from './ajaxSetup.js';
import { setupPolypFormHandlers } from './polypFormHandlers.js';
import { updateColonAnatomyVisibility } from './anatomyHandlers.js';
import { attachDynamicFormListeners, openModal } from './modalHandlers.js';
import { click_delete_all_button } from './deleteAllButton.js';
import { delete_report_by_id } from './deleteReport.js';
import { fetchPatients, fetchReportPreview } from './patientReportHandlers.js';
import { createEditReport } from './create_report.js';
import { fetchReportTable } from './fetchReportTable.js';

let selectedPatientId = null;
let selectedReportId = null;
let n_initial_polyp_forms = null;

// Setup AJAX to include CSRF token
$.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
});


$(document).ready(function() {
    console.log("Document is ready!");
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    

    /////////////////////////
    // Patient Table
    /////////////////////////
    // Initialize the DataTables with additional options
    let patientTable = $('#patient-list').DataTable(
        {
            columns: [
                // { data: 'id' },
                { data: 'first_name' },
                { data: 'last_name' },
                { data: 'dob' },
                // { data: 'gender' }
            ],
            'paging': true,
            'lengthChange': false,
            'searching': true,
            'ordering': true,
            'info': true,
            'autoWidth': false,
            'responsive': true,
        }
    );

    let reportTable = $('#report-table').DataTable(
        {
            columns: [
                { data: 'id' },
                { data: 'date_of_procedure' },
            ],
            'paging': true,
            'lengthChange': false,
            'searching': true,
            'ordering': true,
            'info': true,
            'autoWidth': false,
            'responsive': true,
        }
    );

    // Fetch the initial data
    fetchPatients(patientTable);

    // Handling clicks on dynamically generated DataTable rows
    $('#patient-list tbody').on('click', 'tr', function() {
        let rowData = patientTable.row(this).data();
        console.log("Selected Patient data:", rowData);
        selectedPatientId = rowData.id;  // Assuming the ID is the first column
        let selectedPatientName = rowData.last_name + ', ' + rowData.first_name;  // Assuming first name is the second column and last name is the third
    
        $("#selected-patient-header").text(selectedPatientName);  // Update the header
        fetchReportTable(reportTable, selectedPatientId);
    });

    $('#report-table tbody').on('click', 'tr', function() {
        let rowData = reportTable.row(this).data();
        console.log("Selected Report data:", rowData);
        selectedReportId = rowData.id;
        fetchReportPreview(selectedReportId);
    });




    /////////////////////////
    // Main Buttons
    /////////////////////////
    document.getElementById('deleteAllButton').addEventListener(
        'click', function() {
            click_delete_all_button(csrfToken);
        }
    )
    
    //Patient
    // Open "Add Patient"
    $("#add-patient-btn").click(function() {
        selectedPatientId = null;  // Reset the selected patient ID
        openModal('/fetch_patient_form/', '#patientModal');
    });
    // Open "Edit Patient" modal
    $("#edit-patient-btn").click(function() {
        if (selectedPatientId) {
            openModal(`/fetch_patient_form/${selectedPatientId}/`, '#patientModal');
        }
    });
    // Handle the form submission for creating/editing a patient
    $("#save-patient-btn").click(function() {
        let formData = $("#patient-form").serialize();  // Serialize form data for submission
        let url = selectedPatientId ? `/save_patient/${selectedPatientId}/` : '/save_patient/';
        $.ajax({
            url: url,
            type: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,  // Include CSRF token
            },
            data: formData,
            success: function(response) {
                if (response.status === 'success') {
                    // Refresh the patient list and close the modal
                    fetchPatients(patientTable);
                    $("#patientModal").modal("hide");
                } else {
                    // Handle errors
                    alert("An error occurred: " + response.error);
                }
            }
        });
    });

    
    // Report
    // Open "Create Report" modal
    $("#create-report-btn").click(function() {
        selectedReportId = null;  // Reset the selected report ID
        console.log("Selected Patient ID:", selectedPatientId);
        $.ajax({
                url: `/create_report/${selectedPatientId}/`,
                type: 'POST',
                
                success: function(data) {
                    console.log("Server Response:", data.report_id);
                    selectedReportId = data.report_id;
                    openModal(`/fetch_report/${data.report_id}/`, '#reportModal');  // re-attach listeners
                }
            });
    });

    // Open "Edit Report" modal
    $("#edit-report-btn").click(function() {
        if (selectedReportId) {
            let url = `/fetch_report/${selectedReportId}/`;
            let modalId = '#reportModal';
            $.ajax({
                url: url,
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,  // Include CSRF token
                },
                data: {
                    'report_id': selectedReportId,
                },
                success: function(data) {
                    $(modalId + " .modal-body").html(data);
                    $(modalId).modal("show");
                    attachDynamicFormListeners();  // re-attach listeners
                }
            });
        }
    });
    
    // Handle the "Save" button click
    $("#save-report-btn").click(function() {

        let _data = $("#form");
        // console log form data in a readable format
        console.log("Form Data:", _data.fields);

        // Serialize the form data
        let formData = $("#form").serialize();

        // Determine the URL for the request
        let url = selectedReportId ? `/save_report/${selectedReportId}/` : `/save_report/`;

        // Make the AJAX request
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            success: function(response) {
                if (response.status === 'success') {
                    console.log("Saved Form Data:", formData)
                    // Refresh the report list if needed
                    fetchReportTable(reportTable, selectedPatientId);                
                    $("#reportModal").modal("hide");

                } else {
                    // Handle errors
                    // console.log("Error with saving form data:", formData)
                    alert("Error with saving form data:", formData);
                    // alert("An error occurred: " + response.error);
                }
            },
            error: function(xhr, status, error) {
                console.error("Request failed:");
                console.error("Status Code:", xhr.status);
                console.error("Status Text:", xhr.statusText);
                console.error("Response Text:", xhr.responseText);
            }
        });
    });


    // Handle the "Delete Report" button click.
    $("#delete-report-btn").click(function() {
        delete_report_by_id(csrfToken, selectedReportId)
            .then(() => {
                // Refresh the report list only if the deletion was successful or user canceled the action
                fetchReportTable(reportTable, selectedPatientId);
            })
            .catch(error => {
                // Handle any errors here
                console.error('Deletion failed:', error);
            });
        });
    
        // Handling clicks on dynamically generated report items
        $(document).on('click', '.report-item', function() {
        selectedReportId = $(this).data("report-id");
        fetchReportPreview(selectedReportId);
        });
  });
