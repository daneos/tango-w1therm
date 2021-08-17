tango-w1therm
=============

A Tango device server for 1-wire digital temperature sensors using `w1_therm` driver.  
This includes `DS18*20`, `DS28EA00`, `GX20MH01` and their clones.

The server only supports reading the temperature, there is no support for setting any parameters, alarms, etc. (and I'm not sure there ever will be).

Requirements
------------

* Python 3.x (it should work on 2.7, but this was not tested)
* pytango 9.2+
* `w1_therm`, obviously

Installation
------------

To install, run `sudo python setup.py install` in the project's directory.  
To run, use `w1therm <instance_name>`.

Configuration
-------------

The device is configured using `device_id` property. It is the sensor ROM ID advertised over 1-wire bus.  
You can find the IDs of all 1-wire devices by running `ls /sys/bus/w1/devices`.  
The ID should look something like this: `28-3c01e076af23`. Of course in your case the numbers will be different.

Attributes
----------

There is a single attribute, `temperature`, which provides the sensor temperature in degrees Celsius.

Licensing
---------

This project is distributed under the GNU GPLv3 license. You can read the full license text in `LICENSE` file in project's directory.
