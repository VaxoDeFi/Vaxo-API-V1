#!/bin/bash -x

python -m venv vaxo-venv
pip install -r requirements.txt
qwd='printf "%q\n" "$(pwd)"'
echo $qwd
activate () {
    . $qwd/vaxo-venv/bin/activate
}

activate