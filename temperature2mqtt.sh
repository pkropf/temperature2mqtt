#! /bin/bash


SCRIPT_PATH=`dirname "${BASH_SOURCE[0]}"`
source $SCRIPT_PATH/../venvs/temperature2mqtt/bin/activate
echo `type python3.7`

exec $SCRIPT_PATH/temperature2mqtt.py
