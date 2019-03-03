# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter
import uuid
timeslots_data = [
    {
        'id' : uuid.uuid4(),
        'date' : '2019-03-06',
        'start' : '09:30',
        'end' : '10:00',
        'is_reserved' : False
    },
    {
        'id' : uuid.uuid4(),
        'date' : '2019-03-06',
        'start' : '10:00',
        'end' : '10:30',
        'is_reserved' : False
    }
]

class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]