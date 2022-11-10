import webbrowser

import pystray
import requests
from PIL import Image
from win10toast_click import ToastNotifier

#! pillow deu uma problema pq eu mudei de pasta e tem q colocar esse "r" antes do caminho inteiro da imagem
image = Image.open(r'C:\Users\luisd\Desktop\Projetinhos\MINI_TESTS\assets\lubot.png')
bravePATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
icoPATH = r"C:\Users\luisd\Desktop\Projetinhos\MINI_TESTS\assets\lubot.ico"


##########API TOAST##########
toast = ToastNotifier()
def toastjoke():
    #* usei o jokeAPI pq já tinha feito um teste com ela
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()
    print("JOKE")
    print("="*50)
    print(f"id: {joke['id']}\ntype : {joke['type']}\nsetup: {joke['setup']}\npunchline: {joke['punchline']}")
    print("="*50)
    toast.show_toast(f"PIADA DO LUBOT | [ id: {joke['id']}-type : {joke['type']} ]", f"setup: {joke['setup']}\npunchline: {joke['punchline']}\n\n", icon_path=icoPATH, duration=30,callback_on_click=toastClickJoke)

##########API TOAST##########
##########toastTEST##########
def toastClick():
    print('clicou no toast')
def toastClickJoke():
    print('clicou no joke toast')
    
toast = ToastNotifier()
def toastShow():
    #! pillow deu uma problema pq eu mudei de pasta e tem q colocar esse "r" antes do caminho inteiro da imagem
    
    toast.show_toast("MENSAGEM DO LUBOT", "teste de toast", icon_path=icoPATH , duration=10,callback_on_click=toastClick)
##########toastTEST##########

##########pystray##########
def OI():
    print('OI')

def openBrave():
    try:
        print('Abrindo o Brave')
        webbrowser.get(bravePATH).open('https://www.google.com.br')
    except Exception:
        print('Erro ao abrir o Brave')

def exit(icon):
    icon.visible = False
    icon.stop()

icon = pystray.Icon('name', image, menu=pystray.Menu(
    pystray.MenuItem('OI', OI),
    pystray.MenuItem('Exit', exit),
    pystray.MenuItem('Abrir o Brave', openBrave),
    pystray.MenuItem('toastshow', toastShow),
    pystray.MenuItem('toast joke', toastjoke),
    pystray.MenuItem('submenu', pystray.Menu(
        pystray.MenuItem('subitem1', OI),
        pystray.MenuItem('subitem2', OI),
    )),
))
icon.run()
##########pystray##########


