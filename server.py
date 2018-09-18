from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		# Send response status code
		self.send_response(200)

		# Send headers
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send message back to client
		message = "Battleship Network Application!"

		# Write content as utf-8 data
		self.wfile.write(bytes(message, "utf8"))
		return

	# def do_POST(self):
		

def run(server_class=HTTPServer, handler_class=MyHandler, port=80):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()