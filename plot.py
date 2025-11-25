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

	number_of_events = 0
	x = deque(maxlen=args.buffer)
	y = deque(maxlen=args.buffer)
	stop = False

	##########################

	def collect():

		data = telemetry(args.address, args.port)
		data.sock.settimeout(1)

		print("menu -> settings -> HUD and gameplay")
		print("DATA OUT = ON")
		print("DATA OUT IP ADDRESS =", data.sock.getsockname()[0])
		print("DATA OUT IP PORT =", data.sock.getsockname()[1])

		nonlocal number_of_events

		while not stop:

			number_of_events += 1
			try: data_copy = data()
			except TimeoutError: continue
			x.append(data_copy[1])
			y.append(data_copy[args.index])

	collector_thread = Thread(target=collect)
	collector_thread.start()

	##########################

	def animate(number_of_frames):

		nonlocal number_of_events
		if (number_of_events > args.buffer):
			print(f"Warning: lost {number_of_events - args.buffer} events since last update!")
		number_of_events = 0

		line.set_data(x, y)
		line.axes.relim()
		line.axes.autoscale_view()

	# The anim variable must remain declared, otherwise the animation stops!
	# TODO enable BLIT to improve performance

	anim = FuncAnimation(gcf(), animate, interval=0)
	line, = plot(x, y, ".-")
	show()  # blocks until plot windows is closed

	##########################

	stop = True
	collector_thread.join()


if __name__ == "__main__":
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-b", "--buffer", default=512, type=int)
	parser.add_argument("-i", "--index", default=49, type=int)
	parser.add_argument("-a", "--address", default="localhost")
	parser.add_argument("-p", "--port", default=0, type=int)
	main(parser.parse_args())
