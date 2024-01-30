#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start a Flash Web Application.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config(object):
    """Supported Language list.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel()
app.config.from_object(Config)
babel.init_app(app)


@app.route('/', strict_slashes=False)
def basic_app():
    """Basic Flask app.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
