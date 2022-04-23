import pika, json

params = pika.URLParameters('amqps://ztegcipp:PrXdKG9BvBL9pUe91q5kVvxh-e1lMux-@shark.rmq.cloudamqp.com/ztegcipp')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
