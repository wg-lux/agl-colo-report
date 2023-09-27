export function serialize_patient_form() {
    const patientData = $('#patientForm').serializeArray().reduce(function(obj, item) {
      obj[item.name] = item.value;
      return obj;
    }, {});
}