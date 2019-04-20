import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request
    messagetosend = bytes('Hello World!',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    request = self.requestline
    request = request[5 : int(len(request)-9)]
    print(request)
    if request == 'on':
      GPIO.output(2,True)
    else:
      GPIO.output(2,False)
    return


server_address_httpd = ('127.0.0.1',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting Server:')
httpd.serve_forever()
GPIO.cleanup()

#Code By Christos 'MrMaRc0s' Markos
