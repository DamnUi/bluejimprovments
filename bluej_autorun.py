import pyautogui
import time
import keyboard
import os, sys
import re
import pygetwindow as gw

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Bluej:
    def __init__(self, test_instance=False, space_to_check_for=100) -> None:
        self.space_to_check_for = space_to_check_for
        self.test_instance = test_instance
        self.updated_pos = None
        self.hypen = r'D:\.Python\StandAlone\.BLUEJAUTOSHIT\2023-08-21-15-42-51.png'
        self.bird_img = r'D:\.Python\StandAlone\.BLUEJAUTOSHIT\2023-08-21-15-00-39.png'
        self.lines = r'D:\.Python\StandAlone\.BLUEJAUTOSHIT\2023-08-21-20-54-50.png'
        self.succesful_compile = r'D:\.Python\StandAlone\.BLUEJAUTOSHIT\2023-08-21-21-07-00.png'
        self.found_project_name = None
        self.found_code_name = None
        if self.test_instance:
            time.sleep(3)
            
        
        
    def find_bird(self):
        bird_img = self.bird_img
        bird_pos = pyautogui.locateOnScreen(bird_img)
        return bird_pos
    
    def click_bird(self):
        bird_pos = self.find_bird()
        pyautogui.moveTo(bird_pos)
        pyautogui.click()
        
    def take_ss(self):
        # Test Function pretty much
        # screen shot the pos from find_bird
        self.bird_pos = self.find_bird()
        pyautogui.screenshot('test.png', region=self.bird_pos)
        return("Success")
        # save   
        
    
    def text_getr(self):
        bird_pos = self.find_bird()
        #edit width value to increase
        self.updated_pos = (23, bird_pos[1], self.space_to_check_for, bird_pos[3]) # 23 helps remove it for easier ocr, self.space...for is the width of the text box so it can get the full text to search later
        pyautogui.screenshot('text.png', region=self.updated_pos)
        return("Success")
    # depreciated but still needed, gets all text from screenshot
    
    def precise_text_img_getr(self):
        bird_pos = self.find_bird() # just keeping it ready
        self.hyp_pos = pyautogui.locateOnScreen(self.hypen, region=self.updated_pos)
        og_value = self.hyp_pos[0]
        pyautogui.screenshot('JUSTPLS.png', region=(23, self.hyp_pos[1]-3, og_value-20, self.hyp_pos[3]+4))
        print(self.hyp_pos)

    # Gets only TEXT from screenshot, no hypen also, using hypen
        
    def filter_class_name(self, name):
        filtered_name = re.sub(r'[^a-zA-Z0-9_]', '', name)
        filtered_name = re.sub(r'r^\s+|\s+$', '', filtered_name)
        return filtered_name

    
    def ocr_by_tes(self):
        # if text.png is not found, run text_getr
        try:
            if os.path.isfile('text.png'):
                pass
        except:
            self.text_getr()
        

        image = Image.open('JUSTPLS.png')
        image = image.resize((image.width*3, image.height*3))
        text = pytesseract.image_to_string(image, lang='eng', config='--psm g1')
        text = self.filter_class_name(text)

        return(text)
    
    def compile_c_and_leave(self):
        self.click_bird()
        #press and release ctrl + k twice
        keyboard.press_and_release('ctrl+k')
        keyboard.press_and_release('ctrl+k')
        
        time.sleep(1)
        compile_pos = pyautogui.locateOnScreen(self.succesful_compile)
        if compile_pos == None:
            print("Failed to compile, quitting here")
            sys.exit()
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
            self.find_project_and_right_click()
            
            
        
            
        
    
    def find_project_and_right_click(self):
        #find self.lines on screen
        lines_pos = pyautogui.locateOnScreen(self.lines)
        #ss
        pyautogui.screenshot('lines.png', region=lines_pos)
        #move to 
        pyautogui.moveTo(lines_pos)
        #click
        pyautogui.click(button='right')
                

            



        
        
        
# write a test
if __name__ == '__main__':
    bluej = Bluej(test_instance=True)
    # bluej.precise_text_img_getr()
    print(bluej.compile_c_and_leave())

    