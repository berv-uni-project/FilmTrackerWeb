#!/bin/sh
gunicorn "filmsenti.wsgi" -b "0.0.0.0:${PORT}"