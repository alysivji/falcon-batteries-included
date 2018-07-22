import os

DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://sivdev_user:sivdev_pass@db:5432/sivdev")
