net = require 'net'

class Client

	DEFAULT_PORT: 12311
	DEFAULT_ADDR: "127.0.0.1"

	# start our client and connect to the server
	start: () ->
		@client = net.connect @DEFAULT_PORT

		@client.on 'connect', () ->
			@write "Hey suckah!"
			console.log "suckaH!"

		@client.on 'data', (data) ->
			console.log "Data received: " + data

c = new Client()
c.start()