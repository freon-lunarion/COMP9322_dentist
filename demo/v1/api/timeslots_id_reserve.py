# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from . import timeslots_data as timeslots


class TimeslotsIdReserve(Resource):

    def post(self, id):
        for timeslot in timeslots:
            if timeslot['id'] == id and timeslot['is_reserved'] == True:
                return None, 403, None

            if timeslot['id'] == id and timeslot['is_reserved'] == False:
                timeslot['is_reserved'] = True
                return None, 202, None
        return None, 404, None