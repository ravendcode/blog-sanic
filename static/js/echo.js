(function () {
  'use strict';

  function connect() {
    var port = location.port === '' ? '' : ':' + location.port;
    var wsUrl = 'ws://' + document.domain + port + '/echows';
    if (/https/.test(location.href)) {
      wsUrl = 'wss://' + document.domain + '/echows';
    }
    var id;
    var connected = false;
    // var echoWs = new WebSocket(wsUrl);
    var echoWs = new ReconnectingWebSocket(wsUrl);

    var messageFormElem = document.getElementById('message-form');
    var messagesUlElem = document.getElementById('messages');
    var messageInputElem = document.getElementById('message');
    var idElem = document.getElementById('id');

    echoWs.onopen = function () {
      // console.log('open ws');
    }

    echoWs.onmessage = function (event) {
      var received = JSON.parse((event.data))
      if (received.type === 'server:hello') {
        id = received.id;
        idElem.innerText = received.id;
        if (!connected) {
          var liElem = document.createElement('li');
          content = document.createTextNode(received.type + ': ' + received.data);
          liElem.appendChild(content);
          messagesUlElem.appendChild(liElem);
          connected = true;
        }
      }

      if (received.type === 'client') {
        var liElem = document.createElement('li');
        var content = document.createTextNode(received.id + ': ' + received.data);
        liElem.appendChild(content);
        messagesUlElem.appendChild(liElem);
      }
    };

    echoWs.onclose = function (event) {
      console.log('Socket is closed. Reconnect will be attempted in 1 second.');
      // setTimeout(function () {
      //   connect();
      // }, 1000);
    };

    messageFormElem.onsubmit = function (event) {
      event.preventDefault();

      echoWs.send(JSON.stringify({
        id: id,
        type: 'client',
        data: messageInputElem.value
      }));
      messageInputElem.value = '';
    };
  }

  connect();
}());

