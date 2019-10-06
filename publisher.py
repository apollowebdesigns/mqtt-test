import paho.mqtt.publish as publish


def publish_message():
    message = "boo"
    done = publish.single("paho/test/single", "boo")
    return message
