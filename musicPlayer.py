import folderNavigation
import testLiveGraph
from time import sleep
from tkinter import *
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk # pip install pillow
from multiprocessing import Process
import threading



pauseCondition = False
updateTimeCondition = False
changeSongCondition = False
startCondition = False
count = 0


class MusicPlayer:
    
    def __init__(self, master):

        #root = mainMusicPlayer()
        
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
        #master.title("Sound Spectrum Visualizer Music Player") #this line gives an error with multiprocessing (but i think you can assign the name at the bottom of this file and it still works)
        master.resizable(0,0)


        '''#Drop down menu
        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label="Open", command = self.choose)
        self.filemenu.add_separator()
        #self.filemenu.add_command(label="Exit", command=root.destroy()) # this line was giving an error with multiprocessing
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.menubar) # this line was giving an error with multiprocessing'''

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

        
        #Clickable ListBox
        #self.listSongBoxTest = Listbox(self.top, width=20, height=10,)

        #self.scrollbar = Scrollbar(self.top, orient="vertical")
        #self.scrollbar.config(command=self.listSongBoxTest.yview)
        #self.scrollbar.pack(side="right", fill="y")
        #self.listSongBoxTest.config(yscrollcommand=self.scrollbar.set)
        #self.listSongBoxTest.pack(side="right")
        
        

        self.currentSongTitle = Label(master, text="Playing:")
        self.currentSongTitle.pack(in_=self.middle,side=LEFT)

        self.currentSong = Label(master)
        self.currentSong.pack(in_=self.middle,side=RIGHT)


        '''self.textBox = Text(state='disabled', width=25, height=10)
        self.textBox.configure(state='normal')
        self.textBox.insert(INSERT, "Current Song: ")
        self.textBox.configure(state='disabled')
        self.textBox.pack(in_=self.top,side=LEFT)
        '''

        # Bottom frame includes buttons
        
        self.choose_button = Button(master,text="Choose Folder", command = self.choose)
        self.choose_button.config(image = folderImage)
        self.choose_button.image = folderImage
            
        
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
        
        self.choose_button.pack(in_=self.bottom, side=LEFT, fill=BOTH, expand=True)
        
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
        self.volBar.pack(in_=self.bottomVol,side=LEFT)
        self.testLabel.pack(in_=self.bottomVol, side=LEFT)

        #Time Bar
        self.currentTimeLabel = Label(root, text ='   00:00', relief = RIDGE)
        self.currentTimeLabel.pack(in_=self.bottomVol,side=LEFT)
        self.timeLabel = Label(root, text ='/ 00:00')
        self.timeLabel.pack(in_=self.bottomVol,side=RIGHT)

        
    # Calls the choose folder from folderNavigation
    def choose(self):
         folderNavigation.chooseFolder()
         self.start_button.configure(state=NORMAL)
    # Calls startMusicPlayer from folderNavigation
    def load(self):
        count = 0
        folderNavigation.startMusicPlayer()
        self.displayListOfSongs()
        self.writeCurrentSong()
        self.updateCurrentLength()
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
        global changeSongCondition
        global updateTimeCondition
        global startCondition
        startCondition = True
        changeSongCondition = True
        updateTimeCondition = True
    # Calls prevSong from folderNavigation    
    def prev(self):
        folderNavigation.prevSong()
        self.writeCurrentSong()
        global changeSongCondition
        global updateTimeCondition
        global startCondition
        startCondition = True
        changeSongCondition = True
        updateTimeCondition = True
        
    # Calls playSong from folderNavigation      
    def playSong(self):
        global pauseCondition
        global updateTimeCondition
        global startCondition
        startCondition = True
        updateTimeCondition = True
        if pauseCondition:
            pauseCondition = False
            folderNavigation.unPause()
        else:
            folderNavigation.play()
    # Calls stop from folderNavigation
    def stopSong(self):
        folderNavigation.stop()
        global updateTimeCondition
        updateTimeCondition = False
        global changeSongCondition
        changeSongCondition = True
        global startCondition
        startCondition = False
        global count
        count = 0
        
        
    # Calls pause from folderNavigation 
    def pauseSong(self):
        global pauseCondition
        global updateTimeCondition
        global startCondition
        startCondition = False
        updateTimeCondition = False
        pauseCondition = True
        folderNavigation.pause()
        
    # Writes currentSong to text box 
    def writeCurrentSong(self):
        currentSong = folderNavigation.currentSong()
        self.currentSong.config(text=currentSong)
        self.timeLabel.config(text = '/ ' + self.getLength())
        
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

    def getLength(self):
        return folderNavigation.getLength()

    def getCurrentLength(self):
        totalLength = folderNavigation.getRawLength()
        while True:
            global changeSongCondition
            global count
            if changeSongCondition:
                count = 0
                totalLength = folderNavigation.getRawLength()
                changeSongCondition = False
            mins, secs = divmod(count,60)
            mins = round(mins)
            secs = round(secs)
            formattedCurrentLength = '{:02}:{:02d}'.format(mins, secs)
            self.currentTimeLabel.config(text = '   ' + formattedCurrentLength)
            if startCondition and count < round(totalLength):
                sleep(1)
                count+=1

    def updateCurrentLength(self):
        t1 = threading.Thread(target=self.getCurrentLength)
        t1.start()


#this function should open the spectrum graph
def openGraph():
    while True:
        testLiveGraph.openGraph()
        print("Inside openGraph()")
        sleep(1)
        
        
root = None

def mainMusicPlayer():
    root=Tk()
    root.title("Sound Spectrum Visualizer Music Player")
    musicPlayer = MusicPlayer(root)
    return root

def closing_window():
    root.destroy()
    p1.terminate()




if __name__ == '__main__':
    
    #start openGraph() as its own process
    p1 = Process(target=openGraph)
    p1.start()
    root = mainMusicPlayer()
    #This overides the close button (X). Without this the sound will continue to play and the process wont terminate.
    root.protocol("WM_DELETE_WINDOW",closing_window)
    
    root.mainloop()
    
