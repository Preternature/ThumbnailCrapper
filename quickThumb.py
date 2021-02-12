import os
import cv2
import time
import random
import datetime
import subprocess
from PIL import Image, ImageDraw, ImageFont


class Thumbnail_Crapper:

	def __init__(self, movieLoc, snapshotPathLoc, fontLoc):

		self.initializations(movieLoc, snapshotPathLoc, fontLoc)

		fullDirectory = os.listdir(movieLoc)
		fullDirectory = [i for i in fullDirectory if i.endswith('.mp4')]

		phrase = random.choice(self.copywrites)

		timesWeDoThis = 1
		for _ in range(timesWeDoThis):

			randStyle = random.randint(0, 2)
			drawEmojis = random.randint(0, 3)
			print(drawEmojis)

			if randStyle == 0:
				width = self.finalWidth
				height = self.finalHeight
				times = 1
			else:
				width = self.finalWidth // 2
				height = self.finalHeight // 2
				times = 4


			canvas = Image.new('RGB', (self.finalWidth, self.finalHeight))

			for inst in range(times):

				g = random.choice(fullDirectory)

				img = self.openMovie(g, width, height)

				time.sleep(1.5)

				img = Image.open(img)
				canvas.paste(img, self.placements[inst])

			# get a drawing context
			d = ImageDraw.Draw(canvas)

			middle = (self.finalWidth // 2, self.finalHeight // 2)

			phraseSize = d.textsize(text=phrase, font=self.font)			
			x = int((.5) * (self.finalWidth - phraseSize[0]))
			y = int((.5) * (self.finalHeight - phraseSize[1]))

			black = (0, 0, 0)
			white = (255, 255, 255)

			d.multiline_text((x-1, y-1), phrase, font=self.font, fill=black)
			d.multiline_text((x+1, y-1), phrase, font=self.font, fill=black)
			d.multiline_text((x-1, y+1), phrase, font=self.font, fill=black)
			d.multiline_text((x+1, y+1), phrase, font=self.font, fill=black)
			d.multiline_text((x, y), phrase, font=self.font, fill=white)
			print(d.im.size)
			#canvas.multiline_text((10,10), phrase, font=self.font, fill=(0, 0, 0))

			if drawEmojis:
				print('wetback')
				randEmoji = random.choice([char for char in self.emojisShitters])
				d.text((200, 200), randEmoji, font=self.unicodeFont, fill=black)



				
			canvas.save(R'C:\Users\Woody\Desktop\temp\done.jpg')

			#emojis = random.randint(0, )

			#gridFormat = random.randint(0, 3)

			# random screenie from first video, text
			#if gridFormat == 0:


			#print(g)


	def initializations(self, movieLoc, snapshotPathLoc, fontLoc):

		self.location = movieLoc
		self.snapshotPathLocation = snapshotPathLoc

		self.finalWidth = 1280
		self.finalHeight = 720

		self.placements = [
			(0, 0),
			(self.finalWidth // 2, 0),
			(0, self.finalHeight // 2),
			(self.finalWidth // 2, self.finalHeight // 2),
		]

		while True:
			randFont = random.choice(os.listdir(fontLoc))
			if not randFont.lower().endswith('fon'):
				break

		print(randFont)

		self.font = ImageFont.truetype(fR'{fontLoc}/{randFont}', 110)
		self.unicodeFont = ImageFont.truetype(fR'{fontLoc}/seguiemj.ttf', 110)
		#self.font = ImageFont.load(R"C:\Windows\Fonts\Arial\Arial Black.ttf")

		self.FNULL = open(os.devnull, 'wb')

		os.chdir(self.location)

		self.emojiList()

		self.copywrites = [
			'No Way',
			'No F***ing Way',
			'Epic',
			'Dope',
			'Dope A$$',
			'Epic Style',
			'Too Kool\nfor Skool',
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

		self.emojisShitters = '😱🤣😍🤫🥵🥶❓'


	def getMovieLength(self, movie):

		vcap = cv2.VideoCapture(movie)
		fps = vcap.get(cv2.CAP_PROP_FPS)
		frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
		length = frame_count / fps
		length = int(length * 1000)

		return length


	def openMovie(self, movie, width, height):

		now = time.time()

		snapshotPath =  Rf'{self.snapshotPathLocation}\\{now}.jpg'

		length = self.getMovieLength(movie)

		beginningOffset = 0.2
		endingOffset = 0.9
		randRange = (int(beginningOffset * length), int(endingOffset * length))
		position = random.randint(randRange[0], randRange[1])

		#bammo = f"-vf scale=w={width}:h={height}:force_original_aspect_ratio=decrease"
		bammo = ''

		command = (
					fR'ffmpeg -ss {position}ms -i "{movie}" -vframes 1 -s {width}x{height} {bammo} '
					fR'-f image2 "{snapshotPath}"'
				)
		subprocess.Popen(command, stdout=self.FNULL, stderr=subprocess.STDOUT)
		#subprocess.Popen(command)

		return snapshotPath


if __name__ == '__main__':

	moviesLoc = R'C:\Users\Woody\Desktop\stupidTests'
	snapshotLoc = R'C:\Users\Woody\Desktop\temp'
	fontLoc = R'C:/Windows/Fonts'

	Thumbnail_Crapper(moviesLoc, snapshotLoc, fontLoc)
