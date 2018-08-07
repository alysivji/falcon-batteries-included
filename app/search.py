from app import es as elasticsearch


def add_to_index(index, model):
    if not elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    elasticsearch.index(index=index, doc_type=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not elasticsearch:
        return
    elasticsearch.delete(index=index, doc_type=index, id=model.id)


def query_index(index, query, page, per_page):
    if not elasticsearch:
        return [], 0
    search = elasticsearch.search(
        index=index,
        doc_type=index,
        body={
            "query": {"multi_match": {"query": query, "fields": ["*"]}},
            "from": (page - 1) * per_page,
            "size": per_page,
        },
    )
    ids = [int(hit["_id"]) for hit in search["hits"]["hits"]]
    return ids, search["hits"]["total"]
