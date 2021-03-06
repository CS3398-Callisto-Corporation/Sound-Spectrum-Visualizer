# Sound-Spectrum-Visualizer

Post Sprint 3:

Project Status: Freezing GUI problem has been solved, but input data for graph was changed to the microphone. Plays songs and analysis graph shows best in a quiet room

One feature/accomplishment per team member:

- Wes: Implemented python multiprocessing library to run graph as its own process. No new files created, but main contribution came thorugh editing the musicPlayer.py file. I created a root process that runs the main music player GUI from the function "mainMusicPlayer()" and created another process that calls the openGraph function from the testLiveGraph.py file. This process runs the function openGraph() in musicPlayer.py. Both the mainMusicPlayer() and openGraph() process target functions are near the bottom of musicPlayer.py. I also wrote the majority (one or two lines are from other members) of the "if __name__ == '__main__':" statement at the bottom of musicPlayer.py. I also made a few small edits to folderNavigation.py to switch back to using the pygame library to play sound instead of pyaudio. This does not match up with my next steps stated after sprint 2 due to a change of what graph we were using, Allen implemented the new graph and I took on a larger role in the multiprocessing side of the project.

- Allen: Implemented the live waveform (time domain) and spectrum frequency wave gui into the music player. Used pyqtgraph for the base animated graph, comapred to matplotlib it is faster and more accurate. Also, it's gui desgn presentation is more aesthic than the last graph. When the music play opens testLiveGraph.py, first creates the graph in the __init__ function. The self_plotdata function is self-explanatory;plots down points on the waveforms. The update function self-updates the waveforms as it catches sound through the mic. Animation function is what makes the whole graph animated and moving. When musicPLayer.py calls liveTerstGraph.py, it calls the opengraph function which pops the graph window into screen. 

- Chris: For Spring 3, I implemented volume bar, time bar, and fixed code that broke due to the introduction of multiprocessing in the file musicPlayer.py. In musicPlayer.py the introduction of multiprocessing caused some issues with a few of the features such as the drop down menu. This was changed to just show a folder icon instead of a drop down menu that showed file->open. There are two sections in musicPlayer.py that shows the code for the volumebar, the GUI section and the actual implementation of how to change the volume. These can be found under the commented section labeled #Volume Bar and the functions updateVol() and getVol() which both reference to functions in folderNavigation.py that I wrote last sprint. The volume bar works by implementing a horizontal slider that returns a value based on the location of the slider. The range returned was from 0 to 1. Since PyGame uses a linear way to change sound you could take this value and multiple it or set it directly to the volume. The time bar consumed most of the time as it required threading. The GUI can be seen under the commented section #Time Bar and the alogorythm can be seen under the functions getLength(), getCurrentLength(), and updateCurrentLength() in the file musicPlayer.py. First the time of the song had to be found which was pretty straight forward as PyGame has its own function that returns the total length of the song in seconds. In folderNavigation.py there are multiple functions that take seconds and converts into minutes and seconds (00:00). The functions in folderNavigation.py are getRawLength() and getLength(). Once the total length was found, an algorythm had to run that basically counted unless end of song occured or play/stop button occured. The threading section found in updateCurrentLength() calls this count algorythm so it can run concurrently while the other parts of the GUI works. I also changed how the close button works at the top right of an application. We had an issue where the process opened through multiprocessing would never close unless you directly killed the process through task manager. In the function closing_window() the process is terminated and the root (GUI) is destroyed. Then using this call root.protocol("WM_DELETE_WINDOW",closing_window) will override what the close button does.
I did end up acomplishing majority of what I tasked myself, but there were some things I didn't get around to. All of this can be found in the musicPlayer.py and folderNavigation.py.

- Alyssa: For sprint 3, I was able to get a somewhat working bar chart that takes data from the fft and translates it to a chart. 
anime.py takes the data generated by fft.py and plots the data so it is showing the correct outcome. fft.py was updated so that while it was running, it would call anime.py and display the updated chart. This sprint was an improvement compared to sprint 2 for myself. I accomplished connecting fft.py to anime.py and getting the data to show on a bar char, but I wish it was running more efficeintly and was connected to the main fft we now use.



Each team members next steps:

- Wes: Research interface between pygame and the graph. Then pipe the output of pygame (the sound playing) to the input of the graph

