from client import MQTTReviever
from publisher import publish_message


def send_message():
    message_sent = publish_message()
    return message_sent


c = MQTTReviever()
c.start()
send_message()
while c.captured_message != 'default':
    pass
c.stop()

assert c.captured_message == ''
