
from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier
n=ToastNotifier()

def main(url):
    r=requests.get(url)
    return r.text

result=main("https://weather.com/en-IN/weather/today/l/a5f0fe2ff9a40acc9ce62d67cd99439a71cde78cc0c5c1fbf6da052bef4cdba9")

beautiful=BeautifulSoup(result,"html.parser")

#print(beautiful.prettify())

current_temp = soup.find_all("id", class_="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034") 
chances_rain = soup.find_all("div", class_= "CurrentConditions--CurrentConditions--1XEyg") 

temp = (str(current_temp)) 
temp_rain = str(chances_rain) 

result = "current_temp " + temp[128:-9] + " in patna bihar" + "\n" +temp_rain[131:-14] 

n.show_toast("Weather update", result, duration = 10)

