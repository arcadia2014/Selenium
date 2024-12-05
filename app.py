from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

#@app.route("/")
#def hello_world():
    #return"<p>hello. world</p>"

browser = webdriver.Edge()
browser.get('https://www.bing.com/')
#rowser'Chrome' in browser.title

try:
    elem = browser.find_element(By.NAME, 'q')
    elem.send_keys('sopa instantanea' + Keys.RETURN)
except Exception as e:
    print(f"Error al interactuar con el elemento:" + {e})


