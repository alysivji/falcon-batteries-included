import redis
from rq import Connection, Queue, Worker

# TODO add exceptions to do other stuff besides failed job queue
# http://python-rq.org/docs/exceptions/
# figure out logging

redis_conn = redis.StrictRedis(host="redis", port=6379, db=0)

qs = [Queue(connection=redis_conn)]

with Connection(redis_conn):
    w = Worker(qs)
    w.work()
