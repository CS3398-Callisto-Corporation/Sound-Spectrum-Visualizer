# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:11:51 2018

@author: Wes Nicol


This file contains the play/pause and next/prev song buttons implementation (not GUI, just functionality)
"""
import testLiveGraph
import musicPlayer
import os
from tkinter.filedialog import askdirectory
import pygame
from time import sleep
import sound_tester

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
    #sound_tester.playSong(listofsongs[index])
    #testLiveGraph.openGraph()
    #musicPlayer.openGraph()
    
    
def nextSong():
    global index
    #if-else prevent out of bounds and ability to rotate thru songs
    if index == (numWav-1):
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        
        #starts visual spectrum graph window
        

        
        #uncomment below line to automatically play when prev song is selected
        #sound_tester.playSong(listofsongs[index])
    else:
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        
        #uncomment below line to automatically play when prev song is selected
        #sound_tester.playSong(listofsongs[index])

def prevSong():
    global index
    #if-else prevent out of bounds and ability to rotate thru songs
    if index == 0:
        index = (numWav-1)
        pygame.mixer.music.load(listofsongs[index])
        #pygame.mixer.music.play()
        
        #uncomment below line to automatically play when prev song is selected
        #sound_tester.playSong(listofsongs[index])
    else:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        #pygame.mixer.music.play()
        
        #uncomment below line to automatically play when prev song is selected
        
        #sound_tester.playSong(listofsongs[index])
    
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

def getVolume():
    return get_volume()

def setVolume(v):
    pygame.mixer.init()
    if v>=1:
        pygame.mixer.music.set_volume(1.0)
    elif v<=0:
        pygame.mixer.music.set_volume(0.0)
    else:
        pygame.mixer.music.set_volume(v)

def getRawLength():
    a = pygame.mixer.Sound(listofsongs[index])
    rawLength = a.get_length()
    return rawLength

def getLength():
    lengthSong = getRawLength()
    mins, secs = divmod(lengthSong,60)
    mins = round(mins)
    secs = round(secs)
    formattedLength = '{:02}:{:02d}'.format(mins, secs)
    return formattedLength
    

    
    
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
