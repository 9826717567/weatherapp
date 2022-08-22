from django.shortcuts import render
import requests

def Homepage(request):
    context = {}
    try:
        city = request.GET.get('city')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=20e0d92af760d7a2741d653228da60a7"
        data = requests.get(url).json()
        payload = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'kelvin_temperature': data['main']['temp'],
            'celcius_temperature': data['main']['temp'] - 273,
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity']
        }
        print(data)
        context = {'data': payload}
    except:
        context.setdefault('msg', 'Invalid input')
        return render(request,'weather/homepage.html',context)
    return render(request, 'weather/homepage.html', context)
    
# Create your views here.
