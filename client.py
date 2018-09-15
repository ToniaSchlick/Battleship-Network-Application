import socket
import httplib


#Stablish connection between client and server using TCP.
def stablishConnection():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect (('172.20.1.254', 8080))

    s.send("Are you there?".encode('utf-8'))

    data = s.recv(64)
    print("Received response: '" + data.decode('utf-*')+"'")

    s.close()

def startGame():
    x=userInputX()
    y=userInputY()

    URL=("http://172.20.1.254?x=" + str(x) + "&y=" + str(y))
    print(URL)
    
#Ask for user input x-coordinate.   
def userInputX():
    i=0
    while i==0:#while x-coordinate is not inside the bounds.

        #Ask for x-coordinates input.
        xC=input("Choose x coordinate between 0 and 9: ")
        type(xC)
        
        if xC<=9 and xC>=0: #Check if the input is inside the bounds.
            i=1
        else: #If input is not inside bounds.
            print("The coordinate have to be between 0 and 9. Try again")
    return xC

#Ask for user input y-coordinate.
def userInputY():
    j=0
    while j==0:#while y-coordinate is not inside the bounds.
        #Ask for y-coordinates input.
        yC=input("Choose y coordinate between 0 and 9: ")
        type(yC)
        
        if yC<=9 and yC>=0: #Check if the input is inside the bounds.
            j=1
        else: #If input is not inside bounds.
            print("The coordinate have to be between 0 and 9. Try again")
    return yC


startGame()
