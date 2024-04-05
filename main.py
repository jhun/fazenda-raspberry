from flask import Flask, request, jsonify
from flask_mqtt import Mqtt
import ssl

webapp = Flask(__name__, template_folder="app/template")


webapp.config["MQTT_BROKER_URL"] = "54.94.223.169"
webapp.config["MQTT_BROKER_PORT"] = 8368
webapp.config["MQTT_USERNAME"] = "iot_esp_user23"
webapp.config["MQTT_PASSWORD"] = "TempPassword23@12"
webapp.config["MQTT_TLS_ENABLED"] = True

webapp.config["MQTT_TLS_INSECURE"] = True
webapp.config["MQTT_TLS_CA_CERTS"] = None
webapp.config["MQTT_TLS_CERTFILE"] = None
webapp.config["MQTT_TLS_KEYFILE"] = None
webapp.config["MQTT_TLS_CERT_REQS"] = ssl.CERT_NONE
webapp.config["MQTT_TLS_VERSION"] = None
webapp.config["MQTT_TLS_CIPHERS"] = None

topic = "/flask/mqtt"

mqtt_client = Mqtt(webapp,connect_async=True)

devices = dict()

import app.routes
import app.mqtt
import app.device



if __name__ == "__main__":
    webapp.run(debug=True, host="0.0.0.0", port="80")
