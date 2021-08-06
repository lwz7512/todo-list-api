# dao:  Database Access Object
# todo service to interactive with mysql:
# insert, quey, update, delete

import json
from comn import PageHandler
from db import table_name, get_connection, get_cursor, close_db

class TodoItems(PageHandler):
    def initialize(self, context):
        self.context = context

    def get(self):
        cursor = get_cursor()
        result = cursor.execute("SELECT * from {0}".format(table_name))
        todos = cursor.fetchall() if result else []
        self.json_response(json.dumps(todos))
        cursor.close()
        close_db()


class TodoItem(PageHandler):
    def initialize(self, context):
        self.context = context

    # get one todo
    def get(self, id=None):
        cursor = get_cursor()
        values = (int(id),)
        result = cursor.execute("SELECT * from {0} WHERE id=%s".format(table_name), values)
        todo = cursor.fetchone() if result else {}
        self.json_response(todo)
        # finally clear connection
        cursor.close()
        close_db()

    # insert new todo
    def post(self, id=None):
        connection = get_connection()
        cursor = get_cursor()
        if self.request.body:
            item = self.get_json_arg(self.request.body, ['name'])
            values = (int(id), item["name"])
            cursor.execute("INSERT INTO {0}(id, name) VALUES(%s, %s)".format(table_name), values)
            connection.commit() # commit this operation to save new record!
            self.json_response(item, 201)
        else:
            self.json_error()
        # finally clear connection
        cursor.close()
        close_db()


    # TODO: update one todo
    def put(self, id):
        pass

    # delete one todo
    def delete(self, id):
        connection = get_connection()
        cursor = get_cursor()
        if id:
            values = (int(id),)
            result = cursor.execute("DELETE FROM {0} WHERE id=%s".format(table_name), values)
            connection.commit()
            message = {"message": "deleted"} if result else {"message": "doesnt exist!"}
            self.json_response(message)
        # finally clear connection
        cursor.close()
        close_db()
