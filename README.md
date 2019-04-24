# temperature2mqtt

Read a dht 22 temperature sensor and publish the temperature and humidity to mqtt.

## Installation
Use the install.sh script to install the application. This will copy the needed
files to /usr/local/bin. Edit the temperature2mqtt.ini file and add the mqtt broker
to use and verify that the topics are what's needed. 

If environment variables are used in the temperature2mqtt.ini file, they should
be added to the service using:

    systemctl edit temperature2mqtt

For example, if there is an environment variable that is to be used called SITE,
add:

    [Service]
    Environment=SITE=This is my site name

The runtime environment assumes that there is a python3.7 venv set up in
/usr/local/venvs/temperature2mqtt and that the needed requirements have been
installed. This can be done by activating the venv and then running:

    pip install -r requirements.txt
