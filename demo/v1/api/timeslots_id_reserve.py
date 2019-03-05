# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from . import timeslots_data as timeslots


class TimeslotsIdReserve(Resource):

    def post(self, id):
        print(id)
        for timeslot in timeslots:
            print(timeslot)
            if str(timeslot['id']) == id and timeslot['is_reserved'] == True:
                return None, 403, None

            if str(timeslot['id']) == id and timeslot['is_reserved'] == False:
                timeslot['is_reserved'] = True
                return None, 201, None
        return None, 404, None