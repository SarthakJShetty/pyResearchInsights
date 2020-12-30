'''Hello! This portion of the code that acts as the processing code corroborating with the main scripts [re: Scraper, Analyzer+NLP_Engine, Visualizer]

- Sarthak J. Shetty
06/02/2019

This script has been renamed as the system_functions.py to carry out OS level interactions, such as:
1. tarballing the LOGS generated to reduce space.
2. Deleting the LOGs once the tarball has been created.
3. (Eventually) enable shell script to send the tarballed file over mail to the user.
4. (Eventually) enable shell script to upload the LOGS generated to GitHub.

- Sarthak J. Shetty
15/04/2019'''

'''Importing OS to call the tar function to generate the .tar file.'''
import os
'''From common_functions.py calling the status_logger() function to LOG the tarballing process and others as they are added here.'''
from pyResearchInsights.common_functions import status_logger

def rm_original_folder(logs_folder_name, status_logger_name):
	'''This function deletes the logs folder generated once the .tar.gz file has been created.'''
	rm_original_folder_start_status_key = "Deleting files belonging to:"+" "+logs_folder_name
	status_logger(status_logger_name, rm_original_folder_start_status_key)

	command_to_rm_function = "rm -r"+" "+logs_folder_name

	os.system(command_to_rm_function)

def tarballer(logs_folder_name, status_logger_name):
	'''This function prepares the tar ball of the LOG file.'''
	tarballer_start_status_key = "Tarballing"+" "+logs_folder_name+" "+"into"+" "+logs_folder_name+".tar.gz"
	status_logger(status_logger_name, tarballer_start_status_key)

	command_to_tar_function = "tar czf"+" "+logs_folder_name+".tar.gz"+" "+logs_folder_name
	os.system(command_to_tar_function)

	tarballer_start_end_key = "Tarballed"+" "+logs_folder_name+" "+"into"+" "+logs_folder_name+".tar.gz"
	status_logger(status_logger_name, tarballer_start_end_key)