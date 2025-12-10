import unittest
import json
import requests

url = "http://127.0.0.1:8000"

class AppTests(unittest.TestCase):

	def test_get_hello_endpoint(self):
		r = requests.get(url+'/hello')
		self.assertEqual(json.loads(r.text)['message'], 'Hello world!')
		
	def test_post_hello_endpoint(self):
		r = requests.get(url+'/hello')
		self.assertEqual(r.status_code, 200)
		
if __name__ == '__main__':
    unittest.main()