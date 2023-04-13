# IOT

In this assignment I created a cloud-based IoT system that collects information from a 
set of virtual environmental sensors using the MQTT protocol. I also created a simple website to display the data collected from the sensors.

Virtual Sensors

Using Python language programming I wrote a stand-alone program that represents virtual environmental stations that generate periodically a set of random values for 5 different sensors:

1. Temperature (Range: -50 to 50 Celsius)
2. Humidity (Range: 0 to 100%)
3. Co2 sensor (Range: 300ppm to 2000ppm
4. Rain height (Range: 0 to 50 mm / h)
5. Wind direction (Range: 0 to 360 degrees)
6. Wind intensity (Range: 0 to 100 m/s)
 
I have created 2 virtual stations that run and publish their values on the MQTT channel.

Cloud-based IoT Backend

The MQTT is controlled by the cloud-based backend implemented using AWS IoT.

Web-based Dashboard

Station 2 is displayed on the website 

I make a summary to explain the correct procedure for the system to work properly:

Open the scripts SubscriberClient.py, Station1.py, Station2.py, in the order of how I listed them and in three different terminals, with Python 3
Open the Dashboard with your favourite browser going into the repository, under the folder WebApp/web and open the file Dashboard.html
