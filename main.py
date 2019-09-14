import pynput
import time
from pynput.keyboard import Key, Controller
inp=open("key.txt", "r", encoding='utf-8').read()

time.sleep(5)

inp = inp.replace('highlight', '')

inp = inp.replace('0', '')
inp = inp.replace('1', '')
inp = inp.replace('2', '')
inp = inp.replace('3', '')
inp = inp.replace('4', '')
inp = inp.replace('5', '')
inp = inp.replace('6', '')
inp = inp.replace('7', '')
inp = inp.replace('8', '')
inp = inp.replace('9', '')

inp = inp.replace('<span wordnr="" class="">', '')
inp = inp.replace('</span>', '')

for c in inp:
	time.sleep(0.10)
	keyboard = Controller()
	keyboard.press(c)
	keyboard.release(c)

# print(inp.encode('utf-8'))
# kiến trúc 