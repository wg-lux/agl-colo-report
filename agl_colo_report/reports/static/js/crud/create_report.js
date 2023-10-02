export function createReportForPatient(patientData) {
    return $.ajax({
        url: '/api/reports/create/',
        type: 'POST',
        data: JSON.stringify({patient: patientData}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(response) {
            console.log("Report successfully created:", response);
        },
        error: function(error) {
            console.log("Error creating report:", error);
        }
    });
}
