import streamlit as st
import graphviz as graphviz

def print_choose():
	st.info("Data Analysis dives deeper into the Data Preprocessing and Tokenization pipeline to \
			give a better visualization about the whole process. This section will try to summarise \
			how the data is taken in its RAW form and change into model ready format.")

	st.markdown("To get started, please choose the approporiate\
				action from the 'Select Function' on the sidebar")

def print_tokenization():
	st.subheader("Information about Tokienization")
	st.markdown("General overview of what tokenization achieves: ")
	st.image("./images/note_token.png", use_column_width=True)

	st.subheader("Steps to achieve tokenization")
	st.markdown("Musicautobot uses the following strategy to tokenize the music files.")

	st.subheader("Notes— One to Many")
	st.write("A single music note represents a collection of values: \n - Pitch (C, C#, … A#, B) \n - Duration (quarter note, whole note)")
	st.write("The easiest way to go about this is to encode a single note into a sequence of tokens")
	st.image("./images/one_to_many.png", use_column_width=True)

	st.subheader("Polyphony — Many to One")
	st.write("Uses the strategy of \
			  playing notes sequentially if it’s separated by a special “SEP” token. \
			  If not, play all the notes at once.")
	st.image("./images/bachbot.png", use_column_width=True)

	st.subheader("Putting it all together")
	st.image("./images/last_img.png", use_column_width=True)

	st.markdown("reference : https://towardsdatascience.com/creating-a-pop-music-generator-with-the-transformer-5867511b382a", 
				 unsafe_allow_html=True)

def print_lakh():
	st.markdown("The Lakh MIDI dataset is a collection of 176,581 unique MIDI files, \
                45,129 of which have been matched and aligned to entries in the Million Song Dataset.\
                Its goal is to facilitate large-scale music information retrieval, both symbolic \
                and audio content-based.")

	st.markdown("reference : https://colinraffel.com/projects/lmd/", unsafe_allow_html=True)
	
def print_intro():
	st.title("Music Generation Using Neural Networks")
	st.info("This Demo is created to help you understand and visualize our software project in a more \
		interactive and easy way. \n To switch in between different functionalities, please choose from the sidebar. " 
		)
	st.subheader("Software Project in Neural Networks")
	# Semester
	st.subheader("Winter Semester 19/20")

def print_outline():
	st.title("Outline")
	# GOAL
	st.subheader("Goal:")
	st.markdown("Initially proposed: ")
	st.markdown("Generate multi-instrument music using deep learning (for any specific genre)")
	st.markdown("Revised proposal: ")
	st.markdown("Use deep learning techniques to create a system that can predict/create \
				 just piano (single instrument) music, given a clipped music file.")
	# DATA
	st.subheader("Data:")
	st.markdown("Data collection/processing phase took around ~2 weeks. More Analytics about the data will be \
				 discussed in the Data Analysis section. During Phase 1, our take for a single instrument music \
				 generation included us extracting piano melodies from all the music sources we found, since the amount \
				 of data we had for just piano was not enough to train a model like OPENGPT2 or TRANSFORMERXL\
				 from scratch.")
	st.markdown("During Phase 2, we used two major midi file sources without any extraction processes, since the \
				data preprocessing pipeline for model training took care of that in the code. Our major resources \
				for the data in phase 2 included the Lakh Midi Dataset and Reddit Pop midi Dataset (more will \
				discussed in the Data Analysis section)")
	# PHASES
	st.subheader("Phases:")
	st.markdown("Our project, like every other group project evolved during the course. Our initial specifications \
				included using the extracted piano midi files, and hugging face OPENGPT2 API for music generation \
				but after running into problems which delayed our progress, we started to work in parallel \
				with other model architectures and methodolgies to keep the pace of our project intact. The key \
				differences between Phase 1 & Phase 2 are: ")
	st.markdown("1. Model Architecture")
	st.markdown("2. Use of extracted piano files in Phase 1 & use of original files in Phase 2 for the models")

	# Predictions
	st.subheader("Predictions:")
	st.markdown("We generate predictions by clipping a testing file and letting the trained model\
				 predict the rest of the music part by itself.")

