import folderNavigation

from tkinter import *
from tkinter.filedialog import askdirectory


class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        self.label = Label(master, text="Sound Spectrum Visualiser Music Player")
        self.label.pack()

        '''self.label = Label(master, text=listofsongs[index])
        self.label.pack()'''

        self.choose_button = Button(master,text="Choose Folder", command = self.choose)
        self.choose_button.pack()
        
        self.start_button = Button(master,text="Start Music Player", command = self.load)
        self.start_button.pack()

        self.play_button = Button(master, text="Play", command=self.playSong)
        self.play_button.pack()

        self.pause_button = Button(master, text="Stop", command=self.stopSong)
        self.pause_button.pack()

        self.next_button = Button(master, text="Next", command=self.next)
        self.next_button.pack()

        self.prev_button = Button(master, text="Prev", command=self.prev)
        self.prev_button.pack()


    def choose(self):
         folderNavigation.chooseFolder()
    
    def load(self):
        folderNavigation.startMusicPlayer()
                                   
    def next(self):
        folderNavigation.nextSong()
        
    def prev(self):
        folderNavigation.prevSong()
        
    def playSong(self):
        folderNavigation.play()
        
    def stopSong(self):
        folderNavigation.pause()
        
'''Commented out the code to test the buttons
root = Tk()
my_gui = MusicPlayer(root)
root.mainloop()
'''
