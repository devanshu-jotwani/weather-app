from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=4942f9e86977f6f0b112ac94d8103f23&units=metric&q='

    try:
        city = (request.POST)['c1']#textfield empty(multikeydicterror)
        url=url+city

        r = requests.get(url).json()

        context={'city_weather' : {
                                'flag' : True,
                                'city' : r["name"],#baburao(NameError exception)
                                'temperature' : r["main"]["temp"],
                                'humidity' : r["main"]["humidity"],
                                'description' :r["weather"][0]["description"]
                                            }
                    }
        return render(request , 'weather/home.html', context)
    except Exception:
        context={'city_weather' : {'flag' : False}}
        return render(request , 'weather/home.html', context)
