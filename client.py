import requests



def startGame():
    x=input('Select x from 0-9')
    y=input('Select y from 0-9')


    r = requests.get('http://localhost:8000', str(x) + "&y=" + str(y))
    print(r.url)

startGame()