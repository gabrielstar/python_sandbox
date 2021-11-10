registerListeners();

function registerListeners() {
    document.addEventListener("submit", handleSubmit);
}

function handleSubmit(e) {
    e.preventDefault();
    document.getElementById("messageBox").innerHTML = "Prediction submitted @ " + new Date();
}
