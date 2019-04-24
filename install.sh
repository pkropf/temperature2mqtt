#! /bin/bash


cp -b -S "-`date "+%Y%m%d%H%M%S"`" temperature2mqtt.ini  /usr/local/bin/
cp temperature2mqtt.py      /usr/local/bin/
cp temperature2mqtt.sh      /usr/local/bin/
cp temperature2mqtt.service /lib/systemd/system/

systemctl daemon-reload
systemctl enable temperature2mqtt
systemctl start temperature2mqtt
