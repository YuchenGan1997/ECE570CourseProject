import pika, json
from main import Product, db

params = pika.URLParameters('your RabbitMQ URL')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        image = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(image)
        db.session.commit()
        print('Image Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.filter_by(id=data['id']).first()
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Image Updated')

    elif properties.content_type == 'product_deleted':
        # product = Product.query.get(data)
        product = Product.query.filter_by(id=data).first()
        db.session.delete(product)
        db.session.commit()
        print('Image Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
