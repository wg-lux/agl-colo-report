import { updateCurrentPatientData } from '../../current_patient_data/update.js';

export function updateCurrentPatientDataListener(document) {
    const key = $(this).attr('name');
    const value = $(this).val();
    updateCurrentPatientData({ [key]: value });
};
