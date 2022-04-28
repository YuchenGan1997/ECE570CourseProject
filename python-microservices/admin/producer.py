import pika, json

params = pika.URLParameters('amqps://uewsjhwd:AFwHr-3HhnrFk8a71Szv4EdPdDBCmLzV@chinook.rmq.cloudamqp.com/uewsjhwd?heartbeat=800')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
