# Music_Gen_Streamlit
"Music Generation using Neural Networks" Streamlit App

### TO DO:

- [x] Make a run_app.sh

- [x] Introduction [~5 min] (Sohaib)
	- [x] Team Member names/intro (WS 2019/2020, course name)
	- [x] Outline
		- [x] Introduction 
		- [x] Data
		- [x] Phase 1
		- [x] Phase 2
		- [x] Neural DJ
	- [x] Literature review
		- [x] Refer to the literature slides

- [x] Data Analysis [~10 min] (Shivaani)
	- [x] General Info about data
		- [x] Add charts and sources about data (Lakh and RedditPop)
	- [x] DataProcessing Pipeline Graph (streamlit graph docs/ Abdallah's choice)
	- [x] Raw MIDI data
		- [x] Music21 intro and applications
		- [x] show raw midi (without explanation, button to visualize raw midi (Sohaib))
	- [x] Tokenized MIDI
		- [x] Show Tokenized with variable length
		- [ ] Expand Tokens (musicautobot, go through section and see if its too explained)
	- [x] Play MIDI (Sohaib)
		- [x] Phase 1
			- [x] Play original
			- [x] Play extracted
		- [x] Phase 2 
			- [x] Play sample (Lakh)
 
- [x] Add Model() (Abdallah)
	- [x] Phase 1
		- [x] Modeling  (Hugging Face OpenAI GPT2)
		- [x] Data
			- [x] Only Piano (extracction process)
		- [x] Tokenization problem
	- [x] Phase 2
		- [x] Modeling (Architecture, Transformer XL) 
		- [x] Data 
			- [x] Used piano, but then ran into problems
			- [x] handle big files problem
		- [x] musicautobot API for data 

- [x] Add Prediction() (Code: Sohaib)
	- [x] Overview of pred process
	- [x] Play
		- [x] Play original
		- [x] Play predicted
	- [x] Visualize
		- [x] Note sheet original
		- [x] Note sheet predicted
	- [?] Metrics

- [x] Technical Service/Deployment Pipeline (Code: Sohaib)
	- [x] make a requirements.txt
	- [x] Docker and heroku deployment
		- [x] Make container
		- [x] Check functionalities for each functional part of interface 

# Use Docker to run
make sure you have docker installed 
./run_app.sh (this will take around 7-10 mins)
then go to :  localost:8501

# RUN DEMO
https://neuralpiano.herokuapp.com/
