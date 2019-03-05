# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from . import timeslots_data as timeslots


class TimeslotsId(Resource):

    def delete(self, id):
        for timeslot in timeslots:
            if str(timeslot['id']) == id:
                timeslots.remove(timeslot)
                return None, 200, None

        return None, 404, None
