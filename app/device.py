from __main__ import mqtt_client, devices
import json
import requests

def convert_bool_to_int(form_data):
    for key, value in form_data.items():
        if isinstance(value, bool):
            form_data[key] = int(value)
    return form_data

def send_to_device(mac, endpoint, data):
    print("SEND TO DEVICE")
    if mac in devices.keys():
        ip = devices[mac]["ip"]
        data = convert_bool_to_int(json.loads(data))
        response =  requests.post(f"http://{ip}/{endpoint}", data=data)
        print(response.text)
        print("SENDO TO IP" + f"http://{ip}/{endpoint}")
