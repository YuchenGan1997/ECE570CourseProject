import pika, json

params = pika.URLParameters('amqps://zbocvraw:yiZaSUmYzsb4Ys1Dv2CyueForb2jujR8@moose.rmq.cloudamqp.com/zbocvraw')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
