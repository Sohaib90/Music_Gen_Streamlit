import os
import time

from utils.utils import *

def main():
    st.sidebar.title("What to do:")
    app_mode = st.sidebar.radio("Go to", ["Introduction", "Data Analysis",
                                          "Model Description", "Predictions"])

    if app_mode == "Data Analysis":
        st.title("Data Analysis of MIDI Files")
        select_action = st.sidebar.selectbox("Select function", ["Choose", "Data Info", "Raw MIDI", "Tokenized MIDI", "Play MIDI"])
        midi_file, org_file, vocab = data_analysis_init()

        if not os.path.exists(org_file):
        	st.write("Original (non- extracted) {} does not exist at {}".format(file, org_midi_path))
        else:
        	data_functions(midi_file, org_file, vocab, select_action)


    elif app_mode == "Model Description":
    	st.title("Model Architecture")
    	model()
    elif app_mode == "Predictions":
    	st.title("Music Generation Predictions")
    	predictions()
    elif app_mode == "Introduction":
    	print_intro()


if __name__ == "__main__":
	main()