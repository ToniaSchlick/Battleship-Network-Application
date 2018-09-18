import requests

def startGame():
    x=input('Select x from 0-9')
    y=input('Select y from 0-9')

    r = requests.post('http://localhost:8000', "x=" + str(x) + "&y=" + str(y))
    print(r.url)

startGame()