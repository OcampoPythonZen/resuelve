from django.shortcuts import render
import requests

def home(request):
    url = 'https://us-central1-prueba-resuelve.cloudfunctions.net/movements/2018-01-01/2018-01-10'
    response = requests.get(url)
    data = response.json()


    context = {
        'uid' : data[0]['uid'],
        'account' : data[0]['account'],
        'amount' : data[0]['amount'],
        'type' : data[0]['type'],
        'description' : data[0]['description'],
        'created_at' : data[0]['created_at']
    }


    # for d in data:
    #     context = {}
    #     for k,v in d.items():
    #         context[k]=v
            #print(k,':',v)

    template_name = 'home_movements.html'
    return render(request, template_name, context)
