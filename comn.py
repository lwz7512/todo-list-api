# comn: common module

import json
from tornado.web import RequestHandler


class PageHandler(RequestHandler):

    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)
        self.finish()

    def json_error(self):
        self.json_response({'message': 'body is empty'}, 404)

    def get_json_arg(self, req_body, fields):
        """
        Gets argument from JSON
        """
        results = {}
        for i in fields:
            results[i] = json.loads(req_body).get(i)
        return results
