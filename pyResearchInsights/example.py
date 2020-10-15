'''Hello! We have decided to modularize the entire code, and run it off of one common script.
In the future, the Analyzer.py and the Visualizer.py scripts will be called here as well.

Check out the build-log.md for a detailed changes implemented.
Check out the README.md for more details about the project.

Sarthak J. Shetty
12/09/2018'''

'''Imports scraper_main() from Scraper.py'''
from pyResearchInsights.Scraper import scraper_main
'''Importing the analyzer code here as well'''
from pyResearchInsights.Analyzer import analyzer_main
'''Importing the Cleaner functions here that removes special characters from the corpus'''
from pyResearchInsights.Cleaner import cleaner_main
'''Importing the visualizer and gensim code here'''
from pyResearchInsights.NLP_Engine import nlp_engine_main
'''Imports some of the functions required by different scripts here.'''
from pyResearchInsights.common_functions import pre_processing
'''Declaring tarballer here from system_functions() to tarball the LOG directory, & rm_original_folder to delete the directory and save space.'''
from pyResearchInsights.system_functions import tarballer, rm_original_folder

keywords_to_search = "Western Ghats Conservation"

'''Calling the pre_processing functions here so that abstracts_log_name and status_logger_name is available across the code.'''
abstracts_log_name, status_logger_name = pre_processing(keywords_to_search)

'''Runs the scraper here to scrape the details from the scientific repository'''
scraper_main(keywords_to_search, abstracts_log_name, status_logger_name)

'''Cleaning the corpus here before any of the other modules use it for analysis'''
cleaner_main(abstracts_log_name, status_logger_name)

'''Calling the Analyzer Function here'''
analyzer_main(abstracts_log_name, status_logger_name)

'''Calling the visualizer code below this portion'''
nlp_engine_main(abstracts_log_name, status_logger_name)