import datetime 
import time 
import requests 
from plyer import notification 

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    
    print("Please! Check your internet connection")
    
if (covidData != None):
    
    data = covidData.json()['Success']
    
   
    while(True):
        notification.notify(
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  
            
            
            app_icon = "Paomedia-Small-N-Flat-Bell.ico",
            
            timeout  = 50
        )
       
        time.sleep(60*60*6)