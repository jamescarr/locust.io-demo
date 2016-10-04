from locust import HttpLocust, TaskSet, task, events
import logging
LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
                '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        # this is just using requests to post the auth details
        self.client.post("/login", {"username":"admin", "password":"admin"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profiles")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000



"""
Here we trap some events
"""
def request_failure(request_type, name, response_time, exception):
    LOGGER.info('request_failure fired!')

def request_success(request_type, name, response_time, response_length):
    LOGGER.info('request_success fired!')

def locust_start_hatching():
    LOGGER.info('locust_start_hatching fired!')

def locust_stop_hatching():
    LOGGER.info('locust_stop_hatching fired!')

def hatch_complete(user_count):
    LOGGER.info('hatch_complete fired!')

def quitting():
    LOGGER.info('quitting fired!')


events.locust_start_hatching += locust_start_hatching
events.locust_stop_hatching += locust_stop_hatching
events.hatch_complete += hatch_complete
events.quitting += quitting
events.request_success += request_success
events.request_failure += request_failure
