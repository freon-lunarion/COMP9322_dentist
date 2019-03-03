# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g


from . import Resource
from . import timeslots_data as timeslots
from .. import schemas

import uuid

class Timeslots(Resource):

    def get(self):
        print(g.args)
        rec_start = g.args['offset']
        rec_end = g.args['offset']+g.args['limit']
        output = list()
        for timeslot in timeslots:
            if timeslot['is_reserved'] is False:
                output.append(timeslot)

        return output[rec_start:rec_end], 200, None

    def post(self):
        print(g.json)
        id = uuid.uuid4()
        timeslot = {
            'id':id,
            'date': g.json['date'],
            'start': g.json['start'],
            'end': g.json['end'],
            'is_reserved': False
        }
        timeslots.append(timeslot)
        return None, 201, None