- Alyssa: get the data from the current fft to transfer over to anime.py and have the graph update every second or a few times a second

- Zach: Decrease sensitivity of graphs, and implement filters on sound so that you could experiment with signal processing

- Allen: Worked on testLiveGraph, captures sounds from mic instead of capturing sound FFT from source. Next Step would be either to stabalize the waveform and spectrum wave by decreasing chunk density caught by the mic. Or, try to convert it into a fft reader and capture sound fft directly from sound source. 

- Chris: Reincorporate some of the GUI functionality lost thru the addition of threading/multiprocessing like the drop down menu. Also implemnt something called ListBox from tkinter which is a clickable text box where you could select a song rather than only have the option to shuffle through each song one by one.



*************************************************************************************************************************

*************************************************************************************************************************

Project Status: Currently we have the sound and graphs synced up, however the GUI freezes while a .wav file is playing.
		
Each team members next steps for Sprint 3:

- Wes: Correcting the spacing between the two graphs. Example: The x-axis title from the graph on top overlaps with the title of the graph on bottom.

- Chris: Continue to improve the GUI and add threading to improve the interface (ie. Time bar needs threading)

- Alyssa: Continue working of the bar graph and get it compatible with the fft data and PyAudio.

- Zach: 

- Allen: Need to improve/re-design code for time domain graph, as to work with fft data and PyAudio with no error. 

What each team member worked on during Sprint 2:

- Wes: I worked on the meeting between PyAudio and PyGame. This ended up as allowing PyAudio to both play and analyize the audio, and just using the indexing and file navigation from the folderNavigation.py as control over which song will be played/analyze

- Chris: I worked on the "Music Player" GUI. The current "Music Player" in the master branch has a few issues when it was combined with the analysis part of code. A copy of how the GUI behaved before the combination can be found on the branch: https://github.com/CS3398-Callisto-Corporation/Sound-Spectrum-Visualizer/tree/c_j_developer This is how we hope the GUI behaves with the addition of the graphs.

- Alyssa: I continued working on the bar graph visulizer, but due to problems with PyAudio, I was not able to update anything due to not knowing if the program  was running correctly.

- Zach: 

- Allen:


******************************PREVIOUS INFORMATION (POST-SPRINT-1)******************************************************************************

An application that will take a filename or folder name, and present a player and sound spectrum visualizer.

Some .wav files have been included for ease of testing (gotta love the Godfather)





====FFT Implementation====
FFT Data is able to be extracted and plotted, but is not done in real time. Doing so will require
collaboration with the GUI team, as well as synchronizing audio playback from the music/sound player.
As of now, SciPy is being used to extract Fourier transform data, and is being plotted with MatPlotLib.
For sprint 2, the FFT Implemenation team will need to consider extracting fft data in raw digital values
to a Numpy array to be passed to the GUI team and decoded into spectrogram bars in real-time.

====First Sprint====
Information for the grader.

Christopher Jew - Worked on musicPlayer GUI and added some functions to folderNavigation to implement
				  with the musicPlayer GUI.
				  
				  To use musicPlayer:
				  *No volume button so it may be loud.*
				  Open in an editor and run the module (I used IDLE). GUI music player should appear.
				  Select "Choose Folder" and navigate to a folder with .wav files (Sound-Spectrum-Visualizer folder
				  has .wav files). Click "Start Music Player" to load the files. Use the other buttons to navigate
				  the song list and play the sound. 
				  
Alyssa LeJeune - worked on animatedGraph.py and got it to run by itself by generating random numbers.

Allen Van - Worked on the TimeDomainGUI.py file, as of now it runs on its own with a set equation set for the sin wave. It's more of a demo representation of what to expect when testing live.

Wes Nicol - Created folderNavigation.py file. This file contains the functions that allow the user to choose a folder and navigate through their songs.
            This folder also contains the functions that implement the start, pause, previous song, and next song buttons.  
====Next Steps====

Alyssa LeJeune - going to work on connecting the FFT to the bar graph and get it working in real time

Wes Nicol - work on integrating the different GUIs (ex: have the graphs pop up when a song is selected in the music player

Allen Van - Similar to Alyssa, but going to work on connecting the Time Domain graph and make it work in real time. 

Christopher Jew - Next step is to work on improving the GUI visually as well as adding functionality like volume bar.

