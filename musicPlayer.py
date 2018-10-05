import folderNavigation

from tkinter import *

pauseCondition = False

class MusicPlayer:
    
    def __init__(self, master):

        # Parent Widget
        self.master = master
        master.title("Music Player")

        # Multiple frames
        self.top = Frame(root)
        self.bottom = Frame(root)
        self.top.pack(side=TOP)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Top frame includes text box and labels
        self.label = Label(master, text="Sound Spectrum Visualiser Music Player")
        self.label.pack(in_=self.top)

        self.textBox = Text(width=35, height=20)
        self.textBox.insert(INSERT, "Current Song: ")
        self.textBox.pack(in_=self.top,side=LEFT)
        
        self.listSongBox = Text(width=35, height=20)
        self.listSongBox.insert(INSERT, "----Song List---- \n")
        self.listSongBox.pack(in_=self.top,side=RIGHT)

        # Bottom frame includes buttons
        self.choose_button = Button(master,text="Choose Folder", command = self.choose)
        self.choose_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        
        self.start_button = Button(master,text="Start Music Player", command = self.load)
        self.start_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.start_button.configure(state=DISABLED)

        self.play_button = Button(master, text="Play", command=self.playSong)
        self.play_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.play_button.configure(state=DISABLED)

        self.pause_button = Button(master, text="Pause", command=self.pauseSong)
        self.pause_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.pause_button.configure(state=DISABLED)

        self.stop_button = Button(master, text="Stop", command=self.stopSong)
        self.stop_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.stop_button.configure(state=DISABLED)
        
        self.next_button = Button(master, text="Next", command=self.next)
        self.next_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.next_button.configure(state=DISABLED)

        self.prev_button = Button(master, text="Prev", command=self.prev)
        self.prev_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.prev_button.configure(state=DISABLED)
        

    # Calls the choose folder from folderNavigation
    def choose(self):
         folderNavigation.chooseFolder()
         self.start_button.configure(state=NORMAL)
    # Calls startMusicPlayer from folderNavigation
    def load(self):
        folderNavigation.startMusicPlayer()
        self.displayListOfSongs()
        self.writeCurrentSong()
        self.play_button.configure(state=NORMAL)
        self.pause_button.configure(state=NORMAL)
        self.stop_button.configure(state=NORMAL)
        self.next_button.configure(state=NORMAL)
        self.prev_button.configure(state=NORMAL)
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
        
    # Displays list of songs loaded
    def displayListOfSongs(self):
        for songs in folderNavigation.getListSongs():
            self.listSongBox.insert(INSERT, songs + "\n")
        
        
root = Tk()
musicPlayer = MusicPlayer(root)
root.mainloop()

