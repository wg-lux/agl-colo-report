// patientReportHandlers.js

/**
 * Fetches and displays the list of patients.
 */

// export function fetchPatients() {
//     $.ajax({
//         url: '/fetch_patients/',
//         type: 'GET',
//         success: function(data) {
//           $("#patient-list").html(data);
//         }
//       });
// }



export function fetchPatients(table) {
    $.ajax({
      url: '/fetch_patients/', 
      method: 'GET',
      dataType: 'json',
      success: function(data) {
        // Parse the serialized Django QuerySet
        let parsed_data = JSON.parse(data.patients);  

        // Clear existing data
        table.clear();

        // Flatten the data and add new rows
        let flattened_data = parsed_data.map(patient => ({
          id: patient.pk,
          first_name: patient.fields.first_name,
          last_name: patient.fields.last_name,
          dob: patient.fields.dob,
          gender: patient.fields.gender
        }));

        // Add new data to the table
        table.rows.add(flattened_data).draw();

        // Draw the table
        table.draw();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log("AJAX error:", textStatus, errorThrown);
        console.log(jqXHR);
        let parsed_data = JSON.parse(data);
        console.log(parsed_data);
      }
  });
}


/**
 * Fetches and displays the preview of the selected report.
 * @param {number} reportId - ID of the selected report.
 */
export function fetchReportPreview(reportId) {
    $.ajax({
        url: `/fetch_report_preview/${reportId}/`,
        type: 'GET',
        success: function(data) {
          $("#report-preview").html(data);
        }
    });
}

