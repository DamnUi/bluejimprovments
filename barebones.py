#Fast work for tommorow
import pyautogui
import time
import keyboard
import sys, os
import pygetwindow as gw


#attack shift+enter hotkey to compile_c

hotkey = 'shift+enter'

keyboard.add_hotkey(hotkey, lambda: compile_c_and_leave())



lines = r'linesproj.png'
succesful_compile = r'scompile.png'
bird_img = r'bird.png'
#if files arent found in directory show an error 
try:
    os.path.isfile(lines)
    os.path.isfile(succesful_compile)
    os.path.isfile(bird_img)
except:
    print("Error: Files not found, Try checking your install directory")



def find_bird():
    bird_pos = pyautogui.locateOnScreen(bird_img)
    return bird_pos

def click_bird():
    bird_pos = find_bird()
    pyautogui.moveTo(bird_pos)
    pyautogui.click()
    
def find_project_and_right_click():
    #find self.lines on screen
    lines_pos = pyautogui.locateOnScreen(lines)
    #ss
    pyautogui.screenshot('lines.png', region=lines_pos)
    #move to 
    pyautogui.moveTo(lines_pos)
    #click
    pyautogui.click(button='right')    

def compile_c_and_leave():
    time.sleep(0.5)
    click_bird()
    #press and release ctrl + k twice
    keyboard.press_and_release('ctrl+k')
    keyboard.press_and_release('ctrl+k')
    
    time.sleep(1)
    compile_pos = pyautogui.locateOnScreen(succesful_compile)
    if compile_pos == None:
        print("Failed to compile, try again")
    else:
        print("Successfully compiled")
        keyboard.press_and_release('ctrl+w')
        bluej_main = gw.getWindowsWithTitle('BlueJ:')[0]
        #get title
        bluej_title = bluej_main.title
        print(bluej_title)
        bluej_main.maximize()
        #activate
        bluej_main.restore()
        bluej_main.maximize()
        bluej_main.activate()
        time.sleep(1)
        find_project_and_right_click()
            
    

        
keyboard.wait('esc')