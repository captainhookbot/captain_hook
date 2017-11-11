from __future__ import absolute_import
from ..base import BaseService


class ScrutinizerService(BaseService):
    def get_event(self, request, body):
        return request.headers.ge('X-Scrutinizer-Event', '').replace('.', '_')
