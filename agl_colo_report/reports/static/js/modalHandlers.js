// modalHandlers.js

import { setupPolypFormHandlers } from './polypFormHandlers.js';
import { updateColonAnatomyVisibility } from './anatomyHandlers.js';



export function attachDynamicFormListeners() {
    updateColonAnatomyVisibility();
    setupPolypFormHandlers();

    const colonAnatomySelect = document.querySelector("#id_colon_anatomy");
    const alteredColonAnatomy = document.querySelector("#id_altered_colon_anatomy");
    const deepestInsertionSelect = document.querySelector("#id_deepest_insertion");

    if (colonAnatomySelect) {
        function updateDeepestInsertionOptions() {
            console.log("Updating deepest insertion options")
            let selectedAnatomy = colonAnatomySelect.value;
            
            // If selectedAnatomy is empty or not provided, set it to "colon-normal"
            if (!selectedAnatomy) {
                selectedAnatomy = "1"; // "colon-normal"
            }

            fetch(`/get_available_segments/${selectedAnatomy}/`)
                .then(response => response.json())
                .then(data => {
                    deepestInsertionSelect.innerHTML = "";
                    data.forEach(item => {
                        const option = document.createElement("option");
                        option.value = item.id;
                        option.text = item.name;
                        deepestInsertionSelect.appendChild(option);
                    });
                });
        }
        colonAnatomySelect.addEventListener("change", updateDeepestInsertionOptions);
        alteredColonAnatomy.addEventListener("change", updateDeepestInsertionOptions);
        // Add an event listener to all checkboxes
        document.querySelectorAll('input[data-toggle-form]').forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
        const formId = this.getAttribute('data-toggle-form');
        const formElement = document.getElementById(formId);
        
        if (this.checked) {
            formElement.style.display = 'block';
        } else {
            formElement.style.display = 'none';
        }
    });
});
    }
}


/**
 * Opens a modal and fills its body with content fetched from the given URL.
 * @param {string} url - URL to fetch modal content from.
 * @param {string} modalId - ID of the modal to be populated.
 */
export function openModal(url, modalId) {
    $.ajax({
        url: url,
        type: 'GET',
        success: function(data) {
            $(modalId + " .modal-body").html(data);
            $(modalId).modal("show");

            attachDynamicFormListeners();  // re-attach listeners
        }
    });
}
