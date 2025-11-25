#!/usr/bin/env python3
"""Plots telemetry data from Forza Horizon 4 in real time"""

from argparse import ArgumentParser
from collections import deque
from threading import Thread
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import gcf, plot, show
from fh4 import telemetry

def main(args):

	# The animation function runs in the main thread
	# while the collect function runs in a separated thread
	# The variables below are shared between them

	x = deque(maxlen=args.buffer)
	y = {}
	for i in args.index:
		y[i] = deque(maxlen=args.buffer)
	stop = False

	##########################

	def collect():

		data = telemetry(args.address, args.port)
		data.sock.settimeout(1)

		print("menu -> settings -> HUD and gameplay")
		print("DATA OUT = ON")
		print("DATA OUT IP ADDRESS =", data.sock.getsockname()[0])
		print("DATA OUT IP PORT =", data.sock.getsockname()[1])

		while not stop:

			try: data_copy = data()
			except TimeoutError: continue
			x.append(data_copy[1])
			for i in args.index:
				y[i].append(data_copy[i])

	collector_thread = Thread(target=collect)
	collector_thread.start()

	##########################

	def animate(number_of_frames):

		for i in args.index:
			line[i].set_data(x, y[i])
			line[i].axes.relim()
			line[i].axes.autoscale_view()

	# The anim variable must remain declared, otherwise the animation stops!
	# TODO enable BLIT to improve performance

	anim = FuncAnimation(gcf(), animate, interval=50)
	line = {}
	for i in args.index:
		line[i], = plot(x, y[i], ".-")
	show()  # blocks until plot windows is closed

	##########################

	stop = True
	collector_thread.join()


if __name__ == "__main__":
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-b", "--buffer", default=512, type=int)
	parser.add_argument("-i", "--index", nargs="+", type=int)
	parser.add_argument("-a", "--address", default="localhost")
	parser.add_argument("-p", "--port", default=0, type=int)
	main(parser.parse_args())
