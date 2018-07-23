import falcon


class HTTPError(falcon.HTTPError):
    """HTTPError that stores a dictionary of validation error messages."""

    def __init__(self, status, errors=None, *args, **kwargs):
        self.errors = errors
        super().__init__(status, *args, **kwargs)

    def to_dict(self, *args, **kwargs):
        """
        Override `falcon.HTTPError` to include error messages in responses.
        """

        response_body = super().to_dict(*args, **kwargs)

        if self.errors is not None:
            response_body["errors"] = self.errors

        return response_body
