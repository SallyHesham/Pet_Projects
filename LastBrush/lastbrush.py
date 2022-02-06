from pynput.keyboard import Listener, Key, Controller

# to input keys later on
keyboard = Controller()

# for saving the keys
key1 = None
key2 = None
key3 = None

# activates when a key is pressed
def on_press(key):
    global key1, key2, key3
# saves 3 last pressed keys
    key3 = key2
    key2 = key1
    key1 = key
    print(key1, key2, key3)
# escape method
    if key == Key.esc:
        quit()
# prevents traceback at next line
    elif key2 is None:
        pass
# when e is pressed twice, presses the key pressed before
    elif key1.char == key2.char == 'e':
        print('YOSH!!!')
        keyboard.press(key3)
        keyboard.release(key3)

# activates listener (nothing executes after)
with Listener(on_press=on_press) as listener:
    listener.join()
