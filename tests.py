import unittest
import json
import requests
import os
import signal
import uvicorn
from main import app

url = "http://127.0.0.1:8000"

class AppTests(unittest.TestCase):

	def test_get_hello_endpoint(self):
		r = requests.get(url+'/hello')
		self.assertEqual(json.loads(r.text)['message'], 'Hello world!')
		
	def test_post_hello_endpoint(self):
		r = requests.get(url+'/hello')
		self.assertEqual(r.status_code, 200)
	
	def test_stop_server(self):
		r = requests.get(url+'/stop')
		
if __name__ == '__main__':
	uvicorn.run(app, host="127.0.0.1", port=8000)
    unittest.main()
	pid = os.getpid()
    os.kill(pid, signal.SIGINT)