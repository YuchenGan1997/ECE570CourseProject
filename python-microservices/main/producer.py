import pika, json

params = pika.URLParameters('amqps://mvrcbrxu:LxlVQV2HYAv_HxaampDXlRYpyf1m7lV6@moose.rmq.cloudamqp.com/mvrcbrxu?heartbeat=800')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
