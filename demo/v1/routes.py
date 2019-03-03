# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslots import Timeslots
from .api.timeslots_id import TimeslotsId
from .api.timeslots_id_reserve import TimeslotsIdReserve


routes = [
    dict(resource=Timeslots, urls=['/timeslots'], endpoint='timeslots'),
    dict(resource=TimeslotsId, urls=['/timeslots/<id>'], endpoint='timeslots_id'),
    dict(resource=TimeslotsIdReserve, urls=['/timeslots/<id>/reserve'], endpoint='timeslots_id_reserve'),
]