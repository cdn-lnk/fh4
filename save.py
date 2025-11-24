#!/usr/bin/env python3
"""Saves telemetry data from Forza Horizon 4 into a .csv file"""

from argparse import ArgumentParser
from csv import writer
from fh4 import telemetry

def main(args):

	data = telemetry(args.address, args.port)

	print("menu -> settings -> HUD and gameplay")
	print("DATA OUT = ON")
	print("DATA OUT IP ADDRESS =", data.sock.getsockname()[0])
	print("DATA OUT IP PORT =", data.sock.getsockname()[1])
	print()
	print("Press ctrl+c to exit")

	with open(args.output, "x") as file:
		csv = writer(file)
		while True:
			try: csv.writerow(data())
			except KeyboardInterrupt: break


if __name__ == "__main__":
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-o", "--output", default="data.csv")
	parser.add_argument("-a", "--address", default="localhost")
	parser.add_argument("-p", "--port", default=0, type=int)
	main(parser.parse_args())
