import streamlit as st


def print_tokenization():
	st.info("This section will explain how the tokenization works")
	st.subheader("Information about Tokienization")
	st.markdown("General overview of what we want to achieve: ")
	st.image("./images/note_token.png", use_column_width=True)

	st.subheader("Steps to achieve tokenization")
	st.markdown("As we already have established we will be using MIDI files for our problem. \
				We use MIDI because it’s one of the most popular digital music formats and \
				there’s a ton of these files on the internet. \
				Raw MIDI is represented in bytes. Even when converted to text, \
				it’s not very human readable.\
				Instead of doing that, we will be showing MIDI as for visualizations:")
	st.image("./images/note_pic.png", use_column_width=True)

	st.markdown("Turns out, there’s a couple of gotchas to keep in mind when encoding music files to tokens.\
	 			For text, it’s a pretty straight forward conversion.\
	 			Here’s how you would encode text to a sequence of tokens:")
	st.code("Vocabulary:{'a': 1, 'is': 2, 'language': 3, 'like': 4,'model': 5,'music': 6}")
	st.code("Text: “a music model is like a language model”")
	st.code("Tokenized: [1,6,5,2,4,13,5]")

	st.markdown("It’s a straight one-to-one mapping — word to token. \
				You can do other types of encoding like splitting contractions or byte-pair encoding,\
				but it’s still a sequential conversion.\
				Music however, is best represented in 2D as seen in the above figure")
	st.write("\n")
	st.markdown("Here’s another way of looking at the MIDI using piano roll representation")
	st.image("./images/piano_roll.png",use_column_width=True)
	st.markdown("From here we notice that: ")
	st.markdown("1. A single music note is a collection of values (pitch+duration)")
	st.markdown("2. Multiple notes can be played at a single point in time (polyphony)")
	st.markdown("The objective is to our model using this 2D representation of music. So our tokenization\
				 should be able to handle this 2D representation easily")

	st.subheader("Notes— One to Many")
	st.write("A single music note represents a collection of values: \n - Pitch (C, C#, … A#, B) \n - Duration (quarter note, whole note)")
	st.write("The easiest way to go about this is to encode a single note into a sequence of tokens")
	st.image("./images/one_to_many.png", use_column_width=True)

	st.subheader("Polyphony — Many to One")
	st.write("Another music model called “bachbot” has a clever solution to this. \
			  Play notes sequentially if it’s separated by a special “SEP” token. \
			  If not, play all the notes at once.")
	st.image("./images/bachbot.png", use_column_width=True)

	st.subheader("Putting it all together")
	st.write("When we put these above explained methods and with some magic \
			  (not really, just some manipulations) we get to this final tokenization result")
	st.image("./images/last_img.png", use_column_width=True)