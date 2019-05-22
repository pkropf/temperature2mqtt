# temperature2mqtt

Read a dht 22 temperature sensor and publish the temperature and humidity to mqtt.

Use the install.sh script to install the application. If environment variables are
used in the .ini file, they should be added to the service using:

    systemctl edit temperature2mqtt

For example, if there is an environment variable that is to be used called SITE,
add:

    [Service]
    Environment=SITE=This is my site name
    Environment=LOCATION=The sensor is located here
