class SQLAlchemySessionManager:
    """Create scoped session for each request and close it before response."""

    def __init__(self, db):
        self.db = db

    def process_request(self, req, resp):
        req.context["db"] = self.db

    def process_response(self, req, resp, resource, req_succeeded):
        if "db" in req.context:
            db = req.context.pop("db")
        db.session.remove()
