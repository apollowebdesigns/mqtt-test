import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self):
        self.mqttc = mqtt.Client()
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        self.mqttc.connect("localhost", 1883, 60)
        self.mqttc.subscribe("paho/test/single", 0)

    def on_connect(self, mqttc, obj, flags, rc):
        pass


    def on_message(self, mqttc, obj, msg):
        pass


    def on_publish(self, mqttc, obj, mid):
        pass


    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        pass


    def on_log(self, mqttc, obj, level, string):
        pass

    def start(self):
        self.mqttc.loop_start()

    def stop(self):
        self.mqttc.loop_stop()


class MQTTReviever(MQTTClient):
    received = False
    captured_message = 'default'

    def __init__(self):
        super().__init__()

    def on_message(self, mqttc, obj, msg):
        self.captured_message = msg.topic + " " + str(msg.qos) + " " + str(msg.payload)
        # mqttc.disconnect()
        return self.captured_message

