import pyautogui #imports pyautogui
import keyboard #imports keyboard


def autoclicker(): #declares the function
    start_clicking = False
    count = 0
    while True: #makes a infinite loop
        if start_clicking:
            pyautogui.click() #makes your mouse click
            count += 1
        if keyboard.is_pressed('x'): #detects if b is pressed
            print("x pressed")
            break #if b is detected it breaks the loop
        if keyboard.is_pressed('s'): #detects if s is pressed
            start_clicking = True
            print("s pressed, start_clicking = " + str(start_clicking))
        if keyboard.is_pressed('p'): #detects if p is pressed
            start_clicking = False
            print("p pressed, start_clicking = " + str(start_clicking))
    print("clicked " + str(count) + " times")


autoclicker()