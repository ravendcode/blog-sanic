(function () {
  'use strict';

  var port = location.port === '' ? '' : ':' + location.port;
  var wsUrl = 'ws://' + document.domain + port + '/echo';
  if (/https/.test(location.href)) {
    wsUrl = 'wss://' + document.domain  + '/echo';
  }

  var echoWs = new WebSocket(wsUrl);

  var messageFormElem = document.getElementById('message-form');
  var messagesUlElem = document.getElementById('messages');
  var messageInputElem = document.getElementById('message');


  messageFormElem.onsubmit = function (event) {
    event.preventDefault();

    echoWs.send(JSON.stringify({type: 'client', data: messageInputElem.value}));
    messageInputElem.value = '';
  };

  echoWs.onmessage = function (event) {
    var received = JSON.parse((event.data))
    var liElem = document.createElement('li');
    var content = document.createTextNode(received.type + ': ' + received.data);
    liElem.appendChild(content);
    messagesUlElem.appendChild(liElem);
  };

}());
