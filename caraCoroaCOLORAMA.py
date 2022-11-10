import random
import colorama as c
#* fiz porque tinha visto o colorama no twitter e achei bonitinho pra ficar colorido
num = random.randint(1,2)
if num==1:
    print(c.Fore.GREEN,'cara')
    c.Fore.RESET
else:
    print(c.Fore.GREEN,'coroa')
    c.Fore.RESET
    
#!!!!!!!!!!!!!
c.Fore.RESET #* isso aqui é pra voltar a cor normal, se não o terminal fica verde pra sempre
#!!!!!!!!!!!!!