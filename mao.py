# mao: Memory Access Object

import json
from comn import PageHandler


class TodoItems(PageHandler):
    def initialize(self, context):
        self.items = context
        
    def get(self):
        self.json_response(json.dumps(self.items))


class TodoItem(PageHandler):
    def initialize(self, context):
        self.items = context

    def get(self, id=None):
        if id:
            item = self.get_filtered(id)
            self.json_response(json.dumps(item[0]))
        else:
            self.json_error()

    def post(self, id=None):
        print(id)
        if self.request.body:
            item = self.get_json_arg(self.request.body, ['name', 'id'])
            self.items.append(item)
            self.json_response(item, 201)
        else:
            self.json_error()

    def put(self, id):
        picked_item = self.get_filtered(id)
        if picked_item:
            self.items.remove(picked_item[0])
            item = self.get_json_arg(self.request.body, ['name'])
            item['id'] = int(id)
            self.items.append(item)
            self.json_response(item)

    def delete(self, id):
        new_items = [item for item in self.items if item['id'] != int(id)]
        self.items = new_items
        message = {'message': 'Item with id {} was deleted'.format(id)}
        self.json_response(message)

    def get_filtered(self, id):
        """
        Filters list to pick one item
        """
        result = [item for item in self.items if item['id'] == int(id)]
        return result
