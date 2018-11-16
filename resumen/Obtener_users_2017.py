
import requests
import json

# Meses del año se define de 1 a 12 Meses.
_meses = range(1,13)
# Dias del Mes se define del dia 1 al dia 31 para cubrir todos los dias.
_dias = range(1,32)
# Año del cual se extraeran los usuarios.
_año = 2017

#-----Pruebas de tipo de datos
#print(type(_año))
#print(type(_meses),type(_dias))

# Se cicla para poder realizar las combinaciones de todo el año.
for m in _meses:
    for d in _dias:
        #Cachamos el erro por si no encuentra alguna fecha con los parametrso realizados
        try:

            url = f'https://us-central1-prueba-resuelve.cloudfunctions.net/users/{_año}-1-1/{_año}-{m}-{d}/'
            response = requests.get(url)
            request_text = response.text
            data = json.loads(request_text)
            data_serialized = json.dumps(data, indent = 4)
            print(data_serialized)


        except ValueError:
            print('Ops!. Algo fallo en las fechas buscadas...')
