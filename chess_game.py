"""
CHESS GAME!!

To do:
Lose scene
Main menu
"""


import pygame, sys
from pygame.locals import *

class Piece:
	def __init__(self, name, piece_type, image, coord = (0, 0), state = 1):
		self.name = name
		self.piece_type = piece_type
		self.coord = coord
		self.state = state
		self.image = image

	def move(self, new_coord):
		self.coord = new_coord

	def dead(self):
		self.state = 0
		self.coord = None

	def get_moveList(self, whitePieces, blackPieces):
		#Note that all pieces are assumed to be white-friendly ## DONE AND WORKING!
		moveList = []
		removeList = []
		whitePositions = []
		blackPositions = []
		for piece in whitePieces:
			whitePositions.append(piece.coord)
		for piece in blackPieces:
			blackPositions.append(piece.coord)

		if self.coord in whitePositions:
			whitePositions.remove(self.coord)
		elif self.coord in blackPositions:
			blackPositions.remove(self.coord)

		allPositions = whitePositions + blackPositions
		x, y = self.coord

		if self.piece_type == "king":
			for i in range(-1, 2):
				for j in range(-1, 2):
					moveList.append((x + i, j))
			moveList.remove((x, y))

			for white in whitePositions:
				if white in moveList:
					removeList.append(white)

		elif self.piece_type == "queen":
			for i in range(8):
				moveList.append((x, i))
				moveList.append((i, y))
			moveList.remove((x, y))
			moveList.remove((x, y))

			for position in allPositions:
				if position in moveList:
					if position[0] > x:
						for move in moveList:
							if move not in removeList and move[0] > position[0]:
								removeList.append(move)
					elif position[0] < x:
						for move in moveList:
							if move not in removeList and move[0] < position[0]:
								removeList.append(move)
					elif position[1] > y:
						for move in moveList:
							if move not in removeList and move[1] > position[1]:
								removeList.append(move)
					elif position[1] < y:
						for move in moveList:
							if move not in removeList and move[1] < position[1]:
								removeList.append(move)

					if position in moveList and position not in removeList and position in whitePositions:
						removeList.append(position)


			for i in range(1, 8):
				moveList.append((x + i, y + i))
				moveList.append((x - i, y - i))
				moveList.append((x + i, y - i))
				moveList.append((x - i, y + i))

			for position in allPositions:
				if position in moveList:
					if position[0] > x and position[1] > y:
						for move in moveList:
							if move not in removeList and move[0] > position[0] and move[1] > position[1]:
								removeList.append(move)
					elif position[0] < x and position[1] < y:
						for move in moveList:
							if move not in removeList and move[0] < position[0] and move[1] < position[1]:
								removeList.append(move)
					elif position[0] > x and position[1] < y:
						for move in moveList:
							if move not in removeList and move[0] > position[0] and move[1] < position[1]:
								removeList.append(move)
					elif position[0] < x and position[1] > y:
						for move in moveList:
							if move not in removeList and move[0] < position[0] and move[1] >position[1]:
								removeList.append(move)

					if position in moveList and position not in removeList and position in whitePositions:
						removeList.append(position)

		elif self.piece_type == "castle":
			for i in range(8):
				moveList.append((x, i))
				moveList.append((i, y))
			moveList.remove((x, y))
			moveList.remove((x, y))

			for position in allPositions:
				if position in moveList:
					if position[0] > x:
						for move in moveList:
							if move not in removeList and move[0] > position[0]:
								removeList.append(move)
					elif position[0] < x:
						for move in moveList:
							if move not in removeList and move[0] < position[0]:
								removeList.append(move)
					elif position[1] > y:
						for move in moveList:
							if move not in removeList and move[1] > position[1]:
								removeList.append(move)
					elif position[1] < y:
						for move in moveList:
							if move not in removeList and move[1] < position[1]:
								removeList.append(move)

					if position in moveList and position not in removeList and position in whitePositions:
						removeList.append(position)

		elif self.piece_type == "knight":
			moves = [(x + 1, y + 2), (x + 2, y + 1), (x - 1, y - 2), (x - 2, y - 1), (x + 1, y - 2), (x + 2, y - 1), (x - 1, y + 2), (x - 2, y + 1)]
			moveList.extend(moves)

			for white in whitePositions:
				if white in moveList:
					moveList.remove(white)

		elif self.piece_type == "bishop":
			for i in range(1, 8):
				moveList.append((x + i, y + i))
				moveList.append((x - i, y - i))
				moveList.append((x + i, y - i))
				moveList.append((x - i, y + i))

			for position in allPositions:
				if position in moveList:
					if position[0] > x and position[1] > y:
						for move in moveList:
							if move not in removeList and move[0] > position[0] and move[1] > position[1]:
								removeList.append(move)
					elif position[0] < x and position[1] < y:
						for move in moveList:
							if move not in removeList and move[0] < position[0] and move[1] < position[1]:
								removeList.append(move)
					elif position[0] > x and position[1] < y:
						for move in moveList:
							if move not in removeList and move[0] > position[0] and move[1] < position[1]:
								removeList.append(move)
					elif position[0] < x and position[1] > y:
						for move in moveList:
							if move not in removeList and move[0] < position[0] and move[1] >position[1]:
								removeList.append(move)

					if position in moveList and position not in removeList and position in whitePositions:
						removeList.append(position)

		elif self.piece_type == "white pawn":
			if (x, y - 1) not in allPositions:
				moveList.append((x, y - 1))
				if self.coord[1] == BOXNUM - 2:
					if (x, y - 2) not in allPositions:
						moveList.append((x, y - 2))

			for black in blackPositions:
				if black == (x - 1, y - 1) or black == (x + 1, y - 1):
					moveList.append(black)

		elif self.piece_type == "black pawn":
			if (x, y + 1) not in allPositions:
				moveList.append((x, y + 1))
				if self.coord[1] == 1:
					if (x, y + 2) not in allPositions:
						moveList.append((x, y + 2))

			for black in blackPositions:
				if black == (x + 1, y + 1) or black == (x - 1, y + 1):
					moveList.append(black)

		for move in removeList:
			moveList.remove(move)

		removeList = []

		for move in moveList:
			if (move[0] < 0) or (move[0] > BOXNUM - 1) or (move[1] < 0) or (move[1] > BOXNUM - 1):
				removeList.append(move)

		for move in removeList:
			moveList.remove(move)

		return moveList


	def __repr__(self):
		x = "Name: {}\n".format(self.name)
		x += "Piece type: {}\n".format(self.piece_type)
		x += "Coords {}\n".format(self.coord)
		x += "State {}\n".format(self.state)
		x += "Image source {}\n".format(self.image)
		return x

