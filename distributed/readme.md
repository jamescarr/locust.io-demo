# Distributed Example
This example takes the quickstart example and makes it distributed. When
`docker-compose up -d` is ran only the target and the locust master will
come up, the slave will die right away (because by the time it tries to
come up, master is not available).

If we wanted to run 4 locust minions to distribute tasks amongst we'd
run `docker-compose scale minion=4` to launch 4 containers. If we log
into the locust interface at http://dockerhost:8089 we should see 4
slaves connected.

## Things of Note
* Requests per second will be distributed amongst the available slaves.
  So for example if you're aiming for 10 req/s and 5 slaves, each slave
will run 2 req/s.

