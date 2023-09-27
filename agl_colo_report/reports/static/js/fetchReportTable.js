// fetchReportTable.js

export function fetchReportTable(table, patientId) {
    $.ajax({
        url: "/fetch_reports_for_patient/" + patientId + "/",
        type: "GET",
        dataType: "json",
        success: function (data) {
            let parsed_data = JSON.parse(data.reports);

            // Clear existing data
            table.clear();
            let flattened_data = parsed_data.map(report => ({
                id: report.pk,
                patient_id: report.fields.patient,
                date_of_procedure: report.fields.date_of_procedure,
            }));
            console.log(flattened_data);

            // Add new data to the table
            table.rows.add(flattened_data).draw();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("AJAX error:", textStatus, errorThrown);
            console.log(jqXHR);
            let parsed_data = JSON.parse(data);
            console.log(parsed_data);
        }
    })
}