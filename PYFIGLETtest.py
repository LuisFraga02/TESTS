import pyfiglet
word = "luis" #input("Enter a word to be BIG: ")
#print(pyfiglet.figlet_format(word))
fig = pyfiglet.Figlet()
#print(fig.getFonts())
for font in fig.getFonts():
    print(font+ '\n' + pyfiglet.figlet_format(word,font= font, justify = "center") + '\n')
#* fontes não horriveis
#*slant
#*starwars