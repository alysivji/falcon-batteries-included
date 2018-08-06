"""Debug hook to try things out"""

from __future__ import annotations
import logging

from time import sleep

from rq_scheduler import Scheduler

import falcon

from app import redis_conn

scheduler = Scheduler(connection=redis_conn)


logger = logging.getLogger(__name__)


def task_to_run(sec_to_run: int) -> None:
    for i in range(sec_to_run):
        print(i)
        sleep(.5)
    return None


class PlaygroundResource:
    auth = {"auth_disabled": True}

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        # import pdb; pdb.set_trace()
        # scheduler.enqueue_in(timedelta(seconds=10), task_to_run, 5)
        my_dict = {"asbasdf": 23434, "asdf23": 1234}

        logger.warning("%s", "blahasdf")
        logger.critical("critical blah")

        resp.media = {"service": "healthy"}
