// deleteAllButton.js

export function click_delete_all_button(csrfToken) {
    if (confirm('Are you sure you want to delete all entries? This action cannot be undone.')){
        fetch('/delete_all_entries/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,  // Include CSRF token
            },
        })
        .then(response => {
            if (!response.ok) {
                return response.text().then(text => { throw new Error(text) });
            }
            return response.json();
        })
        .then(data => {
            if (data.status === 'success') {
                alert('All entries have been deleted successfully.');
            } else {
                alert('An error occurred while deleting entries.');
            }
        })
        .catch(error => {
            console.error('Fetch Error:', error);
        });
    }}