// polypFormHandlers.js

/**
 * Initializes and sets up the handlers for the polyp form.
 */

// Function to clear form fields
function clearFormFields(form) {
    form.querySelectorAll("input, select, textarea").forEach(function(input) {
        if (input.type !== 'hidden') {
            input.value = '';
        }
    });
}

// Function to update form attributes
function updateFormAttributes(form, newPolypId, isBackendId = false) {
    form.querySelectorAll("input, select, textarea").forEach(function(input) {
        if (input.name) {
            input.name = input.name.replace('empty', newPolypId);
        }
        if (input.id) {
            input.id = input.id.replace('empty', newPolypId);
        }
    });

    if (isBackendId) {
        form.setAttribute('data-backend-id', newPolypId);
    } else {
        form.setAttribute('data-temp-id', newPolypId);
    }
}

function addNewPolyp() {
    const emptyPolypForm = document.getElementById("polyp-form-empty-template");
    const newPolypForm = emptyPolypForm.cloneNode(true);  // Deep clone
    newPolypForm.style.display = "block";  // Make it visible
    clearFormFields(newPolypForm);

    // Update form attributes to associate with the new polyp
    updateFormAttributes(newPolypForm, newPolypCounter);

    // Decrement the counter for the next new polyp
    newPolypCounter--;

    // Append the new form to the container
    document.getElementById("polyp-form-container").appendChild(newPolypForm);
}

function removePolyp(event) {
    
    if (event.target.classList.contains("remove-polyp-btn")) {
        const polypForm = event.target.closest(".polyp-form");
        polypForm.remove();
    }

}

// document.addEventListener("DOMContentLoaded", function() {
//     let newPolypCounter = -1; // Counter for new polyps

    
    

//     // Add new polyp
//     document.getElementById("add-polyp-btn").addEventListener("click", function() {
        
//     });

//     // Remove polyp
//     document.addEventListener("click", function(event) {
//     });
// });


// export function setupPolypFormHandlers() {
    
//     console.log("Setting up polyp form handlers");
//     const polypContainer = document.querySelector("#polyp-form-container");

//     // Function to clone a polyp form

//     function clonePolypForm() {
//         const templateForm = document.querySelector("#polyp-template");
//         if (templateForm) {
//             return templateForm.cloneNode(true);
//         }
//         return null;
//     }

//     // Function to add a new polyp form
//     function addPolypForm() {
//         const newPolypForm = clonePolypForm();
//         if (newPolypForm) {
//             newPolypForm.style.display = "block"; // Make it visible

//             // Count existing polyp forms to determine the index for the new form
//             const existingForms = polypContainer.querySelectorAll('.polyp-form');
//             const newIdx = existingForms.length + 1; // Since it's zero-based

//             // Create a new label element
//             const newLabel = document.createElement("label");
//             newLabel.textContent = `Polyp ${newIdx}`;

//             // Insert the new label at the beginning of the new polyp form
//             newPolypForm.insertBefore(newLabel, newPolypForm.firstChild);

//             // Append the new form to the container
//             polypContainer.appendChild(newPolypForm);
//         }
//     }


//     // Function to remove a polyp form
//     function removePolypForm(event) {
//         const button = event.target;
//         const polypForm = button.closest('.polyp-form');
//         polypForm.remove();
//     }

//     // Function to duplicate a polyp form
//     function duplicatePolypForm(event) {
//         const button = event.target;
//         const polypForm = button.closest('.polyp-form');
//         const duplicatedForm = polypForm.cloneNode(true);
//         polypContainer.appendChild(duplicatedForm);
//     }

//     function updateManagementForm() {
//         const totalForms = document.querySelectorAll('.polyp-form').length;
//         // const initialForms = document.querySelectorAll('.polyp-form.initial').length; // Assuming you add a class "initial" to pre-rendered forms
    
//         document.getElementById('id_polyp-TOTAL_FORMS').value = totalForms;
//         // document.getElementById('id_polyps-INITIAL_FORMS').value = initialForms;
//     }
    

//     // Attach event listeners
//     updateManagementForm(); // initial setup
//     document.querySelector("#add-polyp-btn").addEventListener("click", addPolypForm);
//     polypContainer.addEventListener("click", function(event) {
//         if (event.target.classList.contains("remove-polyp-btn")) {
//             removePolypForm(event);
//         } else if (event.target.classList.contains("duplicate-polyp-btn")) {
//             duplicatePolypForm(event);
//         }
//         updateManagementForm();
//     });
// }
