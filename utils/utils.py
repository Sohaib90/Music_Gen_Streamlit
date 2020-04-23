import os
import time
import threading
from multiprocessing import Process, Manager

import numpy as np
import pygame as pg
import streamlit as st

from musicautobot.musicautobot.numpy_encode import *
from musicautobot.musicautobot.config import *
from musicautobot.musicautobot.music_transformer import *
from musicautobot.musicautobot.multitask_transformer import *
from musicautobot.musicautobot.utils import midifile

from utils.print_info import *

threadLock = threading.Lock()


def play_updated(midi_file):
    audio_file = open(midi_file, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

def append_to_list(L, file_name, vocab):

    for f in file_name:
        try:
            item = MusicItem.from_file(f, vocab)
            L.append(f)
        except:
            pass

def divide_chunks(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


class myThread (threading.Thread):
    def __init__(self, path_list, vocab, org_list):
        threading.Thread.__init__(self)
        self.path_list = path_list
        self.vocab = vocab
        self.list = org_list
        
    def run(self):
      # print ("Starting Thread..")
      # Get lock to synchronize threads
        threadLock.acquire()
        append_to_list(self.list, self.path_list, self.vocab)

      # Free lock to release next thread
        threadLock.release()

# In[34]:
def thread_it(L, list_x, vocab):
    threads = []
    threads.append(myThread(list_x, vocab, L))
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()


def play_music(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! {}".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    # check if playback has finished
    i = 0
    bar = st.progress(0)
    # while pg.mixer.music.get_busy():
    while True:
        i+=1
        bar.progress(i)
        time.sleep(0.1)
        if (i == 100):
        	pg.mixer.music.stop()
        	break


def music(file):
	freq = 44100    # audio CD quality
	bitsize = -16   # unsigned 16 bit
	channels = 2    # 1 is mono, 2 is stereo
	buffer = 2048   # number of samples (experiment to get right sound)
	pg.mixer.init(freq, bitsize, channels, buffer)
	# optional volume 0 to 1.0
	pg.mixer.music.set_volume(0.8)
	try:
	    play_music(file)
	except KeyboardInterrupt:
	    # if user hits Ctrl/C then exit
	    # (works only in console mode)
	    pg.mixer.music.fadeout(1000)
	    pg.mixer.music.stop()
	    raise SystemExit

def make_chart(type_data = "Data", 
			   labels = ['Python', 'C++', 'Ruby', 'Java', 'Haskell'],
			   sizes=[215, 130, 245, 210, 100], 
			   colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green'],
			   explode = (0.1, 0.1, 0.1, 0.1, 0.1)):

	st.subheader(type_data)

	# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	autopct='%1.1f%%', shadow=True, startangle=140)

	plt.axis('equal')
	st.pyplot()


def data_info_visual():
    '''
    data_info_visual: Makes configurations for the data sources and calls make_chart to 
                      visualize the pie charts in the Data info section
    '''

    data_set_all = ["Lakh Midi Dataset", "Reddit Pop Dataset", "Others"]
    sizes = [178000, 64000, 6000]
    colors = ['gold', 'lightblue', 'yellowgreen']
    explode = (0.0, 0.0, 0.0)
    make_chart(type_data= "Total Data", labels=data_set_all, 
                sizes=sizes, colors=colors, explode=explode)
    print_lakh()

    data_sets = ["MidiWorld", "Maestro Dataset", 
                                 "Mfiles.co.uk", "Piano-midi.de",
                                "Ambrose piano", "MPI Piano Dataset", "Reddit Dataset"]
    numbers = [90, 1300, 50, 270, 3300, 50, 750]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green', 'pink', 'crimson', 'babyblue']  
    make_chart(type_data="Division of 'Others' Dataset",
                labels= data_sets, sizes=numbers,
                colors = colors,
                explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1))

def raw_midi(midi_file):
    '''
    raw_midi: This function call helps visualize the RAW midi parsing which music21 does
    Input: midi_file
    '''
    st.subheader("Raw output of midi file converter")   
    stream = music21.converter.parse(midi_file)
    if len(stream.recurse()) >= 5:
        slider_note_visualize = st.slider("choose number of part visualizations:",0, int(len(stream.recurse())/5), 1)
        iterate = 0
        for s in stream.recurse():
            if iterate == slider_note_visualize:
                break
            st.write(s)
            iterate += 1
    else:
        st.write("converter gave an empty stream")

def tokenize_midi(midi_file, vocab):
    '''
    tokenize_midi: This function call visualize the tokenized version of the midi file
                    selected from the dropdown menu
    Input: midi_file (extracted)
           MusicVocab.create() vocabulary 
    '''
    st.subheader("Tokenized output of the midi file")
    # This section displays the tokens of the MIDI file
    try:
        item = MusicItem.from_file(midi_file, vocab)
        slider_token_len = st.slider("choose length of tokens you want to see",0, len(item.to_text()), int(len(item.to_text())/5))
        st.write( item.to_text()[:slider_token_len]+ " ...")
    except:
        st.write("Exception raised during handling {} ".format(file))
        st.write("Please select another file from sidebar")

def music_midi(midi_file, org_file):
    '''
    music_midi : this function call uses two input files, midi & original and plays 
                them inside the browser
    Input: extracted_file, original file
    '''
    st.info("INFO: This section lets you listen both the original version of the MIDI we used for \
                    extraction and also the extracted version of the melody.")

    st.subheader("Play MIDI")
    st.text("Choose any file from the sidebar to listen to a sample")

    st.subheader("Play Original MIDI")
    play_updated(org_file)

    st.write("\n")
    st.subheader("Play Piano extracted MIDI")
    play_updated(midi_file)



def data_functions(select_action):
    '''
    data_functions: uses function action from the sidebar and displays information
        It has four major sections:
        - Data Info: Uses Data sources and number for data collection visualizations and info
        - Raw MIDI: shows the raw music21 output of the file selected
        - Tokenized MIDI: shows the tokenization process and output
        - Play MIDI: plays the original as well as extracted version of the MIDI file
    
    Input: data_functions takes a string input which is given as a select_action from the
           dropdown menu
    '''
    # See functions
    if select_action == "Choose":
        print_choose()

    elif select_action == "Data Info":
        st.info("This section will give insight about data gathering and analytics")
        # info_checkbox = st.checkbox("Display information about the MIDI data")
        data_info_visual()

    else:
        midi_file, org_file, vocab = data_analysis_init()

        if select_action == "Raw MIDI":
            raw_midi(midi_file)

        elif select_action == "Tokenized MIDI":
            st.info("This section will explain how the tokenization works")

            check_tokens = st.sidebar.checkbox("Show info about Tokens")

            # This section displays the information of the tokenized version
            if check_tokens:
                print_tokenization()

            else:
                tokenize_midi(midi_file, vocab)

        elif select_action == "Play MIDI":
            music_midi(midi_file, org_file)

def data_analysis_init():
    '''
    data_analysis_init(): this function call gets the data, processess it, and then makes the 
                          array for the dropdown menu which is st.sidebar.selectbox
    
    Input: no input
    Output: returns selected midi_file and corresponding output file                
    '''
    vocab = MusicVocab.create()
    midi_path = Path("./streamlit_data/extracted_data")
    org_midi_path = Path("./streamlit_data/original_data")
    midi_files = get_files(midi_path, '.mp3', recurse=True)

    # process extracted files
    # filter_f = process_data(midi_files, vocab)
    file_select = [os.path.basename(x) for x in midi_files]
    file = st.sidebar.selectbox("Choose file", file_select)
    midi_file = midi_path/file

    # process original files
    org_file = str(org_midi_path) + "/" + file

    return midi_file, org_file, vocab

@st.cache()
def process_data(x, vocab):
    '''
    process_data: This function call processs all the data and stores it in the cache 
                of the broswer
    Input: x (list of all the files)
            vocab: MusicVocab.create()
    Output: processed result (list)
    '''
    result = []
    with Manager() as manager:
        L = manager.list()  # <-- can be shared between processes.
        processes = []
        start_time = time.time()
        batch_num = int(len(x) / 2)
        x = list(divide_chunks(x, batch_num))

        for i in range(len(x)):
            p = Process(target=thread_it, args=(L, x[i], vocab))  # Passing the list
            p.start()
            processes.append(p)
            
        for p in processes:
            p.join()
        
        result = list(L)
        return result

def intro():
    select = st.sidebar.selectbox("Options", ["GUI Info", "Outline", "Literature Review"])
    if select == "GUI Info":
        print_gui_info()
    elif select == "Literature Review":
        print_lit_review()
    else:
        print_outline()

def predictions():
	st.subheader("Under Construction..")
	pass