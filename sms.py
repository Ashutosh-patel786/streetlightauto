import conf, json, time
from boltiot import Sms, Bolt
import json, time

minimum_limit = 80 #can be change
maximum_limit1 = 300 #can be change
maximum_limit2 = 350

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if maximum_limit1 <sensor_value > maximum_limit2 :
            response = sms.send_sms("Hi there Turn OFF the Street Light of your area")
        elif sensor_value < minimum_limit:
            response = sms.send_sms("Hi there Turn ON the Street Lights of your area")
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(900) #after 15 min again read the data
