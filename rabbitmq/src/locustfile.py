from rabbitmq import get_client

from locust import Locust, TaskSet, task, events

class RabbitTaskSet(TaskSet):
    @task
    def publish(self):
        get_client().publish()

class MyLocust(Locust):
    task_set = RabbitTaskSet
    min_wait = 1000
    max_wait = 1000

def on_locust_stop_hatching():
    get_client().disconnect()

events.locust_stop_hatching += on_locust_stop_hatching
