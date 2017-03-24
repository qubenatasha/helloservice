from qube.src.api.swagger_models.helloservice \
    import HelloServiceModel, HelloServiceModelPost

"""
swagger parameters definitions
"""
header_ex = {
    "type": "string",
    "description": "Custom header that is expected as part of the request",
    "name": "Authorization",
    "in": "header",
    "required": False
}

path_ex = {
    "type": "string",
    "description": "This is the part of the URL",
    "name": "entity_id",
    "in": "path",
    "required": True
}

query_ex = {
    "type": "string",
    "description": "Query string appended to the URL",
    "name": "sth",
    "in": "query",
    "required": True
    # "required": False
}

body_ex = {
    'name': 'body',
    'description': 'Request body',
    'in': 'body',
    'schema': HelloServiceModel,
    'required': True,
}

body_post_ex = {
    'name': 'body',
    'description': 'Request body',
    'in': 'body',
    'schema': HelloServiceModelPost,
    'required': True,
}

body_put_ex = {
    'name': 'body',
    'description': 'Request body',
    'in': 'body',
    'schema': HelloServiceModelPost,
    'required': True,
}
