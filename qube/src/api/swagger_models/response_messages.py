from flask_restful_swagger_2 import Schema

from qube.src.api.swagger_models.helloservice import HelloServiceErrorModel
from qube.src.api.swagger_models.helloservice import HelloServiceModel
from qube.src.api.swagger_models.helloservice import HelloServiceModelPostResponse

"""
the common response messages printed in swagger UI
"""

post_response_msgs = {
    '201': {
        'description': 'CREATED',
        'schema': HelloServiceModelPostResponse
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': HelloServiceErrorModel
    }
}

get_response_msgs = {
    '200': {
        'description': 'OK',
        'schema': HelloServiceModel
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': HelloServiceErrorModel
    }
}

put_response_msgs = {
    '204': {
        'description': 'No Content'
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': HelloServiceErrorModel
    }
}

del_response_msgs = {
    '204': {
        'description': 'No Content'
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error',
        'schema': HelloServiceErrorModel
    }
}

response_msgs = {
    '200': {
        'description': 'OK'
    },
    '401': {
        'description': 'Unauthorized'
    },
    '400': {
        'description': 'Bad Request'
    },
    '404': {
        'description': 'Not found'
    },
    '500': {
        'description': 'Internal server error'
    }
}


class ErrorModel(Schema):
    type = 'object'
    properties = {
        'error_code': {
            'type': 'string'
        },
        'error_message': {
            'type': 'string'
        }
    }
