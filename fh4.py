"""Reads telemetry data from Forza Horizon 4"""

from socket import AF_INET, SOCK_DGRAM, socket
from struct import calcsize, unpack

class telemetry:

	def __init__(self, address, port):

		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.sock.bind((address, port))
		self.format = "<iI27f4i20f5i12x17fH6B3bx"
		self.size = calcsize(self.format)

	def __call__(self):

		return unpack(self.format, self.sock.recv(self.size))
