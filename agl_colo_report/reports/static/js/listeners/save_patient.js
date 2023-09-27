// Event listener for form submission
import { savePatient } from '../crud/save_patient.js';

export function savePatientListener(document) {
    document.getElementById('#save-patient-btn').addEventListener("click", function() {
        savePatient();
    });
};