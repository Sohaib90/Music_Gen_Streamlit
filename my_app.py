import os
import time

from utils.utils import *

def main():
    st.sidebar.title("What to do:")
    app_mode = st.sidebar.radio("Go to", ["Introduction", "Data Analysis",
                                          "Model Description", "Predictions"])

    if app_mode == "Data Analysis":
        st.title("Data Analysis of MIDI Files")
        select_action = st.sidebar.selectbox("Select function", ["Choose", "Data Info", 
                                                                "Raw MIDI", "Tokenized MIDI", "Play MIDI"])
        data_functions(select_action)

    elif app_mode == "Model Description":
        phase = st.sidebar.selectbox("Choose Phase", ["Phase I", "Phase II"])
        if phase == "Phase I":
            st.title("Phase I")
            print_phase1()
        else:
            st.title("Phase II")
            print_phase2()

    elif app_mode == "Predictions":
        st.title("Music Generation Predictions")
        st.info("This section will help you listen and visualize the predictions/inferences made by the \
                trained model.")
        which_play = st.sidebar.selectbox("Choose Music Model", ["Reddit Pop Model", "Lakh Midi Model"])
        if which_play == "Lakh Midi Model":
    	    play_pred("pred_lmd")
        else:
            play_pred("pred_reddit")

    elif app_mode == "Introduction":
        print_intro()
        intro()

if __name__ == "__main__":
    main()