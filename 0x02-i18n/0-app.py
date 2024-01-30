#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start a Flash Web Application.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def basic_app() -> str:
    """Basic Flask app.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
