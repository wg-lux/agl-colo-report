import { savePatient } from "../crud/save_patient";

export function updateCurrentPatientListener(document) {
    $('#patientForm input, #patientForm select').on('change', function() {
        const key = $(this).attr('name');
        const value = $(this).val();
        updateCurrentPatientData({ [key]: value });
    });
}


// $(document).on('click', '#savePatientBtn', function() {
//     savePatient()
// });