def print_gui_info():
	# SECTIONS
	st.title("GUI Information")

	# Introduction
	st.title("Section 1: Introduction")
	st.markdown("This section is the welcome interface for the project. This section will help \
				explain what the GUI is all about, the different sections it has, how are they divided \
				, so that navigation is easy and without hindrance.")
	st.markdown("On the sidebar you have the option to choose between three sub-sections")
	st.markdown("1. GUI Information" )
	st.markdown("2. Outline ")
	st.markdown("3. Literature Review")
	st.subheader("GUI Information ")
	st.markdown("This is the page where the user will land by defualt, which contains all the \
				 information about the GUI for guidance, divided into subsections by the sidebar.")
	st.subheader("Outline")
	st.markdown("This section will provide a brief overview of how the project was approached and its outline.")

	st.subheader("Literature Review")
	st.markdown("This sub section will include the existing literature and methodologies that have been \
				developed and researched for producing music through deep learning.")
	
	# Data Analysis
	st.title("Section 2: Data Analysis")
	st.markdown("This section dives deeper into the Data Processing pipeline and tries to \
				take a visual/audio eplanatory approach. Subsections include ")
	st.markdown("1. Data Info")
	st.markdown("2. Raw MIDI")
	st.markdown("3. Tokenized MIDI")
	st.markdown("4. Play MIDI")

	st.subheader("Data Info")
	st.markdown("Shows the user visual representation of the data collected and the sources used \
				for the project's pipeline")

	st.subheader("RAW MIDI")
	st.markdown("Shows the RAW version of the MIDI file that we choose from the sidebar. Moreover, \
				briefly explains about the music21 library which was used for data processing.")
	
	st.subheader("Tokenized MIDI")
	st.markdown("Shows tokenized version of our midi files and also explains the process of tokenization.")

	st.subheader("Play MIDI")
	st.markdown("Uses the loaded files and plays for the user the original MIDI file and the piano extraction \
				of the MIDI file (some files may be piano in the original as well as extracted version)")
	
	# Model Description
	st.title("Section 3: Model Description")
	st.markdown("This section will briefly describe about the models and the phases of our training pipeline using \
				different architectures and methodologies, which is divided into Phase I and Phase II.")

	# Prediction
	st.title("Section 4: Predictions")
	st.markdown("Predictions will deal with the output from our trained models. It will have an original file, clipped\
				predicted file and the trimmed + predicted file, which the user can play and visualize.")
	st.markdown("There are two trained models, one is the Reddit Pop Model, which is trained on pop music, and the second is \
				the Lakh Midi Dataset model, which is trained on lakh dataset of classical songs.")

def print_lit_review():
	st.title("Literature Review")
	st.markdown("This section will go through the literature review our group did for the project. It will also discuss \
			the state of the art technologies that have already been used for music generation using AI.")
	
	# Magenta
	st.markdown("## Magenta (Google Brain)")
	st.markdown("Prior Work:")
	st.markdown("* Vanilla approaches include training a RNN (LSTM) model to predict the next note in a musical sequence (e.g. Eck and Schmidhuber 2002).")
	st.markdown("* Similar to character RNN, these Note RNNs were used to generate melodies by initializing them with a short sequence, and then obtaining next notes from the model by repeatedly sampling from the model’s output")
	st.markdown("Problems:")
	st.markdown("* Excessively repeating tokens (less creativity)")
	st.markdown("* Producing sequences that lack a consistent theme or structure (straying from music rules and structure)")
	st.markdown("* Wandering and random sequences (randomness)")
	st.markdown("Research Question:)")
	st.markdown("* Given music has relatively well-defined structural rules, can a simple Note RNN maintain that structural integrity?")	
	st.markdown("Proposition")
	st.markdown("* Given trained Note RNN, goal is to teach it concepts about music theory, while maintaining the information about typical melodies originally learned from data.")
	st.markdown("RL Tuner Design:")
	st.markdown("* Three networks: [The Q network, The Target-Q network] (Deep Q-Learning) and a Reward RNN")
	st.markdown("* Q-network, Target Q-network: recurrent LSTM model, architecture same as Note RNN")
	st.markdown("* Reward RNN: used to supply part of the reward value used to train model. Held fixed during training.")
	st.image("./images/magenta.png", use_column_width=True)


	# MuseGAN
	st.markdown("## MuseGAN")

	st.markdown("High Level Idea:")
	st.markdown("* As the name suggests, this strategy uses Generative Adversarial Networks (GANs)")
	st.markdown("* Three models for symbolic multi-track music generation")
	st.markdown("* The jamming model, the composer model and the hybrid model")
	st.markdown("* The paper shows that the models can generate coherent music of four bars right from scratch")
	st.markdown("Challenges:")
	st.markdown("* Have an account for the hierarchical, temporal, and the structuralpatterns of music")
	st.markdown("* Musical notes are often grouped into chords, arpeggios, or melodies, so chronologically ordering of notes is not suitable")
	st.markdown("Goal:")
	st.markdown("* Generate multi-track polyphonic music with harmonic and rhythmic structure, multitrack interdependency, temporal structure")
	st.markdown("Data Representation:")
	st.markdown("* They use multiple-track piano-roll representation")
	st.markdown("* The piano-roll dataset used is derived from the Lakh MIDI dataset (LMD) (Raffel 2016),4 a large collection of 176,581 unique MIDI files. The MIDI files are converted to multi-track piano-roll.")
	st.image("./images/MuseGAN.png", use_column_width=True)

	# Musenet (Open AI)
	st.markdown("## Musenet (Open AI)")
	st.markdown("The model:")
	st.markdown("* A transformer based model that can generate 4-minute musical compositions with 10 different instruments, and can combine styles from country to Mozart to the Beatles.")

	st.markdown("Approach:")
	st.markdown("* Uses the same general-purpose unsupervised technology as GPT-2, a large-scale transformer model trained to predict the next token in a sequence, whether audio or text.")
	st.markdown("Open AI GPT2:")
	st.markdown("* GPT-2 (2nd version of Open AI GPT) is a large transformer-based language model with 1.5 billion parameters, \
				trained on a dataset of 8 million web pages. GPT-2 is trained with a simple objective: predict the next word, \
				given all of the previous words within some text.")
	st.markdown("Limitations:")
	st.markdown("* Computation time and cost, considering the number of parameters mentioned above.")
	st.markdown("* The instruments you ask for are strong suggestions, not requirements. MuseNet generates each note by calculating the probabilities across all possible notes and instruments.")
	st.markdown("* The model shifts to make your instrument choices more likely, but there’s always a chance it will choose something else.")
	st.markdown("* MuseNet has a more difficult time with odd pairings of styles and instruments (such as Chopin with bass and drums). Generations will be more natural if you pick instruments closest to the composer or band’s usual style.")

	# WaveNet
	st.markdown("## WaveNet")
	st.markdown("What it does:")
	st.markdown("* WaveNet is a CNN based autoregressive  and fully probabilistic generative model that directly models the raw waveform of \
				the audio signal(i.e music or human speech), one sample at a time.")
	st.markdown("* It uses Gated PixelCNN architecture, dilated convolutions and causal convolutions.")
	st.markdown("Original purpose:")
	st.markdown("* To create human like speech better than the Text To Speech models, to make the output more close to real time human speech.")
	st.markdown("Implementation:")
	st.markdown("* The model is a CNN, where the convolutional layers have multiple dilatation factors and predictions only depend on \
				previous timesteps. i.e predictions only depends upto ‘t’ and not ‘t+1,t+2,...t+n’")
	st.markdown("* The Residual and Skip connections help the raw audio directly impact the output.")
	st.markdown("Results:")
	st.markdown("* In context of the speech generation, at each step during sampling a value is drawn from the probability distribution computed by the network and is \
				fed back into the input and a new prediction for the next step is made , for realistic-sounding audio.")
	st.markdown("* Further, the model was also used on piano dataset and new samples were generated opening possibilities for music generation.")

