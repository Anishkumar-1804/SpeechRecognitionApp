document.addEventListener('DOMContentLoaded', function () {
    const startBtn = document.getElementById("startBtn");
    const stopBtn = document.getElementById("stopBtn");
    const recordingIndicator = document.getElementById("recordingIndicator");
    const outputDiv = document.getElementById("output");

    let isRecording = false;

    startBtn.onclick = async function () {
        startBtn.disabled = true;
        stopBtn.disabled = false;
        recordingIndicator.style.display = "block";
        outputDiv.innerText = "";

        const response = await fetch("/transcribe", { method: "POST" });
        const result = await response.text();
        outputDiv.innerText = result;

        recordingIndicator.style.display = "none";
        startBtn.disabled = false;
        stopBtn.disabled = true;
    };

    stopBtn.onclick = function () {
        // We simulate a "stop" since `speech_recognition` auto-stops on silence.
        alert("Recording will auto-stop when speech ends.");
    };
});
