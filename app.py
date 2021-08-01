# from tornado import httpserver
# from tornado import gen
# import tornado.web
import sys
import signal
import tornado.ioloop
from tornado.web import Application
from tornado.ioloop import IOLoop
from db import ping_db


__use_db = False
todo_implementation = __import__('dao' if __use_db else 'mao')


class InitialiseApp(Application):

    def __init__(self, context, todo_service):
        router = [
            (r"/", getattr(todo_service, 'TodoItems'), dict(context = context)),
            (r"/api/v1/item/([^/]+)?", getattr(todo_service, 'TodoItem'), dict(context = context))
        ]
        server_settings = {
            "debug": True,
            "autoreload": True
        }
        Application.__init__(self, router, **server_settings)


async def shutdown():
    print('<<< server stopped!')
    tornado.ioloop.IOLoop.current().stop()
    print('<<< process exited!')
    sys.exit(0) # means a clean exit without any errors / problems

def exit_handler(sig, frame):
    print('>>> to stop tornado server...')
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(shutdown)

def run_server():
    context = None if __use_db else []
    app = InitialiseApp(context, todo_implementation)
    app.listen(3000)
    signal.signal(signal.SIGTERM, exit_handler)
    signal.signal(signal.SIGINT,  exit_handler)
    print('>>> tornado server started!')
    IOLoop.instance().start()


if __name__ == '__main__':
    ping_db() if __use_db else None
    run_server()
