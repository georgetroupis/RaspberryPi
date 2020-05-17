import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
sup = "sup"
TIME_UNIT = 1

DOT= TIME_UNIT
DASH = TIME_UNIT *3
GAP = TIME_UNIT
LETTER_GAP = TIME_UNIT *3
WORD_GAP = TIME_UNIT * 7 

def off():
    GPIO.output(18, False)

def on():
    GPIO.output(18, True)

def switch_Char (char):
    switcher = {
        'a' : '.-',
        'b' : '-...',
        'c' : '-.-.',
        'd' : '-..',
        'e' : ',',
        'f' : '..-.',
        'g' : '--.',
        'h' : '....',
        'i' : '..',
        'j' : '.---',
        'k' : '-.-',
        'l' : '.-..',
        'm' : '--',
        'n' : '-.',
        'o' : '---',
        'p' : '.--.',
        'q' : '--.-',
        'r' : '.-.',
        's' : '...',
        't' : '-',
        'u' : '..-',
        'v' : '...-',
        'w' : '.--',
        'x' : '-..-',
        'y' : '-.--',
        'x' : '--..',
        ' ' : ' '
        }
    return (switcher[char])
        

def ledOutput(morse):
    i = 0
    for char in morse:
        if char == '.':
            cur_time = time.time()
            while time.time() < cur_time + DOT:
                on()
            off()
            
        elif char == '-':
            cur_time = time.time()
            while time.time() < cur_time + DASH:
                on()
        off()
        
        if i != len(morse)-1:
            time.sleep(GAP)
        i +=1
        
phrase = "sup"

for char in phrase:
    if char == ' ':
        time.sleep(WORD_GAP)
    else:
        morse = switch_Char(char)
        ledOutput(morse)
        time.sleep(LETTER_GAP)
    
GPIO.output(18, False)

GPIO.cleanup()