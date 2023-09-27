import { savePatientListener } from "../listeners/save_patient";

export function openPatientModalListener(document) {
  document.getElementById("add-patient-btn").addEventListener("click", function() {
    console.log("Opening patient modal");
    // console.log("Current patient data:", currentPatientData);
    // savePatientListener(document);
    $('#patientModal').modal('show');
  });
}