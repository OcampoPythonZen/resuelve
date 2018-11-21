#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

# Meses del año se define de 1 a 12 Meses.
_meses = range(1,13)
# Dias del Mes se define del dia 1 al dia 31 para cubrir todos los dias.
_dias = range(1,32)
# Año del cual se extraeran los usuarios.
_año = 2018

#-----Pruebas de tipo de datos
#print(type(_año))
#print(type(_meses),type(_dias))

# Se cicla para poder realizar las combinaciones de todo el año.
for m in _meses:
    for d in _dias:
        #Cachamos el error por si no encuentra alguna fecha con los parametrso realizados
        try:

            url = f'https://us-central1-prueba-resuelve.cloudfunctions.net/movements/{_año}-{str(m).zfill(2)}-{str(d).zfill(2)}/{_año}-{str(m).zfill(2)}-{str(d).zfill(2)}/'
            response_m = requests.get(url)
            request_text_m = response_m.text
            data_m = json.loads(request_text_m)
            data_serialized_m = json.dumps(data_m, indent = 4)
            print(data_serialized_m)
            #Mostrara las listas vacias si no contiene nada ese dia []

        except ValueError:
            print('Ups!. Las fechas no son validas...')
