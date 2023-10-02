export function getInitialPatientForm(currentPatientData) {
    // Get the form from the server
    $.get("/api/patient/")  // Replace with your actual API endpoint
        .done(function(data) {
            // Insert the form into the modal
            $('#patientModal .modal-body').html(data.form_html);

            // Initialize currentPatientData with the initial data from the server
            currentPatientData = data.initial_data;

            // Populate the form fields with the initial data
            for (const [key, value] of Object.entries(currentPatientData)) {
                $(`#patientModal [name="${key}"]`).val(value);
            }
        })
        .fail(function() {
            console.log("Error getting the form.");
        });
}