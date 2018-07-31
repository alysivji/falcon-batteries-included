import os

import redis
from rq import Connection, Queue, Worker

# TODO add exceptions to do other stuff besides failed job queue
# http://python-rq.org/docs/exceptions/
# figure out logging


REDIS_URI = os.getenv("REDIS_URL", "redis://redis:6379")
redis_conn = redis.StrictRedis.from_url(REDIS_URI)

qs = [Queue(connection=redis_conn)]

with Connection(redis_conn):
    w = Worker(qs)
    w.work()
