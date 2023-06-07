'''
Source: https://projects.raspberrypi.org/en/projects/get-started-pico-w/1
Source: https://youtu.be/eym8NpHr9Xw
Compilation: Durim Miziraj
2023-06-04T21:55:19
'''

import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
from network_credentials import NetworkCredentials
from webpage import WebPage
from LED_light_manipulation import PicoLight
from uptime_formatter import StandardFormat
import machine
import uptime_formatter

class WebServer:

    ssid = NetworkCredentials.home_ssid
    password = NetworkCredentials.home_password

    def connect():
        #Connect to WLAN
        wlan = network.WLAN(network.STA_IF) # Connect as a station interface. STA_IF meaning as any other device that normally connects to it.
        wlan.active(True)					# Turns on the wifi-interface
        wlan.connect(WebServer.ssid, WebServer.password)		# Ask the interaface to connect to the network whose ssid is provided, with the provided password.
        while wlan.isconnected() == False:	# While the interface is not connected, print message and wait for 1 sec, do this until it is connected
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]				# Sets the ip adress of the pico. Length of the array is four, where router ip is the last, and the pico adress is the first.
        print(f'Connected on {ip}')
        return ip

    def open_socket(ip):
        # Open a socket
        address = (ip, 80) 					# Port 80 is the default port for http requests.
        connection = socket.socket()		# Creating a socket.
        connection.bind(address ) 			# Binding the socket to the ip and port number.
        connection.listen(1)				# Starts listening to requests that come in. The number is the max size of the queue for requests.
        print("listening on", address)
        return connection

    def serve(connection):
        #Start a web server
        pico_led.off()					# Turns off the led.
        pico_led_state = 'OFF'			# Sets the led state variable to off
        temperature = 0					# Sets the temperature variable to 0
        light = PicoLight()             # Create an instance of PicoLight

        # Main loop which never stops as long as the program is running
        while True:
            client = connection.accept()[0]		# Accepts the connection of the device that is connectiong to it
            request = client.recv(1024)			# Recieving data (a request) from the client device that is up to 1 kb (1024 bytes)
            request = str(request)				# Stores the request as a string.
            try:
                request = request.split()[1]	# First index is a html GET method, the other is the type of request.
            except IndexError:					# Catches errors when the request does not have any specified GET variable
                pass							# If the said error is encountered, then 'pass' doesnt let it crash the program, instead it lets it continue on.
            if request == '/lighton?':			# Checks if the request type is '/lighton?', if so. Then it turns light on and sets the status to on
                pico_led.on()
                pico_led_state = 'ON'
            elif request == '/lightoff?':		# Checks if the request type is '/lightoff?', if so. Then it turns light off and sets the status to off
                pico_led.off()
                pico_led_state = 'OFF'
            elif request == '/blink?':
                light.blink(15, 5)	# Blinks at 15hz for 5 seconds
                        
            temperature = round(pico_temp_sensor.temp)			# Stores the temperature of the pico.
            html = WebPage.firstPage(temperature,
                                     pico_led_state,
                                     StandardFormat.formatted_uptime_info(),
                                     str(machine.freq()).rstrip('0')
                                     )	# Stores the html code with the variables that are meant to be shown to the user.
            client.send(html)							# Sends the html code to the client.
            client.close()								# Closes the connection to the client device
