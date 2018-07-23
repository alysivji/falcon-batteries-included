class HealthCheckResource:
    def on_get(self, req, resp):
        auth = {"auth_disabled": True}
        resp.media = {"service": "healthy"}
