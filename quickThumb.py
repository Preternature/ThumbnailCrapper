import os
import cv2
import time
import random
import datetime
import subprocess
from PIL import Image


class Thumbnail_Crapper:

	def __init__(self, location, snapshotPathLocation):

		self.initializations(location, snapshotPathLocation)

		fullDirectory = os.listdir(location)
		fullDirectory = [i for i in fullDirectory if i.endswith('.mp4')]

		timesWeDoThis = 1
		for _ in range(timesWeDoThis):

			g = random.choice(fullDirectory)

			print(g)

			img = self.openMovie(g, self.finalWidth, self.finalHeight)

			#emojis = random.randint(0, )

			#gridFormat = random.randint(0, 3)

			# random screenie from first video, text
			#if gridFormat == 0:


			#print(g)


	def initializations(self, location, snapshotPathLocation):

		self.location = location
		self.snapshotPathLocation = snapshotPathLocation

		self.finalWidth = 1280
		self.finalHeight = 720

		self.FNULL = open(os.devnull, 'wb')

		os.chdir(location)

		self.emojiList()

		self.copywrites = [
			'No Way',
			'No F***ing Way',
			'Epic',
			'Epic Style',
			'Too Kool for Skool',
			'Must See',
			'Amazeballs',
			'For Jesus',
			'Like if you\'re horny ;D',
		]


	def emojiList(self):

		self.screamEmoji 		= '😱'
		self.laughEmoji 		= '🤣'
		self.heartEyesEmoji 	= '😍'
		self.youWontBelieve 	= '🤫'
		self.hotEmoji		 	= '🥵'
		self.coldEmoji		 	= '🥶'
		self.qMarkEmoji	 		= '❓'


	def getMovieLength(self, movie):

		vcap = cv2.VideoCapture(movie)
		height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

		fps = vcap.get(cv2.CAP_PROP_FPS)
		frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
		length = frame_count / fps
		length = int(length * 1000)

		return length


	def openMovie(self, movie, width, height):

		now = time.time()

		snapshotPath =  f'{self.snapshotPathLocation}\\{now}.jpg'

		length = self.getMovieLength(movie)

		beginningOffset = 0.2
		endingOffset = 0.9
		randRange = (int(beginningOffset * length), int(endingOffset * length))
		position = random.randint(randRange[0], randRange[1])

		command = (
					fR'ffmpeg -ss {position}ms -i "{movie}" -vframes 1 -s {width}x{height} '
					fR'-f image2 "{snapshotPath}"'
				)
		subprocess.Popen(command, stdout=self.FNULL, stderr=subprocess.STDOUT)
		#subprocess.Popen(command)

		return snapshotPath


if __name__ == '__main__':

	moviesLoc = R'A:\Source'
	snapshotLoc = R'C:\Users\Woody\Desktop\temp'

	Thumbnail_Crapper(moviesLoc, snapshotLoc)
