from __main__ import mqtt_client, devices
from .device import send_to_device


def publish_mqtt(topic, data,retain = False):
    mqtt_client.publish(topic, payload=data, qos=1, retain=retain)

def parseTopic(topic):
    str_split = topic.split("/")
    return dict(mac=str_split[0], topic=str_split[1])


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        mqtt_client.subscribe("+/cmd")
    else:
        print("Bad connection. Code:", rc)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(topic=message.topic, payload=message.payload.decode())
    parsed = parseTopic(message.topic)
    mac = parsed["mac"]
    topic = parsed["topic"]
    print("Received message on topic: {topic} with payload: {payload}".format(**data))
    send_to_device(mac, topic, message.payload.decode())
    print("TESTE,{mac}, {topic}".format(**parsed))


