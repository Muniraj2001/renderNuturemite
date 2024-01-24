// chatbot.js

function sendMessage() {
    var messageInput = document.getElementById("message-input");
    var message = messageInput.value;

    if (message.trim() === "") {
        return;
    }

    appendMessage("user", message);
    messageInput.value = "";

    // You can add logic to send the user's message to the backend for processing

    // For demonstration purposes, let's simulate a simple bot response
    setTimeout(function() {
        var botResponse = "I received your message: " + message;
        appendMessage("bot", botResponse);
    }, 500);
}

function appendMessage(sender, text) {
    var chatBox = document.getElementById("chat-box");
    var messageElement = document.createElement("div");
    messageElement.className = "message " + sender;
    messageElement.innerHTML = "<p>" + text + "</p>";
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
