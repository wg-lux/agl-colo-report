// Event listener for modal close
import { resetCurrentPatientData } from './patient_modal/current_patient_data.js';

$('#patientModal').on('hidden.bs.modal', function() {
    $('#patientForm')[0].reset();
    resetCurrentPatientData();
});