def print_phase1():
	st.title("Huggingface Transformers")
	st.subheader("Language Modeling")
	st.image("./images/phase1.jpg", use_column_width=True)
	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("Our Plan")
	st.image("./images/phase1_msuic.png", use_column_width=True)

	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("The Model")	
	st.image("./images/openAI-GPT-2-3.png", use_column_width=True)
	st.markdown("""
	* Decoder based transfoermer. \n
	* Auto-regressive in nature
	""")
	
	st.markdown("## Reasons for going with GPT2")
	st.markdown("1.	Text Generation Capipilities")
	st.image("./images/tr.png", use_column_width=True)
	st.markdown("2. replicate the MuseNet Open AI approach")

	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("Used Data")
	st.markdown("We used only Piano data after running the extraction due to")
	st.markdown("* Availability of data")
	st.markdown("* Our search was not done yet")

	st.subheader("-----------------------------------------------------------------------------")

	st.subheader("Problems, why did we shift to Phase ||")
	st.image("./images/phase1_msuic_problems.png", use_column_width=True)
	st.markdown("""
	* Generating features and vicabulary out of step 1
	* Training the model 
	""")
	
def print_phase2():
	st.title("Switching to FastAI")
	st.markdown("# Transformer-XL")
	st.markdown("## Why switching to Transformer-XL")
	st.markdown("* Availability of open source implementatins of GPT2")
	st.markdown("* Similar Perfomance to GPT2")
	st.subheader("-----------------------------------------------------------------------------")

	st.markdown("## Main Takeaways")
	st.markdown("* Transformer-XL is a transformer based archicture")
	st.markdown("* Transformer Memory - Previous tokens are stored in memory to evaluate only on the last predicted token. ")
	#Transformer Memory enables super fast inference. Instead of having to re-evaluate the whole sequence on every prediction,
	# you only need to evaluate on the last predicted token. Previous tokens are already stored in memory
	st.markdown("* Relative position - vanilla transformers use absolute position only.")
	st.subheader("-----------------------------------------------------------------------------")

	st.markdown("# Changes on Data")
	st.markdown("## Train two models.")
	st.markdown("* Lakh classic music model")
	st.markdown("* Reddit Pop music model")	

	st.markdown("## Preprocessing Extra Steps")
	st.markdown("* Data Augmentation")	
	st.markdown("* Positional Beat Encoding - extra Metadata for musical timing")

	st.subheader("-----------------------------------------------------------------------------")

	st.markdown("## Problems during Training.")
	#i.handling the data
	st.image("./images/nested-l.png", use_column_width=True)
	st.subheader("-----------------------------------------------------------------------------")

	st.markdown("## Training time.")
	st.markdown("* lakh - 4 epochs - 8 days")
	st.markdown("* Reddit Pop - 6 epochs - 4 days")
