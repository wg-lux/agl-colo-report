import { getPatients } from './crud/get_patients.js';
import { createPatient } from './crud/create_patient.js';
import { openPatientModalListener } from './listeners/open_patient_modal.js';
import { updateCurrentPatientDataListener } from './listeners/patient_modal/current_patient_data.js';
import { initializeData } from "./initialize/main.js"

let currentPatientData = {};

$(document).ready(function() {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    
    // Add Listeners
    openPatientModalListener(document); // Open the modal when "add-patient-btn" button is clicked
    updateCurrentPatientDataListener(document); // Update currentPatientData when a form input is changed

    
    initializeData();

    getPatients()
        .done(function(data) {
            // Handle success
            console.log("Fetched patients:", data);
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            // Handle error
            console.log("Error fetching patients:", textStatus, errorThrown);
        })
        .always(function() {
            // Always executed after .done() or .fail()
            console.log("Ajax request completed.");
        });

    });