FPS = 10
WINDOWSIZE = 800
MARGIN = WINDOWSIZE/10
BOXNUM = 8
BOXSIZE = (WINDOWSIZE - 2 * MARGIN)/BOXNUM


#			    R    G    B    a
WHITE 		= (255, 255, 255)
LIGHTGRAY  	= (100, 100, 100)
DARKGRAY	= (200, 200, 200)
BLUE        = (  0,   0, 255)
REDTINT     = (255,   0,   0, 128)
GREENTINT	= (  0, 255,   0, 128)
BLUETINT	= (  0,   0, 255, 128)
CYANTINT	= (  0, 100, 255, 128)

BGCOLOR = BLUE



temp1 = []
temp2 = []
temp3 = []
temp4 = []
temp5 = []
temp6 = []
for i in range(1, 9):
	temp1.append("wp{}".format(i))
	temp2.append("bp{}".format(i))
	temp3.append("white pawn")
	temp4.append("black pawn")
	temp5.append("pawn W.png")
	temp6.append("pawn B.png")

WPIECENAMES = ("wc1", "wkn1", "wb1", "wq", "wk", "wb2", "wkn2", "wc2") + tuple(temp1)
BPIECENAMES = ("bc1", "bkn1", "bb1", "bq", "bk", "bb2", "bkn2", "bc2") + tuple(temp2)
WPIECETYPES = ("castle", "knight", "bishop", "queen", "king", "bishop", "knight", "castle") + tuple(temp3)
BPIECETYPES = ("castle", "knight", "bishop", "queen", "king", "bishop", "knight", "castle") + tuple(temp4)
WPIECEIMG = ("castle W.png", "knight W.png", "bishop W.png", "queen W.png", "king W.png", "bishop W.png", "knight W.png", "castle W.png") + tuple(temp5)
BPIECEIMG = ("castle B.png", "knight B.png", "bishop B.png", "queen B.png", "king B.png", "bishop B.png", "knight B.png", "castle B.png") + tuple(temp6)

