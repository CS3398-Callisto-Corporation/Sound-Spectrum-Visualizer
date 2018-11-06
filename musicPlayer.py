import folderNavigation

from tkinter import *
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk # pip install pillow
from time import time

pauseCondition = False
countCondition = False
increment = -1

class MusicPlayer:
    
    def __init__(self, master):

        # Load images
        folderImage = PhotoImage(file="icons/folder-search-icon.png")
        playImage = PhotoImage(file="icons/play-icon.png")
        startImage = PhotoImage(file="icons/start-icon.png")
        pauseImage = PhotoImage(file="icons/pause-icon.png")
        stopImage = PhotoImage(file="icons/stop-icon.png")
        nextImage = PhotoImage(file="icons/next-icon.png")
        prevImage = PhotoImage(file="icons/prev-icon.png")
        titleImage = PhotoImage(file="icons/title-icon.png")

        # Parent Widget
        self.master = master
        master.title("Sound Spectrum Visualizer Music Player")
        master.resizable(0,0)

        #Drop down menu
        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label="Open", command = self.choose)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        root.config(menu=self.menubar)

        # Multiple frames
        self.top = Frame(root)
        #self.top.config(bg="white")
        self.bottom = Frame(root)
        #self.bottom.config(bg="white")
        self.middle = Frame(root)
        self.bottomVol = Frame(root)
        self.top.pack(side=TOP)
        self.middle.pack(side=TOP)
        self.bottomVol.pack(side=BOTTOM)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Top frame includes text box and labels
        self.title = Label(master, text="Sound Spectrum Visualizer Music Player")
        self.title.config(image=titleImage)
        self.title.image = titleImage
        self.title.pack(in_=self.top)

        self.listSongTitle = Label(master, text="Song List")
        self.listSongTitle.pack(in_=self.top)

        self.listSongBox = tkst.ScrolledText(state='disabled',width=40, height=10)
        self.listSongBox.pack(in_=self.top)

        self.currentSongTitle = Label(master, text="Playing:")
        self.currentSongTitle.pack(in_=self.middle,side=LEFT)

        self.currentSong = Label(master)
        self.currentSong.pack(in_=self.middle,side=LEFT)

        '''self.textBox = Text(state='disabled', width=25, height=10)
        self.textBox.configure(state='normal')
        self.textBox.insert(INSERT, "Current Song: ")
        self.textBox.configure(state='disabled')
        self.textBox.pack(in_=self.top,side=LEFT)
        '''

        # Bottom frame includes buttons

        ''' Added drop down file menu instead
        self.choose_button = Button(master,text="Choose Folder", command = self.choose)
        self.choose_button.config(image = folderImage)
        self.choose_button.image = folderImage
        '''
        
        self.start_button = Button(master,text="Start Music Player", command = self.load)
        self.start_button.config(image = startImage)
        self.start_button.image = startImage

        self.play_button = Button(master, text="Play", command=self.playSong)
        self.play_button.config(image = playImage)
        self.play_button.image = playImage

        self.pause_button = Button(master, text="Pause", command=self.pauseSong)
        self.pause_button.config(image = pauseImage)
        self.pause_button.image = pauseImage

        self.stop_button = Button(master, text="Stop", command=self.stopSong)
        self.stop_button.config(image = stopImage)
        self.stop_button.image = stopImage
        
        self.next_button = Button(master, text="Next", command=self.next)
        self.next_button.config(image = nextImage)
        self.next_button.image = nextImage

        self.prev_button = Button(master, text="Prev", command=self.prev)
        self.prev_button.config(image = prevImage)
        self.prev_button.image = prevImage

        #Pack buttons
        
        #self.choose_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        
        self.start_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.start_button.configure(state=DISABLED)

        self.play_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.play_button.configure(state=DISABLED)
        
        self.pause_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.pause_button.configure(state=DISABLED)

        self.stop_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.stop_button.configure(state=DISABLED)

        self.prev_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.prev_button.configure(state=DISABLED)

        self.next_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        self.next_button.configure(state=DISABLED)

        #Volume Bar
        self.volLabel = Label(root, text="Volume")
        self.volLabel.pack(in_=self.bottomVol,side=LEFT)
        
        self.volumeV = DoubleVar() #Variable to hold volume 
        self.volumeV.set(.5)
        
        self.volBar = Scale(master, from_=0, to=1, variable=self.volumeV,orient=HORIZONTAL, showvalue=0, resolution=.01, command=self.updateVol)
        self.testLabel = Label(root, textvariable=self.volumeV)
        self.testLabel.pack(in_=self.bottomVol, side=RIGHT)
        self.volBar.pack(in_=self.bottomVol,side=LEFT)

        #Song Time
        self.timeLabel = Label(root, text='')
        self.timeLabel.pack(in_=self.middle, side=RIGHT)
        self.countLabel = Label(root, text='')
        self.countLabel.pack(in_=self.middle,side=RIGHT)
        
        

    # Calls the choose folder from folderNavigation
    def choose(self):
         folderNavigation.chooseFolder()
         self.start_button.configure(state=NORMAL)
    # Calls startMusicPlayer from folderNavigation
    def load(self):
        folderNavigation.startMusicPlayer()
        self.displayListOfSongs()
        self.writeCurrentSong()
        self.resetCountLabel()
        self.updateTimeLabel()
        self.play_button.configure(state=NORMAL)
        self.pause_button.configure(state=NORMAL)
        self.stop_button.configure(state=NORMAL)
        self.next_button.configure(state=NORMAL)
        self.prev_button.configure(state=NORMAL)
        self.start_button.configure(state=DISABLED)
    # Calls nextSong from folderNavigation                              
    def next(self):
        folderNavigation.nextSong()
        self.writeCurrentSong()
        self.updateTimeLabel()
        
    # Calls prevSong from folderNavigation    
    def prev(self):
        folderNavigation.prevSong()
        self.writeCurrentSong()
        self.updateTimeLabel()
        
    # Calls playSong from folderNavigation      
    def playSong(self):
        global pauseCondition
        if pauseCondition:
            pauseCondition = False
            folderNavigation.unPause()
            self.incrementCountLabel()
        else:
            self.resetCountLabel()
            folderNavigation.play()
            self.incrementCountLabel()
    # Calls stop from folderNavigation    
    def stopSong(self):
        global increment
        increment = -1
        self.resetCountLabel()
        folderNavigation.stop()
    # Calls pause from folderNavigation 
    def pauseSong(self):
        global pauseCondition
        pauseCondition = True
        folderNavigation.pause()
        
    # Writes currentSong to text box 
    def writeCurrentSong(self):
        currentSong = folderNavigation.currentSong()
        self.currentSong.config(text=currentSong)
        
    # Displays list of songs loaded
    def displayListOfSongs(self):
        self.listSongBox.configure(state='normal')
        for songs in folderNavigation.getListSongs():
            self.listSongBox.insert(INSERT, songs + "\n")
        self.listSongBox.configure(state='disabled')

    #Update Volume in real time
    def updateVol(self,_=None):
        folderNavigation.setVolume(self.getVol())

    def getVol(self):
        return self.volumeV.get()

    #Functions dealing with song length
    def getLengthOfSong(self):
        return folderNavigation.getLengthFile()

    def getMinutes(self):
        m = int(self.getLengthOfSong()/60)
        return m

    def getSeconds(self):
        m = self.getMinutes()
        s = int(self.getLengthOfSong()-(60*m))
        return s

    def getTimeString(self):
        min_sec = "/"+str(self.getMinutes())+":"+str(self.getSeconds())
        return min_sec

    def updateTimeLabel(self):
        self.timeLabel.config(text=self.getTimeString())

    
    def incrementCountLabel(self):
        def counter():
            global increment
            if pauseCondition or increment > self.getLengthOfSong():
                return
            self.countLabel.config(text=str(increment))
            increment+=1
            self.countLabel.after(1000, self.incrementCountLabel())
        counter()
        
    def resetCountLabel(self):
        self.countLabel.config(text="0:0")
        
        
            
       
        
root = Tk()
musicPlayer = MusicPlayer(root)
root.mainloop()

