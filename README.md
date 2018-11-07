# Sound-Spectrum-Visualizer



Project Status: Currently we have the sound and graphs synced up, however the GUI freezes while a .wav file is playing.
		
Each team members next steps for Sprint 3:

- Wes: Correcting the spacing between the two graphs. Example: The x-axis title from the graph on top overlaps with the title of the graph on bottom.

- Chris: Continue to improve the GUI and add threading to improve the interface (ie. Time bar needs threading)

- Alyssa: Continue working of the bar graph and get it compatible with the fft data and PyAudio.

- Zach: 

- Allen:

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

