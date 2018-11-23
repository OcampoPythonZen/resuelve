#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
#>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})
total_de_movimientos = 69999.99
suma_del_credito = 99999.99
suma_del_debito = 88868.00
resultado_credito_menos_debito = 35342523.99
nombre_del_usuario = 'Edgar'
uid_del_usuario = 'e345234-45345f3-534534'
total_de_movimientos_del_usuario = 22
suma_del_credit_de_este_usuario = 10000
suma_del_debit_de_este_usuario = 7000
resultado_credito_menos_debito_usuario = 3000

data = {
    'totalRecords' : total_de_movimientos,
    'totalCredit' : suma_del_credito,
    'totalDebit' : suma_del_debito,
    'balance' : resultado_credito_menos_debito,
    'byUser' : [ #Aqui van todos los registros de los empleados...
        {
            'name' : nombre_del_usuario,
            'uid' : uid_del_usuario,
            'records' : total_de_movimientos_del_usuario,
            'resumen' : {
                'credit' : suma_del_credit_de_este_usuario,
                'debit' : suma_del_debit_de_este_usuario,
                'balance' : resultado_credito_menos_debito_usuario,
            }
        }
    ]
 }

print(type(data))
print(json.dumps(data, indent = 4))
#How to acces the balance key
#print(json.dumps(data['byUser'][0]['resumen']['balance'], indent = 4))

url = 'https://us-central1-prueba-resuelve.cloudfunctions.net/conta/resumen'
response = requests.put(url, data = json.dumps(data))
