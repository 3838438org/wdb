#!/usr/bin/env python
from flask import Flask
import logging
from w import w
app = Flask(__name__)


def make_error():
    import whatever


def relay_error():
    make_error()


def bad_recur(n):
    1 / n
    return bad_recur(n - 1)


@app.route("/")
def bad_function():
    a = 2
    b = -2
    c = 1 / (a + b) < 0
    print c <b> a
    relay_error()
    return "Hello World!"


@app.route("/long")
def long_trace():
    return bad_recur(10)

from log_colorizer import make_colored_stream_handler
handler = make_colored_stream_handler()
app.logger.handlers = []
app.logger.addHandler(handler)
import werkzeug
werkzeug._internal._log('debug', '<-- I am with stupid')
logging.getLogger('werkzeug').handlers = []
logging.getLogger('werkzeug').addHandler(handler)
handler.setLevel(getattr(logging, 'DEBUG'))
app.logger.setLevel(getattr(logging, 'DEBUG'))
logging.getLogger('werkzeug').setLevel(
    getattr(logging, 'DEBUG'))

try:
    import wsreload
except ImportError:
    app.logger.debug('wsreload not found')
else:
    url = "http://l:1984/*"

    def log(httpserver):
        app.logger.debug('WSReloaded after server restart')
    wsreload.monkey_patch_http_server({'url': url}, callback=log)
    app.logger.debug('HTTPServer monkey patched for url %s' % url)

app.wsgi_app = w(app.wsgi_app)
app.run(debug=True, host='0.0.0.0', port=1984, use_debugger=False, use_reloader=True)
# 80chars 80chars 80chars 80chars 80chars 80chars 80chars 80chars 80chars 80char
