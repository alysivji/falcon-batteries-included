class SQLAlchemySessionManager:
    """Create scoped session for each request and close it before response."""

    def __init__(self, db):
        self.db = db

    def process_request(self, req, resp):
        req.db = self.db

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(req, "db"):
            delattr(req, "db")
