import time

from rq import Queue
import redis
from somewhere import count_words_at_url

redis_conn = redis.StrictRedis(host='redis', port=6379, db=0)

q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(count_words_at_url, 'http://cnn.com')
print(job.result)   # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)   # => 889
