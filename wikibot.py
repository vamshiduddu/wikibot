import pyttsx3 as py
import datetime
import speech_recognition as sr
import wikipedia
import urllib.request
import os

engine = py.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices') 

#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
	hour =int(datetime.datetime.now().hour)
	if(hour>=0 and hour<12):
		speak("Good Morning!")
	elif(hour>=12 and hour<18):
		speak("Good Afternoon! ")
	else:
		speak("Good Evening!")
	speak("Im wiki bot how may i help you today")



def navigate():
	r= sr.Recognizer()
	with sr.Microphone() as source:
		print("Tell me what you want to search on wikipedia ?")
		r.pause_threshold=1
		audio = r.listen(source)
	try:
		print("please wait while i memorise..")
		result = r.recognize_google(audio,language='en-in')
		print(f"You said:{result}\n")
		speak(result)


	except Exception as e:
		#print(e)
		#print("please say that again")
		#speak("please say that again")
		return "None"
	return result
def image(query):
	query = query.replace(" ","_".lower())
	page_image = wikipedia.page(query)
	image_down_link = page_image.images[5]

	urllib.request.urlretrieve(image_down_link , "loc.jpg")
	os.startfile("loc.jpg") 

if __name__ == '__main__':
	wishme()
	query = navigate().lower()
	if "wikipedia "  in query:
		speak("searching in wiki hang on...!")
		query = query.replace("wikipedia ","")
		result =wikipedia.summary(query,sentences=2)
		image(query)
		speak("According to wiki..")
		page_image = wikipedia.page(query)
		image_down_link = page_image.images[0]
		urllib.request.urlretrieve(image_down_link , "loc.jpg")
		print(result)
		speak(result)
	elif '' in query:
		try:

			speak("searching in wiki hang on...!")
			query = query.replace("","")
			result =wikipedia.summary(query,sentences=3)
			speak("According to wiki..")
			print(result)
			image(query)
			speak(result)
		except Exception as e:
			speak("Im sorry i could not found your query")
	else:
		speak("Im sorry i could not found your query")
