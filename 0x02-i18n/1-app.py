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


def get_locale():
    """Pick the best language translation to use.
    """
    return request.accept_languages.best_match(Config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def basic_app():
    """Basic Flask app.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
