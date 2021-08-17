import os
import re
from tango import AttrWriteType, DevState
from tango.server import run, Device, attribute, device_property

path = "/sys/bus/w1/devices/{device_id}/{node}"


class w1therm(Device):

	device_id = device_property(
		dtype=str,
		doc="Thermometer ROM ID",
	)

	temperature = attribute(
		label="Temperature",
		dtype=float,
		access=AttrWriteType.READ,
		unit="C",
		format="3.3f",
		fget="get_temperature"
	)

	def init_device(self):
		Device.init_device(self)
		self.set_state(DevState.INIT)
		p = path.format(device_id=self.device_id, node="temperature")
		if os.path.exists(p):
			self.node = "temperature"
			self.path = p
			self.info_stream("Using \"temperature\" node.")
			self.set_state(DevState.ON)
		else:
			p = path.format(device_id=self.device_id, node="w1_slave")
			if os.path.exists(p):
				self.node = "slave"
				self.path = p
				self.info_stream("\"temperature\" node not supported.\nUsing \"w1_slave\" node.")
				self.set_state(DevState.ON)
			else:
				self.path = None
				info = "Could not find the sensor with id={device_id}".format(device_id=self.device_id)
				self.info_stream(info)
				self.set_state(DevState.FAULT)
				self.set_status(info)

	def get_temperature(self):
		data = None
		temp = None
		if self.path is not None:
			# following the w1_therm documentation, temperature conversion is triggered
			# by the open-read sequence, so it's not sufficient to just open the file
			# once and read it multiple times
			with open(self.path) as f:
				data = f.read()
			temp_mdeg = 0
			if self.node == "temperature":
				temp_mdeg = int(data)
			if self.node == "slave":
				m = re.search(r".*t=(\d*)", data)
				if m is not None:
					temp_mdeg = int(m.group(1))
			temp = temp_mdeg / 1000.0
		return temp


def start():
	run((w1therm,))


if __name__ == "__main__":
	start()
