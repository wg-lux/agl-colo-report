// ajaxSetup.js

/**
 * Retrieves the value of a cookie by its name.
 * @param {string} name - The name of the cookie to fetch.
 * @returns {string|null} - The value of the cookie or null if not found.
 */
export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) {
                cookieValue = decodeURIComponent(value);
                break;
            }
        }
    }
    return cookieValue;
}


