import { openModal } from "./modalHandlers.js";

export function createReport(title, content) {
    $.ajax({
      url: '/create_report/',  // Replace with the URL of your Django view for creating reports
      method: 'POST',
      data: {
        'title': title,
        'content': content,
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
      },
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          console.log("Report successfully created with ID:", response.report_id);
          // You can also refresh your list of reports or do something else here
        } else {
          console.log("Failed to create report.");
        }
      },
      error: function(error) {
        console.log("An error occurred: ", error);
      }
    });
  }

  
  export function createEditReport(title, content) {
    $.ajax({
      url: '/create_report/',  // Replace with the URL of your Django view for creating reports
      method: 'POST',
      data: {
        'title': title,
        'content': content,
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
      },
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          console.log("Report successfully created with ID:", response.report_id);
          
          // Redirect to the new URL that includes the report_id
          openModal(`/fetch_report/${response.report_id}/`, '#reportModal');
        } else {
          console.log("Failed to create report.");
        }
      },
      error: function(error) {
        console.log("An error occurred: ", error);
      }
    });
  }