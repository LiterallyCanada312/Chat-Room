const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data['message'];
    // Handle incoming message
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// Send message to server
function sendMessage(message) {
    chatSocket.send(JSON.stringify({
        'message': message
    }));
}