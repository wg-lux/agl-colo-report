// This function will add a new polyp form
export function addPolypForm(csrfToken, selectedReportId) {
    $.ajax({
        url: `/add_polyp/${selectedReportId}/`,
        type: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        success: function(data) {
            if (data.status === 'success') {
                // Add code to update the DOM
            }
        }
    });
}
