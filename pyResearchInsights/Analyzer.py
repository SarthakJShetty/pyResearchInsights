'''This code is part of the larger pyResearchInsights project, where we aim
to study the research themes being discussed in scientific publications.

This portion of the code analyzes the contents of the .txt file developed
by the Scraper.py and saves it to a .csv for later visualization by the
soon to be built Visualizer.py script

Sarthak J. Shetty
01/09/2018'''

'''Importing OS here to split the filename at the extension'''
import os
'''Importing status_logger here to log the details of the process run.'''
from pyResearchInsights.common_functions import status_logger
'''Importing the collections which contains the Counter function'''
from collections import Counter
'''Importing pandas here to build the dataframe'''
import pandas as pd
'''Importing numpy here to build the index of the pandas frameword'''
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def analyzer_pre_processing(abstracts_log_name, status_logger_name):
	'''Carries out the pre-processing tasks, such as folder creation'''
	analyzer_pre_processing_status_key="Carrying out pre-processing functions for analyzer"
	status_logger(status_logger_name, analyzer_pre_processing_status_key)

	try:
		'''If the Analyzer script is run independently, not as part of the pipeline as a whole, there would be no filename_CLEAND.txt.
		This ensures that that file can be processed independently.'''
		abstracts_txt_file_name = (abstracts_log_name.split(".txt")[0])+"_"+'CLEANED.txt'
		open(abstracts_txt_file_name, 'r')
	except FileNotFoundError:
		abstracts_txt_file_name = (abstracts_log_name.split(".txt")[0])+'.txt'

	'''This code strips the abstracts_log_name of its extension and adds a .csv to it'''
	abstracts_csv_file_name = (abstracts_log_name.split(".txt")[0]) + "_" + "FREQUENCY_CSV_DATA" + ".csv"

	analyzer_pre_processing_status_key = "Carried out pre-processing functions for analyzer"
	status_logger(status_logger_name, analyzer_pre_processing_status_key)

	return abstracts_txt_file_name, abstracts_csv_file_name

def list_cleaner(list_to_be_cleaned, status_logger_name):
	list_cleaner_start_status_key = "Cleaning the list of words generated"
	status_logger(status_logger_name, list_cleaner_start_status_key)

	'''This function cleans the list containing the words found in the abstract. It eliminates words found in another pre-defined list of words.'''
	words_to_be_eliminated = ['from', 'subject', 're', 'edu', 'use', 'com', 'https', 'url', 'link', 'abstract', 'author', 'chapter', 'springer', 'title', "the", "of", "and", "in", "to", "a", "is", "for", "from", "with", "that", "by", "are", "on", "was", "as", 
	"were", "url:", "abstract:", "abstract",  "author:", "title:", "at", "be", "an", "have", "this", "which", "study", "been", "not", "has", "its", "also", "these", "this", "can", "a", 'it', 'their', "e.g.", "those", "had", "but", "while", "will", "when", "only", "author", "title", "there", "our", "did", "as", "if", "they", "such", "than", "no", "-", "could"]

	cleaned_list_of_words_in_abstract = [item for item in list_to_be_cleaned if item not in words_to_be_eliminated]

	list_cleaner_end_status_key = "Cleaned the list of words generated"
	status_logger(status_logger_name, list_cleaner_end_status_key)	

	return cleaned_list_of_words_in_abstract

def transfer_function(abstracts_txt_file_name, abstracts_csv_file_name, status_logger_name):
    '''This function now includes TF-IDF, LDA, and bigram phrase extraction'''
    transfer_function_status_key = "Transferring data to pandas dataframe"
    status_logger(status_logger_name, transfer_function_status_key)

    list_of_words_in_abstract = []

    with open(abstracts_txt_file_name, 'r') as abstracts_txt_data:
        for line in abstracts_txt_data:
            for word in line.split():
                list_of_words_in_abstract.append(word)

    # Use TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(list_of_words_in_abstract)

    # Apply LDA for topic modeling
    lda = LatentDirichletAllocation(n_components=5)  # Adjust the number of topics
    lda.fit(X)

    # Phrase Extraction using Bigrams
    bigram_finder = BigramCollocationFinder.from_words(list_of_words_in_abstract)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, 10)

    # Building DataFrame for visualization
    dataframe_of_abstract_words = pd.DataFrame({
        'Words': vectorizer.get_feature_names(),
        'TF-IDF': X.toarray().flatten(),
        'Topics': lda.transform(X).flatten()
    })

    # Adding Bigrams
    dataframe_of_abstract_words['Bigrams'] = pd.Series(bigrams)

    transfer_function_status_key = "Data transferred to pandas dataframe"
    status_logger(status_logger_name, transfer_function_status_key)

    # Saving dataframe to csv file
    dataframe_of_abstract_words.to_csv(abstracts_csv_file_name, index=False)

    transfer_function_status_key = "Dataframe saved to CSV"
    status_logger(status_logger_name, transfer_function_status_key)

    return dataframe_of_abstract_words

def analyzer_main(abstracts_log_name, status_logger_name):
	'''Declaring the actual analyzer_main function is integrated to Bias.py code'''
	analyzer_main_status_key="Entered the Analyzer.py code."
	status_logger(status_logger_name, analyzer_main_status_key)

	'''Calling the pre-processing and transfer functions here'''
	abstracts_txt_file_name, abstracts_csv_file_name = analyzer_pre_processing(abstracts_log_name, status_logger_name)
	transfer_function(abstracts_txt_file_name, abstracts_csv_file_name, status_logger_name)

	'''Logs the end of the process Analyzer code in the status_logger'''
	analyzer_main_status_key="Exiting the Analyzer.py code."
	status_logger(status_logger_name, analyzer_main_status_key)