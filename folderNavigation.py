# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:11:51 2018

@author: Wes Nicol


This file contains the play/pause and next/prev song buttons implementation (not GUI, just functionality)
"""

import os
from tkinter.filedialog import askdirectory
import pygame
from time import sleep

listofsongs = []
index = 0


 # this function prompts the user to choose a folder that contains the music they wish to listen to
def chooseFolder(): 
    directory = askdirectory()
    os.chdir(directory)
    
    for files in os.listdir(directory):
        if files.endswith(".wav"):
            listofsongs.append(files)
            print(files)
    
    
# this function initializes the music player and automaically loads up the first song in the list    
def startMusicPlayer():
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])

# when called, this function plays the currently selected song
def play():
    pygame.mixer.music.play()
    

    
    
def nextSong():
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevSong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    
def pause():
    pygame.mixer.music.pause()
    
''' uncomment the below code to test the functionality of these functions (lol)
chooseFolder()
startMusicPlayer()


play()
sleep(3)
pause()
sleep(3)
nextSong()

 
root.mainloop()
'''
