# WEB IOT
## IOT
The internet of things (IOT) is a network of sensors, and other embedded systems that are connected and are in sync through the use of internet. This includes data extraction, data proicessing, data exchange and all shorts of other communications. IOT is recent technology whose popularity is growing exponentially. 

## Components of IOT
Complete IOT platform integrates several technologies as below:
1. Sensors and actuators
2. Gateway
3. Cloud
4. Analytics 
5. User interface

## Web IOT
This project includes the *cloud* and *ueser* *interface* part of the components of IOT. 

## Features
It is a Django project that use websocket for communication with both devices and the UI. This project use redis core in channel layer to implement websocket. The project use sqlite as database for now but can be expanded to other databases if needed. Likewise, the project is also capable of MQTT communication with *broker.emqx.io* as broker and on port 1883.
