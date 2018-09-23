import requests
import json

def update(x, y):
        payload = {'x': x, 'y': y}
        r = requests.post('http://localhost:8000/opponent_board.html', data=json.dumps(payload))
        print(r.url)
        print(r.text)
def startGame(): 
	playing = True 
	while (playing == True): # Keep program running until the game is over
		print("")
		x=input('Select x from 0-9: ')
		y=input('Select y from 0-9: ')
		print("")
		
		payload = {'x': x, 'y': y}
		r = requests.post('http://localhost:8000', data=json.dumps(payload))
		print(r.url)
		print(r.text)
		if (r.text == "You Won! Game Over"):
			playing = False
		print("")
		opponentBoard(x,y,r)

def opponentBoard(x,y,r):
	if r.text=="Hit=1" or r.text=="Hit=1\&sink=S" or r.text=="Hit=1\&sink=C" or r.text=="Hit=1\&sink=B" or r.text=="Hit=1\&sink=R" or r.text=="Hit=1\&sink=D":
		#change opponent_board for O (hit)
		 
		with open("opponent_board.txt", 'r+') as files:
			
			lines=files.readlines()
			
			s= list(lines[int(x)])
			s[int(y)]='O'
			lines[int(x)]="".join(s)
			
			with open("opponent_board.txt", 'r+') as files:
				files.writelines(lines)
				
	elif r.text=="Hit=0":
		#change opponent_board for X (miss)
		with open("opponent_board.txt", 'r+') as files:
			
			lines=files.readlines()
			s= list(lines[int(x)])
			s[int(y)]='X'
			lines[int(x)]="".join(s)
			
			with open("opponent_board.txt", 'r+') as files:
				files.writelines(lines)

def initializeOpponent():
	line=[0 for i in range(10)]
	line[0]="__________\n"
	line[1]="__________\n"
	line[2]="__________\n"
	line[3]="__________\n"
	line[4]="__________\n"
	line[5]="__________\n"
	line[6]="__________\n"
	line[7]="__________\n"
	line[8]="__________\n"
	line[9]="__________\n"

	
	#Modificate the opponent_board.txt with the initial board
	with open("opponent_board.txt", 'r+') as files:
		files.writelines(line)
		
initializeOpponent()
startGame()
