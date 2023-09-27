
// This function will remove a polyp form
export function removePolypForm(csrfToken, polypId) {
    $.ajax({
        url: `/remove_polyp/${polypId}/`,
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