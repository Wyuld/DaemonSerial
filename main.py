import serial
import json
import requests

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:
    value_in_bytes = ser.readlines()
    
    # Verificar se a lista não está vazia antes de imprimir
    if value_in_bytes:
            value_bytes_complete = b''.join(value_in_bytes)
            value_string = value_bytes_complete.decode('utf-8').strip()
            value_json = json.loads(value_string)
            value_json = json.dumps(value_json)
            headers = {'Content-Type': 'application/json'}
            r = requests.post('https://cpd-monitoring.vercel.app/dados', data=value_json, headers=headers)
            print(r.text)
            #print(value_json)
d