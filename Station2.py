#!/usr/bin/env python

# This script works as a Environmental Station, so it will compute (random) values
# through its virtual sensor and it will publish the message composed by the values
# calculated before on the MQTT channel, as long as the station works correctly.

# importing libraries
import paho.mqtt.client as mqtt
import os
import socket
import ssl
from time import sleep
from random import randint
import json
import datetime

def get_data():


    def on_connect(client, userdata, flags, rc):  # function for making connection between
        global connflag  # the MQTT client and the broker
        print("Connected to AWS")
        connflag = True
        print("Connection returned result: " + str(rc))

    def on_message(client, userdata, msg):  # function for ending messages
        print(msg.topic + " " + str(msg.payload))

    # def on_log(client, userdata, level, buf):
    #    print(msg.topic+" "+str(msg.payload))

    awshost = "a1cxcuxmsxl8ng-ats.iot.us-east-2.amazonaws.com"  # endpoint
    awsport = 8883  # port no.
    clientId = "RaspberryPi"  # Update this line with your desired client ID
    # thingName = "sensor"  # thing name
    caPath = "./AmazonRootCA1.pem"  # rootCA certificate
    certPath = "./870cd848ac36b0774d1f22c5e0c146ede55f5b47a29e754b56dbbb80a38410a7-certificate.pem.crt"  # client certificate
    keyPath = "./870cd848ac36b0774d1f22c5e0c146ede55f5b47a29e754b56dbbb80a38410a7-private.pem.key"  # private key

    mqttc = mqtt.Client(client_id=clientId)  # MQTT client object
    mqttc.on_connect = on_connect  # assign on_connect function
    mqttc.on_message = on_message  # assign on_message function
    # mqttc.on_log = on_log

    mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED,
                  tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters

    mqttc.connect(awshost, awsport, keepalive=60)  # Update the client_id parameter with the desired client ID
    # connect to AWS server

    mqttc.loop_start()  # start the loop for sending
    # messages continuously
    i = 0
    final_data = []
    while (i < 1):
        i = i + 1
        sleep(5)  # waiting between messages
        temp = str(randint(-50, 50))  # computation of all the (random) values
        hum = str(randint(0, 100))  # of the sensors, for this
        co2 = str(randint(300, 2000))
        rain = str(randint(0, 50))
        wind_dir = str(randint(0, 360))  # specific station (with id 1)
        wind_int = str(randint(0, 100))
        time = str(datetime.datetime.now())[:19]  # computation of the current date and time

        data = {"id": "2", "datetime": time, "temperature": temp, "humidity": hum, "CO2 Sensor": co2,
                "windDirection": wind_dir, "windIntensity": wind_int, "rainHeight": rain}
        jsonData = json.dumps(data)
        final_data.append(jsonData)
        mqttc.publish("sensor/data", jsonData, 1)  # publish this message on the

    return final_data