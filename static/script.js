
// Simple frontend logic for flash auto-dismiss
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = 'none';
        }, 4000); // hide after 4 seconds
    });
});

// Appointment Form Enhancer (date picker fallback or format)
function validateAppointmentForm() {
    const dateField = document.querySelector('#appointmentDate');
    const timeField = document.querySelector('#appointmentTime');
    if (!dateField.value || !timeField.value) {
        alert("Please fill in both date and time for the appointment.");
        return false;
    }
    return true;
}

// Toggle password visibility
function togglePassword(id) {
    const field = document.getElementById(id);
    if (field.type === 'password') {
        field.type = 'text';
    } else {
        field.type = 'password';
    }
}
