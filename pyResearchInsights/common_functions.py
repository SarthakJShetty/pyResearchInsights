'''Hello! This script contains functions that are resued by other pieces of code and scripts belonging to this
project as well.

Checkout the README.md for more details regarding the project itself.

Sarthak J Shetty
12/09/2018'''

'''datetime is used while building the database logs'''
from datetime import datetime
'''Importing OS functions to build the folders for the LOG run here as well'''
import os
'''Importing argparse to parse the keywords, then supplied to the Scraper.py code'''
import argparse

def status_logger(status_logger_name, status_key):
	'''Status logger to print and log details throught the running the program.
	Declaring current_hour, current_minute & current_second.'''
	current_hour = str(datetime.now().time().hour)
	current_minute = str(datetime.now().time().minute)
	current_second = str(datetime.now().time().second)

	'''Logging the complete_status_key and printing the complete_status_key'''
	complete_status_key = "[INFO]"+current_hour+":"+current_minute+":"+current_second+" "+status_key
	print(complete_status_key)
	status_log = open(status_logger_name+'.txt', 'a')
	status_log.write(complete_status_key+"\n")
	status_log.close()

def status_logger_creator(abstracts_log_name):
	'''This is a standalone status_logger and session_folder filename generator, if someone is using the Bias components as standalone functions'''
	session_folder_name = abstracts_log_name.split('/')[-1]
	os.makedirs(session_folder_name)
	status_logger_name = session_folder_name+"/"+"Status_Logger"
	return status_logger_name, session_folder_name

def pre_processing(keywords):
	'''This function contains all the pre-processing statements related to the running of the program, including:
	1. Abstracts LOG Name
	2. Status Logger Name'''

	if((type(keywords) == str)):
		'''If the user uses the function independently of the argument_parser() we need this to convert the keywords to a list of words'''
		keywords = argument_formatter(keywords)

	'''Declaring the time and date variables here. Year, month, day, hours, minute & seconds.'''
	run_start_year = str(datetime.now().date().year)
	run_start_month = str(datetime.now().date().month)
	run_start_day = str(datetime.now().date().day)
	run_start_date = str(datetime.now().date())
	run_start_hour = str(datetime.now().time().hour)
	run_start_minute = str(datetime.now().time().minute)
	run_start_second = str(datetime.now().time().second)

	'''Keywords have to be written into the filename of the LOG that we are running'''
	folder_attachement = ""
	if(len(keywords)==1):
		folder_attachement = keywords[0]
	else:
		for keyword_index in range(0, len(keywords)):
			if((keyword_index+1)==len(keywords)):
				folder_attachement = folder_attachement+keywords[keyword_index]
			else:
				folder_attachement = folder_attachement+keywords[keyword_index]+"_"

	'''Declaring the LOG folder and the abstract, abstract_id & status_logger files.'''
	logs_folder_name = "LOGS"+"/"+"LOG"+"_"+run_start_date+'_'+run_start_hour+'_'+run_start_minute+"_"+folder_attachement
	abstracts_log_name = logs_folder_name+"/"+'Abstract_Database'+'_'+run_start_date+'_'+run_start_hour+'_'+run_start_minute
	status_logger_name = logs_folder_name+"/"+'Status_Logger'+'_'+run_start_date+'_'+run_start_hour+'_'+run_start_minute

	'''If the filename does not exist create the file in the LOG directory'''
	if not os.path.exists(logs_folder_name):
		os.makedirs(logs_folder_name)
	
	'''Creating the status_log and writing the session duration & date'''
	status_log = open(status_logger_name+'.txt', 'a')
	status_log.write("Session:"+" "+run_start_day+"/"+run_start_month+"/"+run_start_year+"\n")
	status_log.write("Time:"+" "+run_start_hour+":"+run_start_minute+":"+run_start_second+"\n")
	status_log.close()

	logs_folder_name_status_key = "Built LOG folder for session"
	status_logger(status_logger_name, logs_folder_name_status_key)

	return abstracts_log_name, status_logger_name

def keyword_url_generator(keywords_to_search):
	'''Reducing the long output of the pre_processing statement by offloading some of the scraper specific functions to another function'''
	if((type(keywords_to_search) == str)):
		'''If the user uses the function independently of the argument_parser() we need this to convert the keywords to a list of words'''
		keywords = argument_formatter(keywords_to_search)

	query_string = ""
	if (len(keywords)==1):
		query_string = keywords[0]
	else:
		for keyword_index in range(0, len(keywords)):
			if((keyword_index+1)==len(keywords)):
				query_string = query_string+keywords[keyword_index]
			else:
				query_string = query_string+keywords[keyword_index]+"+"

	start_url = "https://link.springer.com/search/page/"
	abstract_url = 'https://link.springer.com'

	'''We take the keywords here and generate the URLs here'''
	return start_url, abstract_url, query_string

def abstract_id_log_name_generator(abstracts_log_name):
	'''We use this function to generate the abstract_id_log_name from the abstracts_log_name'''
	return abstracts_log_name.split('Abstract')[0] + 'Abstract_ID' + abstracts_log_name.split('Abstract')[1]+'_'

def argument_formatter(argument_string):
	'''We make this into a function so that we can use it across the pyResearchInsights stack'''
	return argument_string.split()

def arguments_parser():
	'''This function is used to read the initial keyword that will be queried in Springer (for now).
	We will be scrapping Science, Nature etc later, as long as generic URLs are supported.
	Parses two arguments now:
	a) --keywords: This argument is the term that will be searched for in Springer.
	b) --trends: This argument provides the term whose research trend will be generated.
	c) --paper: This argument is triggered if the PDFs have to be downloaded as well.'''

	parser = argparse.ArgumentParser()
	parser.add_argument("--keywords", help="Keyword to search on Springer", default="Tiger")
	parser.add_argument("--trends", help="Keywords to generate the trends histogram for", default="Conservation")
	parser.add_argument("--paper", help="If papers have to be downloaded as well", default="No")

	arguments = parser.parse_args()
	if arguments.keywords:
		keywords = arguments.keywords
	'''The keyword if a string will be split and then be passed to the scraper functions'''

	keywords = argument_formatter(keywords)

	if arguments.trends:
		trends = arguments.trends
	'''The entire list of the abstract words will be lowered and hence trends term has to be
	lowered to obtain a match with those terms.'''

	'''if arguments.paper:
		paper = arguments.paper'''
	'''If this argument is turned to Yes, then the papers will be downloaded as well'''

	trends = trends.lower()
	trends = argument_formatter(trends)

	return keywords, trends

def end_process(status_logger_name):
	'''Self-explanatory, this function declares successful completion of the code.'''
	end_process_status_key="Process has successfully ended"
	status_logger(status_logger_name, end_process_status_key)