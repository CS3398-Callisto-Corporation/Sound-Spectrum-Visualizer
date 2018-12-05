# Sound-Spectrum-Visualizer

Post Sprint 3:

Project Status: Freezing GUI problem has been solved, but input data for graph was changed to the microphone. Plays songs and analysis graph shows best in a quiet room

One feature/accomplishment per team member:

- Wes: Implemented python multiprocessing library to run graph as its own process. No new files created, but main contribution came thorugh editing the musicPlayer.py file. I created a root process that runs the main music player GUI from the function "mainMusicPlayer()" and created another process that calls the openGraph function from the testLiveGraph.py file. This process runs the function openGraph() in musicPlayer.py. Both the mainMusicPlayer() and openGraph() process target functions are near the bottom of musicPlayer.py. I also wrote the majority (one or two lines are from other members) of the "if __name__ == '__main__':" statement at the bottom of musicPlayer.py. I also made a few small edits to folderNavigation.py to switch back to using the pygame library to play sound instead of pyaudio. 







Each team members next steps:

- Wes: Research interface between pygame and the graph. Then pipe the output of pygame (the sound playing) to the input of the graph

- Alyssa: get the data from the current fft to transfer over to anime.py and have the graph update every second or a few times a second

- Zach: Decrease sensitivity of graphs, and implement filters on sound so that you could experiment with signal processing

- Allen: Worked on testLiveGraph, captures sounds from mic instead of capturing sound FFT from source. Next Step would be either to stabalize the waveform and spectrum wave by decreasing chunk density caught by the mic. Or, try to convert it into a fft reader and capture sound fft directly from sound source. 




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

