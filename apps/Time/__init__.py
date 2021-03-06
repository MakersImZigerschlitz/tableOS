# App Information
AppName = "Time"
AppAuthor = "Mike Zweifel"
AppVersion = "0.1"
AppImage = [[[231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24], [231, 1, 24]], [[220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35], [220, 2, 35]], [[209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46], [209, 3, 46]], [[199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56], [199, 3, 56]], [[188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67], [188, 4, 67]], [[177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78], [177, 4, 78]], [[166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89], [166, 5, 89]], [[155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100], [155, 5, 100]], [[145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110], [145, 6, 110]], [[134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121], [134, 7, 121]], [[123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132], [123, 7, 132]], [[112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143], [112, 8, 143]], [[101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154], [101, 8, 154]], [[91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164], [91, 9, 164]], [[80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175], [80, 10, 175]], [[69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186], [69, 10, 186]], [[58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197], [58, 11, 197]], [[47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208], [47, 11, 208]], [[37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218], [37, 12, 218]], [[26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229], [26, 13, 229]]]

import math, sys
import time
import colorsys

pixels = [[[255 for x in range(3)] for x in range(10)] for x in range(20)]
numMatrix = [[0 for x in range(30)] for x in xrange(8)]
numMatrix = [[0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0],[1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1],[1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1],[1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1],[1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1],[0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0]]
brightness = 0.0
spidev = file("/dev/spidev0.0", "wb")

def drawsnake():
	for row in range(0,20):
		if row%2==0:
			for pixel in range(0,10):
				for color in range(0,3):
					c=int(pixels[row][pixel][color]*brightness)
					spidev.write(chr(c & 0xFF))
		else:
			for pixel in range(9,-1,-1):
				for color in range(0,3):
					c=int(pixels[row][pixel][color]*brightness)
					spidev.write(chr(c & 0xFF))			
        spidev.flush()
        time.sleep(0.001)
def run():
	global pixels
	global brightness
	global numMatrix
	brightness = 1
	pixels = [[[0 for x in range(3)] for x in range(10)] for x in range(20)]
	while 1:
		timestring = time.strftime("%H%M")
		zahleins = int(timestring[0])
		for x in range (1,9):
			for y in range (1,4):
				if numMatrix[(x-1)][(zahleins*3)+(y-1)]==1:
					pixels[y][9-x]=[255,0,0]
				else:
					pixels[y][9-x]=[0,0,0]
		zahlzwei = int(timestring[1])
		for x in range (1,9):
			for y in range (1,4):
				if numMatrix[(x-1)][(zahlzwei*3)+(y-1)]==1:
					pixels[y+4][9-x]=[255,0,0]
				else:
					pixels[y+4][9-x]=[0,0,0]
		zahldrei = int(timestring[2])
		for x in range (1,9):
			for y in range (1,4):
				if numMatrix[(x-1)][(zahldrei*3)+(y-1)]==1:
					pixels[y+11][9-x]=[255,0,0]
				else:
					pixels[y+11][9-x]=[0,0,0]
		zahlvier = int(timestring[3])
		for x in range (1,9):
			for y in range (1,4):
				if numMatrix[(x-1)][(zahlvier*3)+(y-1)]==1:
					pixels[y+15][9-x]=[255,0,0]
				else:
					pixels[y+15][9-x]=[0,0,0]
		#Punkte
		timestring = time.strftime("%S")
		if int(timestring)%2==0:
			pixels[9][2]=[255,0,0]
			pixels[10][2]=[255,0,0]
			pixels[9][3]=[255,0,0]
			pixels[10][3]=[255,0,0]

			pixels[9][6]=[255,0,0]
			pixels[10][6]=[255,0,0]
			pixels[9][7]=[255,0,0]
			pixels[10][7]=[255,0,0]
		else:
			pixels[9][2]=[0,0,0]
			pixels[10][2]=[0,0,0]
			pixels[9][3]=[0,0,0]
			pixels[10][3]=[0,0,0]

			pixels[9][6]=[0,0,0]
			pixels[10][6]=[0,0,0]
			pixels[9][7]=[0,0,0]
			pixels[10][7]=[0,0,0]
		drawsnake()
		time.sleep(1)

if __name__ == '__main__':
	run()
