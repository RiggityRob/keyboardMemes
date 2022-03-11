import pynput

def on_press(key):
	try:
		k = key.char  # single-char keys
	except:
		k = key.name  # other keys
	if k in ",":
            keyboard.press(pynput.keyboard.Key.ctrl)
            keyboard.press("2")
            keyboard.release(pynput.keyboard.Key.ctrl)
            keyboard.release("2")
	if k in ".":
            keyboard.press(pynput.keyboard.Key.ctrl)
            keyboard.press("3")
            keyboard.release(pynput.keyboard.Key.ctrl)
            keyboard.release("3")
	if k in "/":
		keyboard.press(pynput.keyboard.Key.ctrl)
		keyboard.press("6")
		keyboard.release(pynput.keyboard.Key.ctrl)
		keyboard.release("6")
	if k in "m":
		keyboard.press("b")
		keyboard.release("b")
	if k in "~":
		exit()
keyboard = pynput.keyboard.Controller()
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
