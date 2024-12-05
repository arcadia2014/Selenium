from flask import Flask
import unittest
from selenium import webdriver

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)