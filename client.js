// Generated by CoffeeScript 1.3.3
(function() {
  var Client, c, net;

  net = require('net');

  Client = (function() {

    function Client() {}

    Client.prototype.DEFAULT_PORT = 12311;

    Client.prototype.DEFAULT_ADDR = "127.0.0.1";

    Client.prototype.start = function() {
      console.log("hello");
      return this.client = net.connect({
        port: this.DEFAULT_PORT
      }, function() {
        return console.log('client connected');
      });
    };

    return Client;

  })();

  c = new Client();

  c.start();

}).call(this);
