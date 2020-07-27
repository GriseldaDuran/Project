#Weather.py
#Draft


import requests

def weather(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b8aaa2e74c5e9ba9f1cf5b4e060789dc&units=metric');
	return res.json();


''' Function: print_weather
This function just prints the forecast
Parameters
----------
result : JSON
   Gets the Json response from api.
city : TEXT or INT
    Gets the city name or the zip code.

Returns
-------
None.

'''

def print_weather(weatherdata,city):
	print("{}'s temperature: {}°F ".format(city,(weatherdata['main']['temp']*(9/5)+32)))
	print("Details: {}".format(weatherdata['weather'][0]['description']))
	print("Weather: {}".format(weatherdata['weather'][0]['main']))


''' Function: main
    Returns
    -------
    None.
'''

def main():
	city=input('Enter the name of the city:')
	print()
	try:
	  qparam='q='+city;
	  wresp=weather(qparam);
	  print_weather(wresp, city)
	except:
	  print('City name not found...')
      
if __name__=='__main__':
    while True:
        main()
