class HealthCheckResource:
    def on_get(self, req, resp):
        resp.media = {"service": "healthy"}
