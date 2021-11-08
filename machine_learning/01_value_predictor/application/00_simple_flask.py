#!/usr/bin/env python
# coding: utf-8

from werkzeug.wrappers import Request, Response
from flask import Flask

# init app
app = Flask(__name__)


# routes - is decorated
@app.route("/")
def index():
    return "Hello World"


# if we run script __name__ == __main__, if we import it it will contain script name
if __name__ == "__main__":
    from werkzeug.serving import (
        run_simple,
    )  # this is simple development server we can use

    run_simple("localhost", 9000, app)

