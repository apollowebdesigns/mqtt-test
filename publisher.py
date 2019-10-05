import paho.mqtt.publish as publish

done = publish.single("paho/test/single", "boo")
print('done')
print(done)