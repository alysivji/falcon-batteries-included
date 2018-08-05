from __future__ import annotations

import falcon


class HealthCheckResource:
    auth = {"auth_disabled": True}

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.media = {"service": "healthy"}
