class SQLAlchemySessionManager:
    """
    Create scoped session for every request and close it when request ends.

    Adapted from
    https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/
    """

    def __init__(self, db):
        self.db = db

    def process_resource(self, req, resp, resource, params):
        resource.db = self.db

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, "db"):
            delattr(resource, "db")
