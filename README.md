
# Kafka

## Quick Start

1. Docker Compose로 Kafka와 Kafka UI를 실행하고, 프로듀서/컨슈머 파일 실행을 위해 kafka-python를 설치합니다. 

```
docker-compose up -d
pip install -r requirements.txt
```

2. Kafka 프로듀서를 실행하여 메시지를 전송합니다.

```
python producer.py
```

3. Kafka 컨슈머를 실행하여 메시지를 수신합니다.

```
python consumer.py
```

4. 브라우저에서 Kafka UI에 접속하여 메시지를 확인합니다.

```
http://localhost:8080
```

## Other Examples

- 다중 프로듀서/컨슈머 예제를 `multi_producer.py`, `multi_consumer.py` 파일에서 확인하실 수 있습니다.
