import pyttsx3

#* da pra adicionar mais vozes mas é meio complicado e não sei se é necessário
voice_engine = pyttsx3.init()
voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[0].id) #voz 0 femenina portugues
#voice_engine.setProperty('voice', voices[1].id) #voz 1 feminina ingles
fala = "bau tica bau bau"
voice_engine.say(fala)
voice_engine.runAndWait()

