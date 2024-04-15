import pynput

mouse = pynput.mouse.Controller()

button = pynput.mouse.Button

def on_press(key):
	try:
		k = key.char  # single-char keys
	except:
		k = key.name  # other keys
	if k in ",":
            mouse.press(button.left)
	if k in ".":
            mouse.press(button.middle)
	if k in "~":
		exit()
keyboard = pynput.keyboard.Controller()
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
