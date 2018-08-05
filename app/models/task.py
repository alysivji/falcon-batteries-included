import redis
import rq

from .. import db, redis_conn
from . import BaseModel


class Task(BaseModel):
    """Task Information Table"""

    def __repr__(self):
        return f"<Task: {self.user.email}-{self.name}>"

    # Attributes
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", name="fk_task_user_id"))
    complete = db.Column(db.Boolean, default=False)

    # Relationships
    user = db.relationship("User", back_populates="tasks")

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=redis_conn)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get("progress", 0) if job is not None else 100
