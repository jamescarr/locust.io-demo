from locust import HttpLocust, TaskSet, task, events
import logging
from reporter import Reporter

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
                '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        # this is just using requests to post the auth details
        self.client.post("/login", {"username":"admin", "password":"admin"})

    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000



"""
Here we trap some events
"""
reporter = Reporter()
events.request_success += reporter.request_success
events.hatch_complete += reporter.hatch_complete
