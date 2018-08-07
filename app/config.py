import os

IN_PRODUCTION = os.getenv("ENV_NAME", False)
SECRET_KEY = os.getenv("SECRET_KEY", "shhhh! it's a secret")

# infrastructure
local_db = "postgresql://sivdev_user:sivdev_pass@db:5432/sivdev"
DATABASE_URI = os.getenv("DATABASE_URI", local_db)
ELASTICSEARCH_URI = os.getenv("ELASTICSEARCH_URI", None)
REDIS_URI = os.getenv("REDIS_URL", "redis://redis:6379")

# email service
OUTBOUND_EMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS", None)
OUTBOUND_EMAIL_PASSWORD = os.getenv("GMAIL_APPLICATION_PASSWORD", None)

# internal configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(name)s:%(lineno)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {"local": {"class": "logging.StreamHandler", "formatter": "standard"}},
    "loggers": {
        "app": {"handlers": ["local"], "level": "INFO" if IN_PRODUCTION else "DEBUG"}
    },
}
