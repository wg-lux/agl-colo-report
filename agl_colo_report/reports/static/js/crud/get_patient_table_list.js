export function getPatientTableList() {
    return $.ajax({
        url: "/api/patients/get-table/",
        type: "GET",
        success: function(data) {
            console.log("Fetched patients:", data);
            // updatePatientTable(currentPatientList); // Update the DataTable or other UI elements
        },
        error: function(error) {
            console.log("Error fetching patients:", error);
        }
    });
}
