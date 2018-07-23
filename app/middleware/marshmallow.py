import falcon
from marshmallow import ValidationError

from app.exceptions import HTTPError


class SerializationMiddleware:
    """JSON <=> SQLAlchemy"""

    def process_resource(self, req, resp, resource, params):
        deserialization_required = (hasattr(resource, "deserializers")
                                    and req.method.lower() in resource.deserializers)
        if not deserialization_required:
            return

        deserializer = resource.deserializers[req.method.lower()]
        try:
            result = deserializer.load(req.media)
        except ValidationError as err:
            raise HTTPError(falcon.HTTP_UNPROCESSABLE_ENTITY, err.messages)

        req._deserialized = result

    def process_response(self, req, resp, resource, req_succeeded):
        serialization_required = (hasattr(resource, "serializers")
                                  and req.method.lower() in resource.serializers
                                  and hasattr(resp, "_data"))
        if not serialization_required:
            return

        serializer = resource.serializers[req.method.lower()]
        try:
            result = serializer.dump(resp._data)
        except ValidationError as err:
            # TODO figure out when this gets hit. need better unit tests
            raise HTTPError(falcon.HTTP_IM_A_TEAPOT, err.messages)

        resp.media = result
