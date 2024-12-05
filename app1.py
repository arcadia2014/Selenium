from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

browser = webdriver.Chrome()

browser.get('https://www.bodegaaurrera.com.mx/search?q=sopa%20instantanea&typeahead=sopa')
assert 'Edge' in browser.title

try:
    elem = browser.find_element(By.NAME, 'q')
    elem.send_keys('sopa instantanea' + Keys.RETURN)
except Exception as e:
    print("Error{e}")
    

@app.route('/test')
def test():
    return 'test'
if __name__ == '__main__':
    app.run(debug=True)