"""Collection of hooks"""
from .utilities import find_by_id


class LoadObjectFromDB(object):
    def __init__(self, model):
        self._model = model

    def __call__(self, req, resp, resource, params):
        req._item = find_by_id(db=req.context["db"], model=self._model, id=params["id"])
