import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    pass


def on_message(mqttc, obj, msg):
    print('message!!!')
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    pass


def on_log(mqttc, obj, level, string):
    pass


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("paho/test/single", 0)

mqttc.loop_forever()