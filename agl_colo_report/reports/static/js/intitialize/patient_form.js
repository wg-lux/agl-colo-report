import { updateCurrentPatientData } from "../listeners/patient_modal/current_patient_data";

export function getInitialPatientForm() {
    $.get("/api/patient/")  // Replace with your actual API endpoint
        .done(function(data) {
            $('#patientModal .modal-body').html(data.form_html);  // Insert the form into the modal
        })
        .fail(function() {
            console.log("Error getting the form.");
        });
}