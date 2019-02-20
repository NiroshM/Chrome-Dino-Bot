from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time

class Coordinates:
    dinosaur = (664, 498) #Coordinates of the top right pixel of the dino

def startGame():                           
    if resetImage() == 11926:
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')   

def jump():
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')

def resetImage():     
    box = (938, 474, 981, 512) #Coordinates of restart box, top left corner and bottom right coordinates
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(a.sum())
    return a.sum()

def cactusImage():                     
    box = (Coordinates.dinosaur[0] + 104, Coordinates.dinosaur[1], Coordinates.dinosaur[0] + 156, Coordinates.dinosaur[1] + 40) #Coordinates of cactus, top right corner and bottom left coordinates
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())          
    #print(a.sum())
    return a.sum()                        

pyautogui.click(938, 474)
while True:               
    startGame()            
    if(cactusImage() != 2327):
        jump()

       
               



                       


