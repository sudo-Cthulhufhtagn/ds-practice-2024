import locust

json_req = {
   "user":{
      "name":"fgbhf",
      "contact":"hgnfh"
   },
   "creditCard":{
      "number":"1111222233334444",
      "expirationDate":"05/21",
      "cvv":"633"
   },
   "userComment":"",
   "items":[
      {
         "name":"JavaScript - The Good Parts",
         "quantity":1,
         "total":3,
         "author":"Jane Doe"
      }
   ],
   "discountCode":"",
   "shippingMethod":"",
   "giftMessage":"",
   "billingAddress":{
      "street":"Long Street 457",
      "city":"Tallinn",
      "state":"f",
      "zip":"911AM",
      "country":"Estonia"
   },
   "giftWrapping":False,
   "termsAndConditionsAccepted":True,
   "notificationPreferences":[
      "email"
   ],
   "device":{
      "type":"Smartphone",
      "model":"Samsung Galaxy S10",
      "os":"Android 10.0.0"
   },
   "browser":{
      "name":"Chrome",
      "version":"85.0.4183.127"
   },
   "appVersion":"3.0.0",
   "screenResolution":"1440x3040",
   "referrer":"https://www.google.com",
   "deviceLanguage":"en-US"
}

class MyUser(locust.HttpUser):
   host = "http://localhost:8081"
   
   @locust.task
   def my_task(self):
      headers = {"Content-Type": "application/json"}
      self.client.post("/checkout", json=json_req, headers=headers)