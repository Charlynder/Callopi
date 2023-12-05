from flask import Flask, render_template
import threading

app = Flask(__name__)

class CServer:
    def __init__(self, app):
        self.app = app
        self.stopServerEvent = threading.Event()

    def server(self):
        try:
            PORT = 8080
            self.app.run(port=PORT, debug=True, use_reloader=False)

            # wait for server to be stopped
            self.stopServerEvent.wait()

        except Exception as e:
            print(f'An error occurred: {str(e)}')

    def stopServer(self):
        print('Stopping server')
        self.stopServerEvent.set()

# Instantiate the Flask app
cserver = CServer(app)

# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# You can define more routes and handlers as needed

if __name__ == '__main__':
    # Start the server in a separate thread
    server_thread = threading.Thread(target=cserver.server)
    server_thread.daemon = True
    server_thread.start()

    # Wait for user input to stop the server
    input("Press Enter to stop the server...")

    # Stop the server when the user presses Enter
    cserver.stopServer()
