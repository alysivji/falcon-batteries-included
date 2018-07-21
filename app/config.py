import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sivdev_user:sivdev_pass@db:5432/sivdev")
