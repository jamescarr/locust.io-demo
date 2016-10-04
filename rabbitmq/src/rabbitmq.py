from datetime import datetime
import logging
import multiprocessing
import os
import threading

from locust import events
import pika
from pika.exceptions import AMQPError


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
                '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


class RabbitMQClient(object):
    _connected = False

    def __init__(self):
        self._process_name = multiprocessing.current_process().name
        self._thread_name = threading.current_thread().name

    def connect(self):
        params = pika.URLParameters(os.environ['RABBITMQ_CONNECTION'])
        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._connected = True


    def publish(self):
        """
        Constructs and publishes a simple message
        via amqp.basic_publish

        """
        if not self._connected:
            self.connect()

        message = "Process: {}, Thread: {}".format(self._process_name,
                                                   self._thread_name)

        try:
            watch = StopWatch()
            watch.start()
            self._channel.basic_publish('test.exchange', 'test.message', message)
            watch.stop()
        except AMQPError as e:
            watch.stop()
            events.request_failure.fire(
                    request_type="BASIC_PUBLISH",
                    name="test.message",
                    response_time=watch.elapsed_time(),
                    exception=e,
                )
        else:
            events.request_success.fire(
                    request_type="BASIC_PUBLISH",
                    name="test.message",
                    response_time=watch.elapsed_time(),
                    response_length=0
                )

    def close_channel(self):
        if self._channel is not None:
            LOGGER.info('Closing the channel')
            self._channel.close()

    def close_connection(self):
        if self._connection is not None:
            LOGGER.info('Closing connection')
            self._connection.close()

    def disconnect(self):
        self.close_channel()
        self.close_connection()
        self._connected = False


class StopWatch():
    def start(self):
        self._start = datetime.now()

    def stop(self):
        self._end = datetime.now()

    def elapsed_time(self):
        timedelta = self._end - self._start
        return timedelta.total_seconds() * 1000

client = None
def get_client():
    global client
    if client is None:
        client = RabbitMQClient()
    return client
