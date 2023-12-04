import unittest
import time
from io import StringIO
from contextlib import redirect_stdout
import threading

# Import the CServer class from your code
from bin.server import CServer  # Replace 'your_module_name' with the actual name of your module

class TestCServer(unittest.TestCase):
    def test_server(self):
        c_server = CServer()

        # Capture the printed output
        with StringIO() as output_buffer, redirect_stdout(output_buffer):
            c_server_thread = threading.Thread(target=c_server.server)
            c_server_thread.start()
            # Sleep for a few seconds to allow the server to run
            time.sleep(3)

            # Stop the server
            c_server.stopServer()
            c_server_thread.join()

            # Check if the server started and stopped without errors
            output = output_buffer.getvalue()
            self.assertIn("Serving at http://localhost:8080", output)
            self.assertIn("stopping server", output)

if __name__ == '__main__':
    unittest.main()
