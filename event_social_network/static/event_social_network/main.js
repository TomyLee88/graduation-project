//this function help with date selector over crispy forms. In event creating/edit forms //
document.addEventListener("DOMContentLoaded", function() {
    var dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        input.classList.add('custom-date-input');
        input.placeholder = 'Select date...';
    });
});
document.addEventListener("DOMContentLoaded", function() {
    var timeInputs = document.querySelectorAll('input[type="time"]');
    timeInputs.forEach(function(input) {
        input.classList.add('custom-time-input');
        input.placeholder = 'Select time...';
    });
});
