from kafka import KafkaConsumer
import json
import time

consumers = {
    "topic1": KafkaConsumer(
        "topic1",
        bootstrap_servers="localhost:29092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    ),
    "topic2": KafkaConsumer(
        "topic2",
        bootstrap_servers="localhost:29092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    ),
}


def consume_messages(max_empty_polls=5):
    # Keep track of how many times we poll without receiving any messages
    empty_poll_count = 0

    while empty_poll_count < max_empty_polls:
        has_message = False
        for topic, consumer in consumers.items():
            # Poll for messages for each topic
            messages = consumer.poll(timeout_ms=1000)
            if messages:
                has_message = True  # We received at least one message, reset empty poll count
                for partition, records in messages.items():
                    for record in records:
                        print(f"Received from {topic}: {record.value}")

        if has_message:
            empty_poll_count = 0  # Reset the empty poll counter if we got messages
        else:
            empty_poll_count += 1  # Increment if no messages received

        time.sleep(1)  # Add a short delay between polls

    print("No new messages, exiting.")


if __name__ == "__main__":
    consume_messages()
