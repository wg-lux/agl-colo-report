export function createPatient(patientData, csrfToken) {
    $.ajax({
        url: "/api/patient/create/",  // Update this URL based on your API endpoint
        method: "POST",
        headers: {
            'X-CSRFToken': csrfToken,  // Include CSRF token
        },
        data: JSON.stringify(patientData),
        contentType: "application/json",
        success: function(response) {
          // Handle success
          // Close the modal
          $('#patientModal').modal('hide');
        },
        error: function(response) {
          // Handle error
        }
      });
    }