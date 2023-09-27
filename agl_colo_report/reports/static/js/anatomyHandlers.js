// anatomyHandlers.js

/**
 * Initializes and sets up the handlers for the anatomy form.
 */
export function updateColonAnatomyVisibility() {
    const alteredColonAnatomySelect = document.querySelector("#id_altered_colon_anatomy");
    const colonAnatomySelect = document.querySelector("#id_colon_anatomy");
    const colonAnatomyFormGroup = colonAnatomySelect.closest('.form-group');

    function toggleColonAnatomy() {
        const selectedValue = alteredColonAnatomySelect.value;
        if (selectedValue === 'yes') {
            colonAnatomyFormGroup.style.display = "block";
        } else {
            colonAnatomyFormGroup.style.display = "none";
            colonAnatomySelect.value = 'colon_normal';  // Set to your default value
        }
    }

    // Initialize and toggle based on initial value
    toggleColonAnatomy();
    
    // Update whenever altered_colon_anatomy changes
    alteredColonAnatomySelect.addEventListener("change", toggleColonAnatomy);
}
