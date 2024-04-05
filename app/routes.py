from flask import render_template, request
from datetime import datetime
import json
from __main__ import webapp, devices
from .mqtt import publish_mqtt

@webapp.route("/device/update", methods=["POST"])
def deviceUpdate():
    print(request.get_json(force=True))
    newDevice = request.json
    if newDevice["mac"] not in devices.keys():
        devices[newDevice["mac"]] = {}

    devices[newDevice["mac"]]["mac"] = newDevice["mac"]
    devices[newDevice["mac"]]["time"] = (int)(datetime.now().timestamp())
    devices[newDevice["mac"]]["ip"] = newDevice["ip"]
    devices[newDevice["mac"]]["status"] = newDevice["status"]
    publish_mqtt(f"{newDevice['mac']}/status", json.dumps(newDevice["status"]),retain=True)
    return [newDevice]

@webapp.route("/cmd/ack", methods=["POST"])
def deviceCMDAck():
    data = request.get_json(force=True)
    print(data)
    print('CMD ACK')
    publish_mqtt(f"{data['mac']}/cmd/ack", json.dumps(dict({"msg_id":data["msg_id"]})))
    return 'ok'
  

@webapp.route("/devices")
def devicesApp():
    return devices


@webapp.route("/")
def home():
    return render_template("home.html", devices=devices)
