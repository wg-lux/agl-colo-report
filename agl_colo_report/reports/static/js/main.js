import { openPatientModalListener } from "./listeners/patient_modal/main.js";
// import { updateCurrentPatientListener } from './listeners/patient_form.js';
import { initializeData } from './intitialize/main.js';
import { getPatientTableList } from './crud/get_patient_table_list.js';
import { getReportTableList } from "./crud/get_report_table_list.js";
import { saveCurrentPatientData } from './crud/save_patient.js';
import { createReportForPatient } from './crud/create_report.js';


let currentPatientData = {};
let currentPatientList = [];
let currentSelectedPatient = null;
let patientTable = null;
let currentReportList = [];
let currentSelectedReport = null;

initializeData(
    currentPatientData
);


$(document).ready(function() {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    

    //////////////////////////////// Initialize DataTables ////////////////////////////////
    // Patient Table
    const patientTable = $('#patientTable').DataTable({
        columns: [
            { data: 'first_name' },
            { data: 'last_name' },
            { data: 'dob' },
            { data: 'gender' },
            {
                data: null,
                defaultContent: '<button class="btn btn-secondary select-patient">Select</button>',
                orderable: false
            }
        ]
    });
    // Report Table
    const reportTable = $('#reportTable').DataTable({
        columns: [
            { data: 'date_of_procedure' },
            {
                data: null,
                defaultContent: '<button class="btn btn-secondary select-report">Select</button>',
                orderable: false
            }
        ]
    });
    //////////////////////////////// END Initialize DataTables ////////////////////////////////

    //////////////////////////////// REPORT FORM FUNCTIONS ////////////////////////////////////
    // attach save-report-btn event listener
    $(document).on('click', '#save-report-btn', function() {
        const reportId = currentSelectedReport.id;
        console.log("Saving report with id:", reportId);
    
        let formData = new FormData();
    
        let baseFormData = {};
        $('#base-report-form').serializeArray().forEach(item => {
            baseFormData[item.name] = item.value;
        });
    
        let premedicationFormData = {};
        $('#premedication-form').serializeArray().forEach(item => {
            premedicationFormData[item.name] = item.value;
        });

        let drugApplicationFormData = {};
        $('#drug-application-form').serializeArray().forEach(item => {
            drugApplicationFormData[item.name] = item.value;
        });
    
        formData.append('base_form_data', JSON.stringify(baseFormData));
        formData.append('premedication_form_data', JSON.stringify(premedicationFormData));
        formData.append('drug_application_formset_data', JSON.stringify(drugApplicationFormData));
    
        $.ajax({
            url: `/api/reports/update-report/${reportId}/`,
            type: 'PUT',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                console.log('Report updated successfully:', data);
            },
            error: function(error) {
                console.log('Error updating report:', error);
            }
        });
    });
    
    
    
    function insertReportFormIntoHTML(reportForms) {
        // Assume we have a <div id="report-form-container"></div> in our HTML
        const reportFormContainer = document.getElementById("base-report-form-container");
        const premedicationFormContainer = document.getElementById("premedication-form-container");
        const drugApplicationFormContainer = document.getElementById("drug-application-form-container");
        const polypFormContainer = document.getElementById("polyp-form-container");

        // Get html strings from reportForms
        let baseFormHTML = reportForms.base_form_data;
        let premedicationFormHTML = reportForms.premedication_form_data;
        let drugApplicationFormHTML = reportForms.drug_application_formset_data;
        let polypFormHTML = reportForms.polyp_formset_data;

        // Insert the HTML into the container
        reportFormContainer.innerHTML = baseFormHTML;
        premedicationFormContainer.innerHTML = premedicationFormHTML;
        drugApplicationFormContainer.innerHTML = drugApplicationFormHTML;
        polypFormContainer.innerHTML = polypFormHTML;
    };
    
    
    function fetchReportForm(reportId) {
        $.ajax({
            url: `/api/reports/get-report/${reportId}/`,
            type: 'GET',
            success: function(data) {
                // This function will handle inserting the form into the HTML
                console.log("Fetched report form:", data);
                const report_forms = data;
                insertReportFormIntoHTML(report_forms);

            },
            error: function(error) {
                console.log("Error fetching report form:", error);
            }
        });
    };

    // event listener for create polyp button
    $(document).on('click', '#create-polyp-btn', function() {
        console.log("Creating polyp");
        const reportId = currentSelectedReport.id;
        $.ajax({
            url: `/api/colon-polyp/create/`,
            type: 'POST',
            data: JSON.stringify({report_id: currentSelectedReport.id}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                console.log("Polyp created successfully:", data);
                fetchReportForm(reportId);
            },
            error: function(error) {
                console.log("Error creating polyp:", error);
            }
        });
    });

    
    
    function attachReportFormListeners() {
    // event listeners will catch changes to important fields
    // if a listener catches a change, update report in DB, fetch new report, and update form 
    
    };
    
    function renderReportForm() {
        // render forms with data from currentSelectedReport
        // attach event listeners to rendered forms

        // got replaced by the fetchReportForm function?????
        

    };
    //////////////////////////////// END REPORT FORM FUNCTIONS ////////////////////////////////

    //////////////////////////////// REPORT TABLE FUNCTIONS ///////////////////////////////////    
    function attachSelectReportListener() {
        $("#reportTable tbody").off("click", "button.select-report").on("click", "button.select-report", function() {
            const data = reportTable.row($(this).parents("tr")).data();
            currentSelectedReport = data;
            console.log("Function attachSelectReportListener");
            console.log("Selected report:", currentSelectedReport);
            // get current report id
            const reportId = currentSelectedReport.id;
            fetchReportForm(reportId);
        });
    };
    
    function updateReportTable() {
        const table = $("#reportTable").DataTable();
        table.clear();
        table.rows.add(currentReportList);
        table.draw();
    };
    
    function refreshReportTable() {
        getReportTableList(currentSelectedPatient).then(function(data) {
            currentReportList = data;
            console.log("Function refreshReportTable");
            console.log("Fetched reports:", data);
            updateReportTable(currentReportList);
            attachSelectReportListener();
        });
    }

    //////////////////////////////// END REPORT TABLE FUNCTIONS ////////////////////////////////

    //////////////////////////////// PATIENT TABLE FUNCTIONS ///////////////////////////////////
    function updateCurrentPatientInformationBlock() {
        // Reference to the HTML element
        const patientInfoBlock = document.getElementById('current-patient-information-block');
    
        // Check if currentSelectedPatient is not null
        if (currentSelectedPatient) {
            // Create HTML content to display patient data
            let patientInfoHtml = `
                <p><strong>ID:</strong> ${currentSelectedPatient.id}</p>
                <p><strong>First Name:</strong> ${currentSelectedPatient.first_name}</p>
                <p><strong>Last Name:</strong> ${currentSelectedPatient.last_name}</p>
                <p><strong>Date of Birth:</strong> ${currentSelectedPatient.dob}</p>
                <p><strong>Gender:</strong> ${currentSelectedPatient.gender}</p>
            `;
    
            // Set the HTML content to the div
            patientInfoBlock.innerHTML = patientInfoHtml;
        } else {
            // If currentSelectedPatient is null, clear the div
            patientInfoBlock.innerHTML = "<p>No patient selected.</p>";
        }
    }
    //initialize block
    updateCurrentPatientInformationBlock();
    function attachSelectPatientListener() {
        $('#patientTable tbody').off("click", "button.select-patient").on('click', 'button.select-patient', function () {
            const data = patientTable.row($(this).parents('tr')).data();
            currentSelectedPatient = data;
            console.log("Selected patient:", currentSelectedPatient);
            updateCurrentPatientInformationBlock();
            refreshReportTable();
        });
    };
    function updatePatientTable() {
        const table = $('#patientTable').DataTable();
        table.clear();
        table.rows.add(currentPatientList);
        table.draw();
    };

    function refreshPatientTable() {
        getPatientTableList().then(function(data) {
            currentPatientList = data;
            // console.log("Fetched patients:", data);
            updatePatientTable(currentPatientList);
            attachSelectPatientListener();
        });
    };
    refreshPatientTable();
    //////////////////////////////// END PATIENT TABLE FUNCTIONS ////////////////////////////////

    //////////////////////////////// PATIENT MODAL FUNCTIONS ///////////////////////////////////
    openPatientModalListener(document); // Open the modal when "add-patient-btn" button is clicked
    // add event listener to change the currentPatientData variable
    $(document).on('change', '#patientForm input, #patientForm select', function() {
        console.log("Updating current patient data");
        const key = $(this).attr('name');
        const value = $(this).val();
        currentPatientData[key] = value;
        console.log(currentPatientData);  // You can log it to see the changes
    });
    
    // EventListener
    $(document).on('click', '#savePatientBtn', function() {
        console.log("Saving patient");
        saveCurrentPatientData(currentPatientData, csrfToken)
            .done(function(data) {
                refreshPatientTable();
                $('#patientModal').modal('hide');
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                // Handle error
                console.log("Error saving patient:", textStatus, errorThrown);
            });
    });

    //////////////////////////////// END PATIENT MODAL FUNCTIONS ////////////////////////////////

    //////////////////////////////// CREATE REPORT BUTTON ///////////////////////////////////////
    $(document).on('click', '#create-report-btn', function() {
        console.log("Creating report for patient: ", currentSelectedPatient);
    
    // Call the createReportForPatient function and pass in currentSelectedPatient
    createReportForPatient(currentSelectedPatient)
        .done(function(data) {
            // Successfully created the report, refresh the report table
            console.log("Successfully created report: ", data);
            refreshReportTable();
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            // Handle error
            console.log("Error creating report:", textStatus, errorThrown);
        });
    });

});
