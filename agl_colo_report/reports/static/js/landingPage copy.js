// static/js/landingPage.js
// This will hold the ID of the currently selected patient and report
let selectedPatientId = null;
let selectedReportId = null;


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function setupPolypFormHandlers() {
    console.log("Setting up polyp form handlers");
    const polypContainer = document.querySelector("#polyp-form-container");

    // Function to clone a polyp form

    function clonePolypForm() {
        const templateForm = document.querySelector("#polyp-template");
        if (templateForm) {
            return templateForm.cloneNode(true);
        }
        return null;
    }

    // Function to add a new polyp form
    function addPolypForm() {
        const newPolypForm = clonePolypForm();
        if (newPolypForm) {
            newPolypForm.style.display = "block"; // Make it visible

            // Count existing polyp forms to determine the index for the new form
            const existingForms = polypContainer.querySelectorAll('.polyp-form');
            const newIdx = existingForms.length + 1; // Since it's zero-based

            // Create a new label element
            const newLabel = document.createElement("label");
            newLabel.textContent = `Polyp ${newIdx}`;

            // Insert the new label at the beginning of the new polyp form
            newPolypForm.insertBefore(newLabel, newPolypForm.firstChild);

            // Append the new form to the container
            polypContainer.appendChild(newPolypForm);
        }
    }


    // Function to remove a polyp form
    function removePolypForm(event) {
        const button = event.target;
        const polypForm = button.closest('.polyp-form');
        polypForm.remove();
    }

    // Function to duplicate a polyp form
    function duplicatePolypForm(event) {
        const button = event.target;
        const polypForm = button.closest('.polyp-form');
        const duplicatedForm = polypForm.cloneNode(true);
        polypContainer.appendChild(duplicatedForm);
    }

    function updateManagementForm() {
        const totalForms = document.querySelectorAll('.polyp-form').length;
        const initialForms = document.querySelectorAll('.polyp-form.initial').length; // Assuming you add a class "initial" to pre-rendered forms
    
        document.getElementById('id_polyps-TOTAL_FORMS').value = totalForms;
        document.getElementById('id_polyps-INITIAL_FORMS').value = initialForms;
    }
    
    

    // Attach event listeners
    document.querySelector("#add-polyp-btn").addEventListener("click", addPolypForm);
    polypContainer.addEventListener("click", function(event) {
        if (event.target.classList.contains("remove-polyp-btn")) {
            removePolypForm(event);
        } else if (event.target.classList.contains("duplicate-polyp-btn")) {
            duplicatePolypForm(event);
        }
        updateManagementForm();
    });
}

function updateColonAnatomyVisibility() {
    const alteredColonAnatomySelect = document.querySelector("#id_altered_colon_anatomy");
    const colonAnatomySelect = document.querySelector("#id_colon_anatomy");
    const colonAnatomyFormGroup = colonAnatomySelect.closest('.form-group');

    function toggleColonAnatomy() {
        const selectedValue = alteredColonAnatomySelect.value;
        if (selectedValue === 'yes') {
            colonAnatomyFormGroup.style.display = "block";
        } else {
            colonAnatomyFormGroup.style.display = "none";
            colonAnatomySelect.value = 'colon_normal';  // Set to your default value
        }
    }

    // Initialize and toggle based on initial value
    toggleColonAnatomy();
    
    // Update whenever altered_colon_anatomy changes
    alteredColonAnatomySelect.addEventListener("change", toggleColonAnatomy);
}

function attachDynamicFormListeners() {
    updateColonAnatomyVisibility();
    setupPolypFormHandlers();

    console.log("Attaching dynamic form listeners");
    const colonAnatomySelect = document.querySelector("#id_colon_anatomy");
    const alteredColonAnatomy = document.querySelector("#id_altered_colon_anatomy");
    const deepestInsertionSelect = document.querySelector("#id_deepest_insertion");

    if (colonAnatomySelect) {
        function updateDeepestInsertionOptions() {
            console.log("Updating deepest insertion options")
            const selectedAnatomy = colonAnatomySelect.value;
            fetch(`/get_available_segments/${selectedAnatomy}/`)
                .then(response => response.json())
                .then(data => {
                    deepestInsertionSelect.innerHTML = "";
                    data.forEach(item => {
                        const option = document.createElement("option");
                        option.value = item.id;
                        option.text = item.name;
                        deepestInsertionSelect.appendChild(option);
                    });
                });
        }
        colonAnatomySelect.addEventListener("change", updateDeepestInsertionOptions);
        alteredColonAnatomy.addEventListener("change", updateDeepestInsertionOptions);
    }
}

// Also, attach listeners after dynamically loading the form
function openModal(url, modalId) {
    $.ajax({
        url: url,
        type: 'GET',
        success: function(data) {
            $(modalId + " .modal-body").html(data);
            $(modalId).modal("show");
            attachDynamicFormListeners();  // re-attach listeners
        }
    });
}
  
function openNewWindow(url) {
    window.open(url, '_blank', 'width=800,height=600,top=100,left=100');
}

function fetchPatients() {
  $.ajax({
    url: '/fetch_patients/',
    type: 'GET',
    success: function(data) {
      $("#patient-list").html(data);
    }
  });
}

function fetchReportsForPatient(patientId) {
  $.ajax({
    url: `/fetch_reports_for_patient/${patientId}/`,
    type: 'GET',
    success: function(data) {
      $("#report-list").html(data);
    }
  });
}

function fetchReportPreview(reportId) {
  $.ajax({
    url: `/fetch_report_preview/${reportId}/`,
    type: 'GET',
    success: function(data) {
      $("#report-preview").html(data);
    }
  });
}

$(document).ready(function() {
    // Initial fetch of patients
    fetchPatients();
  
    // Open "Add Patient" modal
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
            data: formData,
            success: function(response) {
                if (response.status === 'success') {
                    // Refresh the patient list and close the modal
                    fetchPatients();
                    $("#patientModal").modal("hide");
                } else {
                    // Handle errors
                    alert("An error occurred: " + response.error);
                }
            }
        });
    });

    // Open "Create Report" modal
    $("#create-report-btn").click(function() {
        selectedReportId = null;  // Reset the selected report ID
        if (selectedPatientId) {
            openModal(`/create_report/${selectedPatientId}`, '#reportModal');
        }
    });

    // Open "Edit Report" modal
    $("#edit-report-btn").click(function() {
        if (selectedReportId) {
            openModal(`/fetch_report/${selectedReportId}/`, '#reportModal');
        }
    });
    
    // Handle the "Save" button click
    $("#save-report-btn").click(function() {
        let formData = $("#report-form").serialize();
        let url = selectedReportId ? `/save_report/${selectedReportId}/` : `/save_report/`;
        
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            success: function(response) {
                if (response.status === 'success') {
                    // Refresh the report list if needed
                    if (selectedReportId) {
                        fetchReportsForPatient(selectedPatientId);
                        $("#reportModal").modal("hide");
                    }
                } else {
                    // Handle errors
                    alert("An error occurred: " + response.error);
                }
            }
        });
    });
  
    // Handling clicks on dynamically generated patient items
    $(document).on('click', '.patient-item', function() {
      selectedPatientId = $(this).data("patient-id");
      $("#selected-patient-header").text($(this).text());  // Update the header
      fetchReportsForPatient(selectedPatientId);
    });
  
    // Handling clicks on dynamically generated report items
    $(document).on('click', '.report-item', function() {
      selectedReportId = $(this).data("report-id");
      fetchReportPreview(selectedReportId);
    });
  
  });
