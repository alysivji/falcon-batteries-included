FROM python:3.7.0-slim-stretch

LABEL maintainer="Aly Sivji <alysivji@gmail.com>" \
    description="Development image for batteries included Falcon project"

WORKDIR /app

COPY requirements.txt requirements_dev.txt /tmp/
COPY ./app /app

RUN groupadd -g 901 -r sivdev && \
    useradd -g sivdev -r -u 901 sivdev_user && \
    pip install --no-cache-dir -r /tmp/requirements_dev.txt

EXPOSE 7000

# Switch from root user for security
USER sivdev_user

CMD ["gunicorn", "app:api", "-b", "0.0.0.0:7000"]
