import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://uewsjhwd:AFwHr-3HhnrFk8a71Szv4EdPdDBCmLzV@chinook.rmq.cloudamqp.com/uewsjhwd?heartbeat=800')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
