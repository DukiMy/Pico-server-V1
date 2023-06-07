import machine
from web_server import WebServer

def start_server():

    try:
        ip = WebServer.connect()					# Stores the picos ip-number
        connection = WebServer.open_socket(ip)	# Stores the connection object
        WebServer.serve(connection)				# Takes requests and serves the connected client device.
    except KeyboardInterrupt:			# Handles the ctrl+c command.
        machine.reset()

start_server()