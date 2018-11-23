#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

            url = f'https://us-central1-prueba-resuelve.cloudfunctions.net/users/{_año}-{str(m).zfill(2)}-{str(d).zfill(2)}/{_año}-{str(m).zfill(2)}-{str(d).zfill(2)}/'
            response = requests.get(url)
            request_text = response.text
            data = json.loads(request_text)
            data_serialized = json.dumps(data, indent = 4)
            print(data_serialized)

            # {
            #     "nombre": "Frances",
            #     "apellido": "Eichmann",
            #     "segundo_nombre": "",
            #     "segundo_apellido": "Stark",
            #     "uid": "812eea02-e741-4b01-9ff6-763d510db524", -- buscar la relacion para sacar la suma de sus movimientos
            #     "email": "Pasquale44@hotmail.com",
            #     "active": false,
            #     "created_at": "2017-01-04T13:42:53.778Z"
            # }


        except ValueError:
            print('Ups!. Algo fallo en las fechas buscadas...')
