import os

OUTBOUND_EMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS", None)
OUTBOUND_EMAIL_PASSWORD = os.getenv("GMAIL_APPLICATION_PASSWORD", None)

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://sivdev_user:sivdev_pass@db:5432/sivdev"
)
REDIS_URI = os.getenv("REDIS_URL", "redis://redis:6379")

SECRET_KEY = os.getenv("SECRET_KEY", "shhhh! it's a secret")
