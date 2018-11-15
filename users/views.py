
from django.shortcuts import render
import requests
import datetime

def home(request):
    url = 'https://us-central1-prueba-resuelve.cloudfunctions.net/users/2017-01-01/2017-04-01'
    response = requests.get(url)
    data = response.json()


    context = {
        'nombre' : data[0]['nombre'],
        'apellido' : data[0]['apellido'],
        'segundo_nombre' : data[0]['segundo_nombre'],
        'segundo_apellido' : data[0]['segundo_apellido'],
        'uid' : data[0]['uid'],
        'email' : data[0]['email'],
        'active' : data[0]['active'],
        'created_at' : data[0]['created_at']
    }


    # for d in data:
    #     context = {}
    #     for k,v in d.items():
    #         context[k]=v
            #print(k,':',v)

    template_name = 'home_users.html'
    return render(request, template_name, context)
