import { getInitialPatientForm } from "./patient_form.js";

export function initializeData(currentPatientData) {
    getInitialPatientForm(currentPatientData);
    console.log("Current patient data after initializing:", currentPatientData);
}