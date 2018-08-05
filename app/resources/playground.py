"""Debug hook to try things out"""

from __future__ import annotations
from datetime import datetime, timedelta
from time import sleep

from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler

import falcon

from app import redis_conn

scheduler = Scheduler(connection=redis_conn)


def task_to_run(sec_to_run: int) -> None:
    for i in range(sec_to_run):
        print(i)
        sleep(.5)
    return None


class PlaygroundResource:
    auth = {"auth_disabled": True}

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        # import pdb; pdb.set_trace()
        scheduler.enqueue_in(timedelta(seconds=10), task_to_run, 5)
        resp.media = {"service": "healthy"}
