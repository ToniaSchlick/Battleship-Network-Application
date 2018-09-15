import socket
import httplib


#Stablish connection between client and server using TCP.
def stablishConnection():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind (('172.20.1.254', 8080))

    s.listen(1)

    conn, addr = s.accept()

    data = conn.recv(64)
    print("Received request: '" + data.decode('utf-8')+"'")

    conn.send("Yes".encode('utf-8'))

    conn.close()

#create initial board and modificate the own_board.txt
def createBoard(x, y):

    line=[0 for i in range(10)]
    line[0]="CCCCC_____\n"
    line[1]="BBBB______\n"
    line[2]="SSS_______\n"
    line[3]="D_________\n"
    line[4]="D_________\n"
    line[5]="__________\n"
    line[6]="__________\n"
    line[7]="__________\n"
    line[8]="__________\n"
    line[9]="__________\n"

    #Modificate the own_board.txt with the initial board
    with open("own_board.txt", 'r+') as files:
        files.writelines(line)

    #Read every line in the own_board.txt    
    with open("own_board.txt", 'r+') as files:
        lines=files.readlines()
        if lines[x][y]=="S":#check if something was hit (testing)
            print "Hit"
            


createBoard(2,2)# Random number for testing

