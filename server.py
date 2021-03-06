from http.server import BaseHTTPRequestHandler, HTTPServer
import json

STotal=0
CTotal=0
BTotal=0
RTotal=0
DTotal=0

class MyHandler(BaseHTTPRequestHandler):

        def set_header(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

        def do_GET(self):
                # Send response status code
                self.send_response(200)
                # Send headers
                self.wfile.write(bytes("<embed src=""own_board.txt"">", "utf-8"))
                print("Connection")

        def do_POST(self):
                # Send response status code
                self.send_response(200)

                # Send headers
                self.send_header('Content-type','text/html')
                self.end_headers()
                
                # Extract move from http post
                self.data_string = self.rfile.read(int(self.headers['Content-Length']))
                data = json.loads(self.data_string)
                print ("{}".format(data))
                print (data['x'], data['y'])

                # Random number for testing
                # until be able to read the actual desire values that were send
                message = createBoard(data['x'], data['y'])
                
                # Write content as utf-8 data and
                # Send message back to client
                self.wfile.write(bytes(message, "utf8"))
                
                return
                

def run(server_class=HTTPServer, handler_class=MyHandler, port=80):
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()


def initializeBoard():
        line=[0 for i in range(10)]
        line[0]="CCCCC_____\n"
        line[1]="BBBB______\n"
        line[2]="SSS_______\n"
        line[3]="RRR_______\n"
        line[4]="D_________\n"
        line[5]="D_________\n"
        line[6]="__________\n"
        line[7]="__________\n"
        line[8]="__________\n"
        line[9]="__________\n"

        
        
        #Modificate the own_board.txt with the initial board
        with open("own_board.txt", 'r+') as files:
                files.writelines(line)

def createBoard(x, y):

        global STotal
        global CTotal
        global BTotal
        global RTotal
        global DTotal

        if(x.isnumeric()==0 or y.isnumeric()==0):
                                message="HTTP Bad Request"
                                return message
                         # x or y ou of bounds
        if int(x)>9 or int(y)>9:
                                message="HTTP Not Found"
                                return message
        
        #Read every line in the own_board.txt    
        with open("own_board.txt", 'r+') as files:
                lines=files.readlines()
                s= list(lines[int(x)])
                
                # Missing the HTTP bad request response
                # Thinking on using the isnumeric() function to check for Bad Request

                # Location have alreay been fire
                if lines[int(x)][int(y)]=="X" or lines[int(x)][int(y)]=="O":
                                message="HTTP Gone"

                # If the Submarine was hit
                elif lines[int(x)][int(y)]=="S":
                                STotal=STotal+1 #Increase number of time that Submarine have been hit
                                
                                s[int(y)]='O'
                                lines[int(x)]="".join(s)
                                
                                if STotal==3:
                                                message="Hit=1\&sink=S"
                                else:
                                                message="Hit=1"

                # If the Carrier was hit        
                elif lines[int(x)][int(y)]=="C":
                                CTotal=CTotal+1 #Increase number of time that Carrier have been hit

                                s[int(y)]='O'
                                lines[int(x)]="".join(s)
                                
                                if CTotal==5:
                                                message="Hit=1\&sink=C"
                                else:
                                                message="Hit=1"

                # If the Battleship was hit        
                elif lines[int(x)][int(y)]=="B":
                                BTotal=BTotal+1 #Increase number of time that Battleship have been hit

                                s[int(y)]='O'
                                lines[int(x)]="".join(s)
                                
                                if BTotal==4:
                                                message="Hit=1\&sink=B"
                                else:
                                                message="Hit=1"

                # If the Cruiser was hit
                elif lines[int(x)][int(y)]=="R":
                                
                                RTotal=RTotal+1 #Increase number of time that Cruiser have been hit

                                s[int(y)]='O'
                                lines[int(x)]="".join(s)
                                
                                if RTotal==3:
                                                message="Hit=1\&sink=R"
                                else:
                                                message="Hit=1"

                # If one of the Destroyers was hit
                elif lines[int(x)][int(y)]=="D":
                                
                                DTotal=DTotal+1 #Increase number of time that Destroyers have been hit

                                s[int(y)]='O'
                                lines[int(x)]="".join(s)
                                
                                if DTotal==1 or DTotal==2:
                                                message="Hit=1\&sink=D"
                                else:
                                                message="Hit=1"
                                                
                 # If nothing was hit (miss)
                else:
                                s[int(y)]='X'
                                lines[int(x)]="".join(s)
                                message="Hit=0"

                #If all boats were sink. Game over
                if STotal==3 and CTotal==5 and BTotal==4 and RTotal==3 and DTotal==2:
                                
                                message="You Won! Game Over"
                
           
                # Updated own board
                with open("own_board.txt", 'r+') as files:
                                files.writelines(lines)

        # Return the response message that is going to be send to the client
        return message


initializeBoard()
run()










