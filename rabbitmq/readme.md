# Load Testing RabbitMQ with Locust
This directory contains a demo of using locust to load test rabbitmq. It
uses a custom runner that blasts `basic_publish` calls to rabbitmq.

## Running It
1. `docker-compose up -d`
2. navigate to `http://dockerhost:15672` and login with `guest`/`guest`
3. Create an exchange named `test.exchange` and bind a queue to it.
4. Navigate to `http://dockerhost:8089` and launch a swarm
5. In the rabbitmq management panel, watch the publish rates hit the
   ceiling!

