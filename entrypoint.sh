#!/bin/bash

set -x
echo "Starting backend ...sleep 20s waiting pg"
sleep 20

echo "Run migrate"
export FLASK_APP=run.py
flask db upgrade
