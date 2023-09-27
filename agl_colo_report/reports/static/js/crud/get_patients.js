export function getPatients() {
    return $.ajax({
        url: '/api/get_patients',
        type: 'GET',
        // Funtion returns a promise with the data
      });
}