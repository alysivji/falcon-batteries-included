from falcon import status_codes as status
from marshmallow import ValidationError

from app.exceptions import HTTPError


class SerializationMiddleware:
    """JSON <=> SQLAlchemy"""

    def process_resource(self, req, resp, resource, params):
        deserializer = resource.deserializers[req.method.lower()]
        if not deserializer:
            return

        try:
            result = deserializer.load(req.media)
        except ValidationError as err:
            raise HTTPError(status.HTTP_UNPROCESSABLE_ENTITY, err.messages)

        req.deserialized = result

    def process_response(self, req, resp, resource, req_succeeded):
        serializer = resource.serializers[req.method.lower()]
        if not serializer:
            return

        try:
            result = serializer.dump(resp._data)
        except ValidationError as err:
            raise HTTPError(status.HTTP_IM_A_TEAPOT)

        resp.media = result.data  # add this to the post dump
