# import streamlit as st
import os
import numpy as np
from multiprocessing import Process, Manager
import time
import matplotlib.pyplot as plt

# from musicautobot.musicautobot.numpy_encode import *
# from musicautobot.musicautobot.config import *
# from musicautobot.musicautobot.music_transformer import *
# from musicautobot.musicautobot.multitask_transformer import *
# from musicautobot.musicautobot.utils import midifile
from utils import *
from tokenization_info import *


def main():
	st.sidebar.title("What to do:")
	app_mode = st.sidebar.radio("Go to", [ "Introduction", "Data Analysis", "Model Description", "Predictions"])

	if app_mode == "Data Analysis":
		st.title("Data Analysis of MIDI Files")

		# infromation

		st.subheader("Choose a file from the sidebar and apply functions of your choice")
		vocab = MusicVocab.create()
		midi_path = Path("./streamlit_data/extracted_data")
		org_midi_path = Path("./streamlit_data/original_data")
		midi_files = get_files(midi_path, '.mid', recurse=True)

		# process extracted files
		filter_f = process_data(midi_files, vocab)
		file_select = [os.path.basename(x) for x in filter_f]
		file = st.sidebar.selectbox("Choose file", file_select)
		midi_file = str(midi_path) + "/" + file


		# process original files
		org_file = str(org_midi_path) + "/" + file

		if not (os.path.exists(org_file)):
			st.write("Original (non- extracted) {} does not exist at {}".format(file, org_midi_path))
		else:
			# See functions
			select_action = st.sidebar.selectbox("Select function", ["Choose", "Data Info", "Raw MIDI", "Tokenized MIDI", "Play MIDI"])
			if select_action == "Choose":
				st.info("Data Analysis dives deeper into the Data Preprocessing and Tokenization pipeline to \
						give a better visualization about the whole process. This section will try to summarise \
						how the data is taken in its RAW form and change into model ready format.")

			elif select_action == "Data Info":
				st.info("This section will give insight about data gathering and analytics")
				# info_checkbox = st.checkbox("Display information about the MIDI data")
				make_chart()

			elif select_action == "Raw MIDI":
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

			elif select_action == "Tokenized MIDI":
				st.info("This section will explain how the tokenization works")

				check_tokens = st.sidebar.checkbox("Show info about Tokens")

				# This section displays the information of the tokenized version
				if check_tokens:
					print_tokenization()

				else:
					st.subheader("Tokenized output of the midi file")
					# This section displays the tokens of the MIDI file
					try:
						item = MusicItem.from_file(midi_file, vocab)
						slider_token_len = st.slider("choose length of tokens you want to see",0, len(item.to_text()), int(len(item.to_text())/3))
						st.write( item.to_text()[:slider_token_len]+ " ...")
					except:
						st.write("Exception raised during handling {} ".format(file))
						st.write("Please select another file from sidebar")


			elif select_action == "Play MIDI":
				st.info("INFO: This section lets you listen both the original version of the MIDI we used for \
					extraction and also the extracted version of the melody.")

				st.subheader("Play MIDI")
				st.text("Choose any file from the sidebar to listen to a sample")

				st.markdown("Click the button below to play original MIDI")
				play_org = st.button("Play Original")

				st.write("\n")
				st.markdown("Click the button below to play Piano extracted MIDI")
				play_file = st.button("Play Extracted")

				if play_file:
					music(midi_file)

				if play_org:
					music(org_file)


	elif app_mode == "Model Description":
		st.title("Model Architecture")
		model()
	elif app_mode == "Predictions":
		st.title("Music Generation Predictions")
		predictions()
	elif app_mode == "Introduction":
		st.title("Music Generation Using Neural Networks")
		st.info("This Demo is created to help you understand and visualize our software project in a more \
			interactive and easy way. \n To switch in between different functionalities, please choose from the sidebar. " 
			)
		st.subheader("Software Project in Neural Networks")
		st.text("Abdallah Bashir")
		st.text("Shivaani Kumar")
		st.text("Sohaib Arshid")


@st.cache()
def process_data(x, vocab):
	result = []
	item_list = []
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


def model():
	st.subheader("Under Construction..")
	pass

def predictions():
	st.subheader("Under Construction..")
	pass

if __name__ == "__main__":
	main()