del temp1
del temp2
del temp3
del temp4
del temp5
del temp6


def main():
	global DISPLAYSURF, FPSCLOCK, TURN

	pygame.init()

	DISPLAYSURF = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))
	FPSCLOCK = pygame.time.Clock()

	mousex = 0 
	mousey = 0
	pygame.display.set_caption("Chess")

	selectedPieceWhite = None
	selectedPieceBlack = None
	selectedPiece1 = None
	selectedPiece2 = None
	selectedBox1 = None
	selectedBox2 = None

	whitePieces, blackPieces = generatePieces()
	board = generateBoardData(whitePieces, blackPieces)
	TURN = 0

	while True:
		mouseClicked = False

		DISPLAYSURF.fill(BGCOLOR)
		drawBoard()
		drawPieces(whitePieces, blackPieces)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEMOTION:
				#get position of mouse when hovering
				mousex, mousey = event.pos
			if event.type == MOUSEBUTTONUP:
				#get position of mouse when clicked
				mousex, mousey = event.pos
				mouseClicked = True

		#stores box mouse is over
		boxx, boxy = getBoxAtPixel(mousex, mousey)

		if boxx != None and boxy != None:
		#if the mouse is hovering over a box
			if mouseClicked == False:
			#if mouse is only hovering over the box, highlight the box
				highlightBox(boxx, boxy, BLUETINT)	#working
			else:
			#if mouse clicks on the box
				if selectedPiece1 == None:
				#if no piece is previously selected, store the first piece and box
					selectedPiece1 = getPieceAtBox(boxx, boxy, whitePieces, blackPieces)
					selectedBox1 = getBoxAtPosition(boxx, boxy)
				elif selectedBox1 != (boxx, boxy):
				#if a piece was selected already, store the second piece and box in other variables if the box clicked is not the same as the previous one
					selectedPiece2 = getPieceAtBox(boxx, boxy, whitePieces, blackPieces)
					selectedBox2 = getBoxAtPosition(boxx, boxy)


		if selectedPiece1 != None:
		#if a piece is previously selected, get the list of possible moves of the piece
			if TURN % 2 == 0:
				moveList = selectedPiece1.get_moveList(whitePieces, blackPieces)
				if selectedBox2 == None:
				#If a second box is not selected, highlight possible moves
					if selectedPiece1 in whitePieces:
						highlightMoves(moveList, GREENTINT)
					else:
						moveList = selectedPiece1.get_moveList(blackPieces, whitePieces)
						highlightMoves(moveList, REDTINT)
				else:
				#if a box is selected, move piece and eat the piece on the box if there's one, then reset all variables
					if selectedPiece1 in whitePieces and selectedBox2 in moveList:
						selectedPiece1.move(selectedBox2)
						if selectedPiece2 != None and selectedPiece1.coord == selectedPiece2.coord:
						#if there is a piece on the selected box, then the selected piece will die
							selectedPiece2.dead()
						selectedPiece1 = None
						selectedPiece2 = None
						selectedBox1 = None
						selectedBox2 = None
						TURN += 1
					else:
					#if the piece cannot move to that box, replace first selections with the second selections
						selectedPiece1 = selectedPiece2
						selectedBox1 = selectedBox2
						selectedPiece2 = None
						selectedBox2 = None

			else:
				#If a second box is not selected, highlight possible moves
				moveList = selectedPiece1.get_moveList(blackPieces, whitePieces)
				if selectedBox2 == None:
					if selectedPiece1 in blackPieces:
						highlightMoves(moveList, GREENTINT)
					else:
						moveList = selectedPiece1.get_moveList(whitePieces, blackPieces)
						highlightMoves(moveList, REDTINT)
				else:
				#if a box is selected, move piece and eat the piece on the box if there's one, then reset all variables
					if selectedPiece1 in blackPieces and selectedBox2 in moveList:
						selectedPiece1.move(selectedBox2)
						if selectedPiece2 != None and selectedPiece1.coord == selectedPiece2.coord:
							selectedPiece2.dead()
						selectedPiece1 = None
						selectedPiece2 = None
						selectedBox1 = None
						selectedBox2 = None
						TURN += 1
					else:
					#if the piece cannot move to that box, replace first selections with the second selections
						selectedPiece1 = selectedPiece2
						selectedBox1 = selectedBox2
						selectedPiece2 = None
						selectedBox2 = None

		if selectedBox1 != None:
			highlightBox(selectedBox1[0], selectedBox1[1], CYANTINT)

		pygame.display.update()
		FPSCLOCK.tick(FPS)

