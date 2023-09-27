// deleteReport.js

export function delete_report_by_id(csrfToken, report_id) {
    return new Promise((resolve, reject) => {
        if (confirm('Are you sure you want to delete the report with ID ' + report_id + '? This action cannot be undone.')){
            fetch('/delete_report/' + report_id + '/', {
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
                    alert('Report with ID ' + report_id + ' has been deleted successfully.');
                    resolve(data);  // Resolve the promise
                } else {
                    alert('An error occurred while deleting Report with ID ' + report_id);
                    reject(new Error('Deletion failed'));  // Reject the promise
                }
            })
            .catch(error => {
                console.error('Fetch Error:', error);
                reject(error);  // Reject the promise
            });
        } else {
            resolve(null);  // User canceled the action; resolve the promise
        }
    });
}
