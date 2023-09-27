export function savePatient() {
    // log necessary globals
    console.log("Saving patient");
    console.log("Current patient data:", currentPatientData);
    console.log("CSRF token:", csrftoken);
    return $.ajax({
        url: '/api/patient/',
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        data: $('#patientForm').serialize(),
        success: function(response) {
            if(response.success) {
                // Close modal and refresh page or data
                $('#patientModal').modal('hide');
            } else {
                // Handle form errors
            }
        }
    });
}
