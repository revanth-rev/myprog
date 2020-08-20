import pyttsx3
import os

pyttsx3.speak("I am your personal assistant!! If you want to open anything, just say the word!")

while True:
	print("Please specify your requirements : "  , end='')
	p = input()

	if (("open" in p) or ("run" in p))  and ("chrome" in p):
	  os.system("chrome")

	elif (("open" in p) or ("run" in p))  and (("edge" in p) or ("microsoft edge" in p)):
	  os.system("msedge")

	elif (("open" in p) or ("run" in p))  and ("internet explorer" in p):
	  os.system("iexplore")

	elif (("open" in p) or ("run" in p) or  ("execute" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif (("open" in p) or ("run" in p) or  ("execute" in p)) and  (("explorer" in p) or ("file explorer" in p) ) :
	  os.system("explorer")

	elif (("open" in p) or ("run" in p))  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")

	elif (("open" in p) or ("run" in p) or  ("execute" in p)) and  (("calculator" in p) or ("calci" in p) ) :
	  os.system("calc")

	elif (("open" in p) or ("run" in p) or  ("execute" in p)) and  (("paint" in p) or ("mspaint" in p) ) :
	  os.system("mspaint")

	elif (("open" in p) or ("run" in p) or  ("execute" in p)) and  ("task manager" in p) :
	  os.system("taskmgr")

	elif (("open" in p) or ("run" in p) or  ("execute" in p)) and ("sublime text" in p):
	  os.system("sublime_text")

	elif  ("exit" in p)  or ("quit" in p) or ("close" in p) or ("Thank You" in p) or ("stop" in p):
	  break

	else:
	  print("dont support")



