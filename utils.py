import os
import numpy as np
from multiprocessing import Process, Manager
import time
import threading
import pygame as pg
import streamlit as st

from musicautobot.musicautobot.numpy_encode import *
from musicautobot.musicautobot.config import *
from musicautobot.musicautobot.music_transformer import *
from musicautobot.musicautobot.multitask_transformer import *
from musicautobot.musicautobot.utils import midifile

threadLock = threading.Lock()

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