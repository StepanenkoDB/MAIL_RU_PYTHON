from random import randint
from time import sleep
from wsgiref.simple_server import make_server

def events(max_delay, limit):
	while True:
		delay = randint(1, max_delay)
		if delay >= limit:
			sleep(limit)
			yield None
		else:
			sleep(delay)
			yield 'Event generated, awaiting %d s' % delay

global_event = events(10,5)

class WSGI:
	def __init__(self, environ, start_response):
		self.environ = environ
		self.start = start_response

	def __iter__(self):
		for i in global_event:
			if i != None:
				status = '200 OK'
				response_headers = [('Content-type', 'text/plain')]
				self.start(status, response_headers)
				yield i
			else:
				status = '404 No Content'
				response_headers = [('Content-type', 'text/plain')]
				self.start(status, response_headers)
				yield "Failure\n"


if __name__ == '__main__':
	httpd = make_server('', 8000, WSGI)
	print "Serving on port 8000..."
	httpd.serve_forever()