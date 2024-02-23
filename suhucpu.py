#!/usr/bin/python

# IoT project monitor suhu CPU Raspberry PI Zero W
# Hantar data ke ThingSpeak.com serta bina graf untuk tujuan pemantauan
# graf data ini boleh dilihat di:

# https://thingspeak.com/channels/2433847

# Ditulis oleh 9W2KEY OJ15dx
# Pada 24 Feb, 2024 (12:07am)

from time import sleep
import http.client
import urllib.request, urllib.parse, urllib.error
import time


key = "Bubuh API Key demo sini"  # Put your API Key here
def thermometer():


    while True:
#Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 
# Get Raspberry Pi CPU temp
        params = urllib.parse.urlencode({'field1': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":

        while True:

                thermometer();
                time.sleep(180); # Tunggu 3 minit
