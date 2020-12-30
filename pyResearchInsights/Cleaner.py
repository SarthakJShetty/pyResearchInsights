'''
Hello! This script is part of the larger pyResearchInsights project that you can check out here: https://github.com/SarthakJShetty/pyResearchInsights
We are trying to build an end-to-end ACA tool here
-Sarthak
(03/10/2019)

Purpose of this script:
Clean the corpus of special character'''

'''Importing the status logger function here to LOG the cleaner module working for debugging'''
from pyResearchInsights.common_functions import status_logger

'''This holds the elements of the abstract after it has been split at the spaces'''
elements = []
'''Holds the dirty elements that contain the \\ and // in them'''
dirty_elements = []
'''Holds the clean members of the abstract elements'''
cleaned_str_list = []
'''Holds the screened abstracts, null of any special character occurances'''
cleaned_texts = []

'''What needs to be implemented here?
1. A way for each element containing \\ to be put into a list.
2. Subtract said list from elements'''

def txt_to_list(abstract_directory, status_logger_name):
    '''Converting the text file to a list for easier processing'''
    txt_to_list_start_status_key = "Converting text to list"
    status_logger(status_logger_name, txt_to_list_start_status_key)

    try:
        '''If the Cleaner script is run independently, not as part of the pipeline as a whole, there would be no filename_ANALYTICAL.txt.
        This ensures that that file can be processed independently.'''
        cleaner_abstract_directory = (abstract_directory.split(".txt")[0])+"_"+'ANALYTICAL.txt'
        folder = open(cleaner_abstract_directory, 'r')
    except FileNotFoundError:
        cleaner_abstract_directory = (abstract_directory.split(".txt")[0])+'.txt'
        folder = open(cleaner_abstract_directory, 'r')

    abstracts = []

    for line in folder:
        abstracts.append(line)

    txt_to_list_end_status_key = "Converted text to list"
    status_logger(status_logger_name, txt_to_list_end_status_key)

    return abstracts

def dirty_element_generator(texts, status_logger_name):
    '''Finds all the elements which have the special character in them, makes a list and
    referes through them durng the next phases'''
    dirty_element_generator_start_status_key = "Generating list with special elements for weeding out later"
    status_logger(status_logger_name, dirty_element_generator_start_status_key)

    for text in texts:
        elements = text.split(" ")
        for element in elements:
            if('\\' in element):
                dirty_elements.append(element)
    
    dirty_element_generator_end_status_key = "Generated list with special elements for weeding out later"
    status_logger(status_logger_name, dirty_element_generator_end_status_key)

    return dirty_elements

def dirty_element_weeder(texts, dirty_elements, status_logger_name):
    '''Refers to the list of dirty variables and cleans the abstracts'''
    dirty_element_weeder_start_status_key = "Removing elements with special characters from the text list"
    status_logger(status_logger_name, dirty_element_weeder_start_status_key)

    cleaned_str_list =[]
    for text in texts:
        elements = text.split(" ")
        for element in elements:
            if element not in dirty_elements:
                cleaned_str_list.append(element)
        cleaned_texts.append(" ".join(lol for lol in cleaned_str_list))
        cleaned_str_list = []

    dirty_element_weeder_end_status_key = "Removed elements with special characters from the text list"
    status_logger(status_logger_name, dirty_element_weeder_end_status_key)
    
    return cleaned_texts

def cleaned_abstract_dumper(abstract_directory, cleaned_texts, status_logger_name):
    '''Dumping the cleaned abstracts to the disc and will be referring to it henceforth in the code'''
    cleaned_abstract_dumper_start_status_key = "Dumping the cleaned abstract .txt to the disc"
    status_logger(status_logger_name, cleaned_abstract_dumper_start_status_key)

    pre_new_cleaned_texts_folder = abstract_directory.split(".txt")[0]
    new_cleaned_texts_folder = open(pre_new_cleaned_texts_folder + "_"+"CLEANED.txt", 'w')

    for cleaned_text in cleaned_texts:
        new_cleaned_texts_folder.write(cleaned_text)
        new_cleaned_texts_folder.write('\n')

    cleaned_abstract_dumper_end_status_key = "Dumped the cleaned abstract .txt to the disc"
    status_logger(status_logger_name, cleaned_abstract_dumper_end_status_key)

    return new_cleaned_texts_folder
    
def cleaner_main(abstract_directory, status_logger_name):
    '''This module removes all the special characters from the abstract scrapped using the Bias tool.'''
    cleaner_main_start_status_key = "Entering the Cleaner module"
    status_logger(status_logger_name, cleaner_main_start_status_key)

    abstracts = txt_to_list(abstract_directory, status_logger_name)
    dirty_elements = dirty_element_generator(abstracts, status_logger_name)
    cleaned_texts = dirty_element_weeder(abstracts, dirty_elements, status_logger_name)
    new_cleaned_texts_folder = cleaned_abstract_dumper(abstract_directory, cleaned_texts, status_logger_name)
    '''Main contribution from this block of the code is the new cleaned .txt folder and cleaned abstracts. Just in case.'''
    
    cleaner_main_end_status_key = "Exiting the Cleaner module"
    status_logger(status_logger_name, cleaner_main_end_status_key)

    return cleaned_texts, new_cleaned_texts_folder