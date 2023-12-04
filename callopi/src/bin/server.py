'''
Callopi web server
Author: Christian Alvarez
Start Date: 10/22/2023
'''

#import requests
import http.server
import socketserver
import threading

class CServer:
    def __init__(self):
        self.stopServerEvent = threading.Event()

    def server(self):
        try:
            PORT = 8080
            Handler = http.server.SimpleHTTPRequestHandler

            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(f'Serving at http://localhost:{PORT}')
                ServerThread = threading.Thread(target = httpd.serve_forever())
                ServerThread.daemon = True
                ServerThread.start()

                # wait for server to be stopped
                self.stopServerEvent.wait()

        except Exception as e:
            print(f'An error Occurred: {str(e)}')

    def stopServer(self):
        print('stopping server')
        self.stopServerEvent.set()

