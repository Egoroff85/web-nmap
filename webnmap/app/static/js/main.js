let checkboxes = document.getElementsByName("is_active");

function changeScheduleState(e) {
    let xhr = new XMLHttpRequest();
    let csrftoken = Cookies.get('csrftoken');
    xhr.open('POST', '/toggle_schedule/', true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.setRequestHeader("X_REQUESTED_WITH", "XMLHttpRequest");
    let body = JSON.stringify(
        {"id": e.target.id,
        "is_active": e.target.checked}
    );
    xhr.onload = () => {
        console.log(xhr.response);
    };
    xhr.send(body);
}

for (let checkbox of checkboxes) {
  checkbox.addEventListener('change', changeScheduleState);
}

document.getElementById("id_add_schedule_0").onload = scheduleHide();

function scheduleHide() {
    let noSchedule = document.getElementById("id_add_schedule_0");
    let intervalTitle = document.querySelector("label[for='id_interval_0']");
    let intervalCheckboxes = document.getElementById("id_interval");
    if (noSchedule.checked) {
        intervalTitle.hidden = true;
        intervalCheckboxes.hidden = true;
    } else {
        intervalTitle.hidden = false;
        intervalCheckboxes.hidden = false;
    }
}

let scheduleRadioButtons = document.getElementsByName("add_schedule");

for (let radioButton of scheduleRadioButtons) {
  radioButton.addEventListener('change', scheduleHide);
}