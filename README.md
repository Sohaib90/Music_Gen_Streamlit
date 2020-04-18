# Music_Gen_Streamlit
"Music Generation using Neural Networks" Streamlit App

### TO DO:

- [x] Make a run_app.sh

- [ ] Introduction [~5 min] (Sohaib)
	- [ ] Team Member names/intro (WS 2019/2020, course name)
	- [ ] Outline
		- [ ] Introduction 
		- [ ] Data
		- [ ] Phase 1
		- [ ] Phase 2
		- [ ] Neural DJ
	- [ ] Definition
	- [ ] Literature review
		- [ ] Refer to the literature slides

- [x] Data Analysis [~10 min] (Shivaani)
	- [ ] General Info about data
		- [ ] Add charts and sources about data (Lakh and RedditPop)
	- [ ] DataProcessing Pipeline Graph (streamlit graph docs/ Abdallah's choice)
	- [ ] Raw MIDI data
		- [ ] Music21 intro and applications
		- [x] show raw midi (without explanation, button to visualize raw midi (Sohaib))
	- [x] Tokenized MIDI
		- [x] Show Tokenized with variable length
		- [ ] Expand Tokens (musicautobot, go through section and see if its too explained)
	- [x] Play MIDI (Sohaib)
		- [ ] Phase 1
			- [x] Play original
			- [x] Play extracted
		- [ ] Phase 2 
			- [ ] Play sample (Lakh)
 
- [ ] Add Model() (Abdallah)
	- [ ] Phase 1
		- [ ] Modeling  (Hugging Face OpenAI GPT2)
		- [ ] Data
			- [ ] Only Piano (extracction process)
		- [ ] Tokenization problem
	- [ ] Phase 2
		- [ ] Modeling (Architecture, Transformer XL) 
		- [ ] Data 
			- [ ] Used piano, but then ran into problems
			- [ ] handle big files problem
		- [ ] musicautobot API for data 

- [ ] Add Prediction() (Code: Sohaib)
	- [ ] Overview of pred process
	- [ ] Play
		- [ ] Play original
		- [ ] Play predicted
	- [ ] Visualize
		- [ ] Note sheet original
		- [ ] Note sheet predicted
	- [?] Metrics

- [ ] Technical Service/Deployment Pipeline (Code: Sohaib)
	- [x] make a requirements.txt
	- [ ] Docker and heroku deployment
		- [x] Make container
		- [ ] Check functionalities for each functional part of interface 

# Use Docker to run
make sure you have docker installed 
./run_app.sh (this will take around 7-10 mins)
then go to :  localost:8501