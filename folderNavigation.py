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
numWav = 0


 # this function prompts the user to choose a folder that contains the music they wish to listen to
def chooseFolder():
    global numWav
    directory = askdirectory()
    os.chdir(directory)
    
    for files in os.listdir(directory):
        if files.endswith(".wav"):
            numWav+=1
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
    #if-else prevent out of bounds and ability to rotate thru songs
    if index == (numWav-1):
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    else:
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()

def prevSong():
    global index
    #if-else prevent out of bounds and ability to rotate thru songs
    if index == 0:
        index = (numWav-1)
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    else:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    
#added pause/unpause to differ from stop    
def pause():
    pygame.mixer.music.pause()

def unPause():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()

def currentSong():
    return listofsongs[index]

def getListSongs():
    return listofsongs
    
    
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