def getLeftTopCoords(boxx, boxy):
	x = MARGIN + BOXSIZE * boxx
	y = MARGIN + BOXSIZE * boxy

	return (x, y)

def getBoxAtPixel(mousex, mousey):
	for boxx in range(BOXNUM):
		for boxy in range(BOXNUM):
			x, y = getLeftTopCoords(boxx, boxy)
			boxRect = pygame.Rect(x, y, BOXSIZE, BOXSIZE)
			if boxRect.collidepoint(mousex, mousey):
				return boxx, boxy
	return None, None

def getBoxAtPosition(boxx, boxy):
	return (boxx, boxy)

def drawBoard():
	#draw out chessboard onto display surface
	half = BOXSIZE/2

	for boxx in range(BOXNUM):
		for boxy in range(BOXNUM):
			left, top = getLeftTopCoords(boxx, boxy)
			if (boxx + boxy) % 2 == 0:
				pygame.draw.rect(DISPLAYSURF, LIGHTGRAY, (left, top, BOXSIZE, BOXSIZE))
			else:
				pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left, top, BOXSIZE, BOXSIZE))

def generatePieces():
	whitePieces = [Piece(name, piece_type, image) for name, piece_type, image in zip(WPIECENAMES, WPIECETYPES, WPIECEIMG)]
	blackPieces = [Piece(name, piece_type, image) for name, piece_type, image in zip(BPIECENAMES, BPIECETYPES, BPIECEIMG)]

	for i in range(2):
		for j in range(BOXNUM):
			whitePieces[i*BOXNUM + j].coord = (j, BOXNUM - (i + 1))

	for i in range(2):
		for j in range(BOXNUM):
			blackPieces[i*BOXNUM + j].coord = (j, i)

	return whitePieces, blackPieces

def drawPieces(whitePieces, blackPieces):
	#Need to add resizing later
	allPieces = whitePieces + blackPieces

	for piece in allPieces:
		if piece.state == 1:
			x, y = piece.coord
			image = pygame.image.load(piece.image)
			image = pygame.transform.smoothscale(image, (int(BOXSIZE), int(BOXSIZE)))
			DISPLAYSURF.blit(image, getLeftTopCoords(x, y))


def generateBoardData(whitePieces, blackPieces):
	board = []
	for boxx in range(BOXNUM):
		board.append([])
		for boxxy in range(BOXNUM):
			board[boxx].append(0)

	for piece in whitePieces:
		if piece.state == 1:
			x, y = piece.coord
			board[x][y] = 1

	for piece in blackPieces:
		if piece.state == 1:
			x, y = piece.coord
			board[x][y] = 1

	return board

def getPieceAtBox(boxx, boxy, whitePieces, blackPieces):
	allPieces = whitePieces + blackPieces
	for piece in allPieces:
		if piece.coord == (boxx, boxy):
			return piece
	return None

def highlightBox(boxx, boxy, color):
	tempSurf = DISPLAYSURF.convert_alpha()
	left, top = getLeftTopCoords(boxx, boxy)
	pygame.draw.rect(tempSurf, color, (left, top, BOXSIZE, BOXSIZE))
	tempRect = tempSurf.get_rect()
	DISPLAYSURF.blit(tempSurf, tempRect)

def highlightMoves(moveList, color):
	tempSurf = DISPLAYSURF.convert_alpha()
	for move in moveList:
		left, top = getLeftTopCoords(move[0], move[1])
		pygame.draw.rect(tempSurf, color, (left, top, BOXSIZE, BOXSIZE))
	tempRect = tempSurf.get_rect()
	DISPLAYSURF.blit(tempSurf, tempRect)

if __name__ == "__main__":
	main()
















