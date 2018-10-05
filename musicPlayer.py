import folderNavigation

from tkinter import *
from tkinter.filedialog import askdirectory

pauseCondition = False

class MusicPlayer:
    
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        self.label = Label(master, text="Sound Spectrum Visualiser Music Player")
        self.label.pack()

        self.textBox = Text(width=70, height=2)
        self.textBox.insert(INSERT, "Current Song: ")
        self.textBox.pack()

        self.choose_button = Button(master,text="Choose Folder", command = self.choose)
        self.choose_button.pack()
        
        self.start_button = Button(master,text="Start Music Player", command = self.load)
        self.start_button.pack()

        self.play_button = Button(master, text="Play", command=self.playSong)
        self.play_button.pack()

        self.pause_button = Button(master, text="Pause", command=self.pauseSong)
        self.pause_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stopSong)
        self.stop_button.pack()

        self.next_button = Button(master, text="Next", command=self.next)
        self.next_button.pack()

        self.prev_button = Button(master, text="Prev", command=self.prev)
        self.prev_button.pack()

    # Calls the choose folder from folderNavigation
    def choose(self):
         folderNavigation.chooseFolder()
    # Calls startMusicPlayer from folderNavigation
    def load(self):
        folderNavigation.startMusicPlayer()
        self.writeCurrentSong()
    # Calls nextSong from folderNavigation                              
    def next(self):
        folderNavigation.nextSong()
        self.writeCurrentSong()
    # Calls prevSong from folderNavigation    
    def prev(self):
        folderNavigation.prevSong()
        self.writeCurrentSong()
        
    # Calls playSong from folderNavigation      
    def playSong(self):
        global pauseCondition
        if pauseCondition:
            pauseCondition = False
            folderNavigation.unPause()
        else:
            folderNavigation.play()
    # Calls stop from folderNavigation    
    def stopSong(self):
        folderNavigation.stop()
    # Calls pause from folderNavigation 
    def pauseSong(self):
        global pauseCondition
        pauseCondition = True
        folderNavigation.pause()
        
    # Writes currentSong to text box 
    def writeCurrentSong(self):
        currentSong = folderNavigation.currentSong()
        self.textBox.delete('1.0', END)
        self.textBox.insert(INSERT, "Current Song: " + currentSong)
        
        

root = Tk()
my_gui = MusicPlayer(root)
root.mainloop()

