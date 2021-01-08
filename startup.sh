#!/bin/sh
gunicorn "filmesenti.wsgi" -b "0.0.0.0:${PORT}"