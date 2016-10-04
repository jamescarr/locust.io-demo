# Locust.IO Demos
This project has a few demos of how to use locust.io to load test
various services. Given as part of a presentation on locust.io!

<script async class="speakerdeck-embed" data-id="ba3c5801b7f24e16a82a0837974a05d7" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>


* `quickstart` - The locust.io quickstart tutorial that logs in and load
  tests pages on a grafana installation
* `distributed` - the same thing as Quickstart but done with multiple
  workers
* `Events` - A quick tour of events
* Graphing - An example of using events to tap response times in
  influxdb + grafana
* `RabbitMQ` - A final demo of using locust.io to load test something
  non-web based... by blasting AMQP packets to a rabbitMQ host


## Running the Samples
All of these samples run locally using docker-compose. Simply switch to
the demo directory, type `docker-compose up -d`.

### URLs

* http://dockerhost:8086 - Locust.io dashboard
* http://dockerhost:3000 - grafana installation, login is admin/admin
* http://dockerhost:15672 - rabbitmq installation, login is guest/guest
