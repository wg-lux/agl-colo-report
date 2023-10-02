export function getReportTableList(currentSelectedPatient) {
    // Check if a patient is selected
    console.log("Getting report table list for patient:", currentSelectedPatient)
    if (currentSelectedPatient && currentSelectedPatient.id) {
        const url = `/api/reports/get-table/?patient_id=${currentSelectedPatient.id}`;
        return $.ajax({
            url: url,
            type: "GET",
            success: function(data) {
                console.log("Fetched reports:", data);
                // Update the DataTable or other UI elements
            },
            error: function(error) {
                console.log("Error fetching reports:", error);
            }
        });
    } else {
        console.log("No patient selected.");
        // Handle this case as needed
    }
}
