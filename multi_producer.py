from kafka import KafkaProducer
import json
import time

producers = {
    'topic1': KafkaProducer(bootstrap_servers='localhost:29092', value_serializer=lambda v: json.dumps(v).encode('utf-8')),
    'topic2': KafkaProducer(bootstrap_servers='localhost:29092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
}

def send_messages():
    for i in range(10):
        message_topic1 = {'message': f'Topic1 message {i}'}
        message_topic2 = {'message': f'Topic2 message {i}'}
        producers['topic1'].send('topic1', message_topic1)
        producers['topic2'].send('topic2', message_topic2)
        print(f'Sent to topic1: {message_topic1}, Sent to topic2: {message_topic2}')
        time.sleep(1)

if __name__ == "__main__":
    send_messages()
    for producer in producers.values():
        producer.flush()
