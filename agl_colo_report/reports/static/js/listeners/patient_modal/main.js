import { resetCurrentPatientData } from "../../current_patient_data/reset.js";

export function openPatientModalListener(document) {
  document.getElementById("add-patient-btn").addEventListener("click", function () {
    console.log("Opening patient modal");
    // savePatientListener(document);
    $('#patientModal').modal('show');
  });
}

export function closePatientModalListener(document) {
    document.getElementById("patientModalClose").addEventListener("click", function () {
        console.log("Closing patient modal");
        $('#patientModal').modal('hide');
    });

    $('#patientModal').on('hidden.bs.modal', function () {
        $('#patientForm')[0].reset();
        resetCurrentPatientData();
    });
}
