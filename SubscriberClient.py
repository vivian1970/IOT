
#!/usr/bin/env python

# This script works as a Subscriber Client, so it will be subscribed
# to a topic, it will receive all the messages on that topic and
# eventually displays every message on a website.

# importing libraries
import paho.mqtt.client as mqtt
import os
import socket
import ssl
from flask import Flask, render_template  # import Flask for web server and render_template for rendering HTML templates
import json
from Station2 import get_data

data = get_data()
final_data = data
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', data=final_data)




if __name__ == '__main__':
    app.run(debug=True)

