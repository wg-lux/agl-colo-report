// static/js/reportFormPartial.js
// Execute code when the document is fully loaded
$(document).ready(function () {

    // Initialize form index by counting the number of existing polyp forms
    let formIdx = $('#polyp-formset-wrapper .polyp-form').length;

    // Function to toggle the visibility of the 'Colon Anatomy' field
    function toggleColonAnatomyField() {
        // Get the value of the selected 'Altered Colon Anatomy' option
        const alteredValue = $("input[name='altered_colon_anatomy']:checked").val();

        // Show or hide the 'Colon Anatomy' field based on the selected value
        if (alteredValue === 'yes') {
            $("#id_colon_anatomy").closest('.form-group').show();
        } else {
            $("#id_colon_anatomy").closest('.form-group').hide();
        }
    }

    // Function to update the indices of form elements
    function updateElementIndex(el, prefix, ndx) {
        const idRegex = new RegExp(`${prefix}-\\d+-`);
        const replacement = `${prefix}-${ndx}-`;

        // Update the 'for', 'id', and 'name' attributes to use the new index
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(idRegex, replacement));
        if (el.id) el.id = el.id.replace(idRegex, replacement);
        if (el.name) el.name = el.name.replace(idRegex, replacement);
    }

    // Call the function once to set the initial state of 'Colon Anatomy' field
    toggleColonAnatomyField();

    // Attach a change event to toggle the 'Colon Anatomy' field whenever 'Altered Colon Anatomy' changes
    $("input[name='altered_colon_anatomy']").change(toggleColonAnatomyField);

    // Function to clone a form and add it to the formset
    function cloneMore(selector, prefix) {
        // Clone the template form
        const newElement = $(selector).clone(true);
        newElement.removeAttr("style"); // Make the form visible

        // Get the total number of forms currently in the formset
        const total = $('#id_' + prefix + '-TOTAL_FORMS').val();

        // Remove any existing <strong> labels to avoid duplication
        newElement.find('strong').remove();

        // Create a new label to indicate the polyp form number
        const polypNumber = parseInt(total) + 1;
        const polypLabel = $('<strong>').text('Polyp Form #' + polypNumber);

        // Add the new label to the form
        newElement.prepend(polypLabel);

        // Update indices of form elements
        newElement.find(':input').each(function () {
            updateElementIndex(this, prefix, total);
        });

        // Add the new form to the formset
        $('#polyp-formset-wrapper').append(newElement);

        // Update the total number of forms in the management form
        $('#id_' + prefix + '-TOTAL_FORMS').val(polypNumber);

        // Clone an empty location form and add it to the new polyp form
        const locationForm = $("#empty-location-form").clone(true);
        locationForm.removeAttr("style");
        locationForm.removeAttr("id");
        newElement.append(locationForm);
    }

    // Toggle the visibility of the polyp forms when the button is clicked
    $('#toggle-polyp-forms').click(function () {
        $('#polyp-formset-wrapper').toggle();
    });

    // Prevent the default form submission to handle it with AJAX
    $("#reportForm").submit(function (event) {
        event.preventDefault();
    });

    // Remove any empty polyp forms
    $(".polyp-form").each(function () {
        const inputs = $(this).find('input, select');
        let allEmpty = true;

        // Check if all fields in the form are empty
        inputs.each(function () {
            if ($(this).val()) {
                allEmpty = false;
                return false;
            }
        });

        // Remove the form if it's empty
        if (allEmpty) {
            $(this).remove();
        }
    });

    // Add a new polyp form when the 'Add Polyp' button is clicked
    $('#add-polyp-form').click(function () {
        cloneMore('#empty-polyp-form', 'form');
        return false;
    });

    // Handle form submission with AJAX
    $("#reportForm").submit(function (event) {
        event.preventDefault(); // Prevent default form submission

        // Serialize the form data
        const formData = $(this).serialize();

        // Make an AJAX POST request to submit the form
        $.ajax({
            url: '/reports/create_report/', // URL endpoint for form submission
            type: 'POST',
            data: formData,
            success: function (response) {
                // Handle success
                if (response.status === 'ok') {
                    alert('Report successfully saved!');
                    location.reload();
                } else {
                    alert('Failed to save report!');
                }
            },
            error: function (error) {
                // Handle errors
                alert('An error occurred while saving the report!');
            }
        });
    });
});
