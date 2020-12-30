'''Hello! This code code is part of the pyResearchInsights project.
We will be displaying the results from the NLP_Engine.py code here, using primarily using pyLDAvis library.

Check out the repository README.md for a high-level overview of the project and the objective.

Sarthak J. Shetty
24/11/2018'''

from pyResearchInsights.common_functions import argument_formatter, status_logger
'''import matplotlib as plt'''
import matplotlib.pyplot as plt
'''Library necessary to develop the html visualizations'''
import pyLDAvis
'''Generating dictionary from the textual_data that is lemmatized'''
from collections import Counter
'''Importing pandas to create the dataframes to plot the histograms'''
import pandas as pd
'''Importing the colormap functions using matplotlib'''
from matplotlib import cm

def visualizer_generator(lda_model, corpus, id2word, logs_folder_name, status_logger_name):
	'''This code generates the .html file with generates the visualization of the data prepared.'''
	visualizer_generator_start_status_key = "Preparing the topic modeling visualization"
	status_logger(status_logger_name, visualizer_generator_start_status_key)

	'''Here, we generate the actual topic modelling visualization from thghe model created by pyLDAvis'''
	textual_data_visualization = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
	pyLDAvis.save_html(textual_data_visualization, logs_folder_name+"/"+"Data_Visualization_Topic_Modelling.html")

	'''Here, we generate the order of topics according to the LDA visualization'''
	topic_order = [textual_data_visualization[0].iloc[topic].name for topic in range(lda_model.num_topics)]

	return topic_order

	visualizer_generator_end_status_key = "Prepared the topic modeling visualization"+" "+logs_folder_name+"/"+"Data_Visualization_Topic_Modelling.html"
	status_logger(status_logger_name, visualizer_generator_end_status_key)		

def topic_builder(lda_model, topic_order, num_topics, num_keywords, textual_data_lemmatized, logs_folder_name, status_logger_name):
	'''We generate histograms here to present the frequency and weights of the keywords of each topic and save them to the disc for further analysis'''
	topic_builder_start_status_key = "Preparing the frequency and weights vs keywords charts"
	status_logger(status_logger_name, topic_builder_start_status_key)

	'''Setting the colormaps here to generate the num_topics charts that proceed'''
	colorchart = cm.get_cmap('plasma', num_topics)

	topics = lda_model.show_topics(num_topics = -1, num_words = num_keywords, formatted=False)
	data_flat = [w for w_list in textual_data_lemmatized for w in w_list]
	counter = Counter(data_flat)

	'''Generating a pandas dataframe that contains the word, topic_id, importance and word_count'''
	out = []
	for i, topic in topics:
	    for word, weight in topic:
	        out.append([word, i , weight, counter[word]])

	'''We will use bits of this dataframe across this function'''
	df = pd.DataFrame(out, columns=['word', 'topic_id', 'importance', 'word_count'])

	for topic in topic_order:
		'''Progressively generating the figures comprising the weights and frequencies for each keyword in each topic'''
		_, ax = plt.subplots(1, 1, figsize=[20, 15])
		x_axis = [x_axis_element for x_axis_element in range(0, num_keywords)]

		'''Creating the x_axis labels here, which is the topic keywords'''
		x_axis_labels = [element for element in df.loc[df.topic_id==topic, 'word']]
		y_axis = [round(element, 2) for element in df.loc[df.topic_id==topic, 'word_count']]

		'''Here, we make sure that the y_axis labels are equally spaced, and that there are 10 of them'''
		word_count_list = [word_count for word_count in df.loc[df.topic_id==topic, 'word_count']]
		word_count_increment = (max(word_count_list)/10)
		y_axis_labels = [round(0 + increment*(word_count_increment)) for increment in range(0, 10)]

		'''Here, we make sure that the y_axis_twin labels are equally spaced, and that there are 10 of them'''        
		word_importance_list = [word_count for word_count in df.loc[df.topic_id==topic, 'importance']]
		word_importance_increment = (max(word_importance_list)/10)
		y_axis_twin_labels = [0 + increment*(word_importance_increment) for increment in range(0, 10)]

		plt.xticks(x_axis, x_axis_labels, rotation=40, horizontalalignment='right', fontsize = 25)
		ax.bar(x_axis, y_axis, width=0.5, alpha=0.3, color=colorchart.colors[topic], label="Word Count")
		ax.set_yticks(y_axis_labels)
		ax.tick_params(axis = 'y', labelsize = 25)
		ax.set_ylabel('Word Count', color=colorchart.colors[topic], fontsize = 25)
		ax.legend(loc='upper left', fontsize = 20)

		'''Generating the second set of barplots here'''		
		ax_twin = ax.twinx()
		ax_twin.bar(x_axis, df.loc[df.topic_id==topic, 'importance'], width=0.2, color=colorchart.colors[topic], label = "Weight")
		ax_twin.set_ylabel('Weight', color=colorchart.colors[topic], fontsize = 25)
		ax_twin.set_yticks(y_axis_twin_labels)
		ax_twin.tick_params(axis='y', labelsize = 25)
		ax_twin.legend(loc='upper right', fontsize = 20)
		plt.title('Topic Number: '+str(topic_order.index(topic) + 1), color=colorchart.colors[topic], fontsize=25)

		'''Saving each of the charts generated to the disc'''		
		plt.savefig(logs_folder_name + '/FrequencyWeightChart_TopicNumber_' + str(topic_order.index(topic) + 1) + '.png')

	topic_builder_end_status_key = "Prepared the frequency and weights vs keywords charts"
	status_logger(status_logger_name, topic_builder_end_status_key)

def trends_histogram(abstracts_log_name, logs_folder_name, trend_keywords, status_logger_name):
	'''This function is responsible for generating the histograms to visualizations the trends in research topics.'''
	trends_histogram_start_status_key = "Generating the trends histogram"
	status_logger(status_logger_name, trends_histogram_start_status_key)

	'''What's happening here?
	a) trends_histogram receives the dictionary filename for the dictionary prepared by the Scraper code.
	b) Information is organized in a conventional key and value form; key=year, value=frequency.
	c) We extract the key from the dictionary and generate a new list comprising of the years in which the trend keywords occurs.
	d) We calculate the max and min years in this new list and convert them to int and extract the complete set of years that lie between these extremes.
	e) We cycle through the keys in the dictionary and extract frequency of occurrence for each year in the list of years.
	f) If the term does not appear in that year, then it's assigned zero (that's how dictionaries work).
	g) The two lists (list of years and list of frequencies) are submitted to the plot function for plotting.'''

	'''This list will hold the abstract years which contain occurrences of the word that we are investigating'''
	list_of_years=[]
	list_of_frequencies = []

	'''Accessing the dictionary data dumped by the Scraper code'''
	abstract_word_dictionary_file = open(abstracts_log_name + '_DICTIONARY.csv', 'r')

	'''Here we collect the dictionary data dumped by the Scraper code'''
	for line in abstract_word_dictionary_file:
		list_of_years.append(int(line.split(',')[0]))
		list_of_frequencies.append(int(line.split(',')[1][:-1]))

	'''Tabulating the start and the ending years of appearence of the specific trend_keywords'''
	starting_year = min(list_of_years)
	ending_year = max(list_of_years)

	'''Recreating the actual dictionary here'''
	abstract_word_dictionary = {list_of_years[year]:list_of_frequencies[year] for year in range(0, len(list_of_years))}

	'''Generating a continuous list of years to be plotted from the abstracts collected'''
	list_of_years_to_be_plotted = [year for year in range((starting_year), (ending_year)+1)]
	
	frequencies_to_be_plotted = []

	'''Here we generate the corresponding frequencies for each of the years recorded'''
	for year in range(starting_year, ending_year+1):
		try:
			frequencies_to_be_plotted.append(abstract_word_dictionary[year])
		except KeyError:
			frequencies_to_be_plotted.append(0)

	'''Here, we will generate a list of frequencies to be plotted along the Y axis, using the Y ticks function'''
	y_ticks_frequency = []

	'''Extracting the largest frequency value in the list to generate the Y ticks list'''
	max_frequency_value = max(frequencies_to_be_plotted)
	for frequency_element in range(0, max_frequency_value+1):
		y_ticks_frequency.append(frequency_element)

	'''Varying the size of the figure to accommodate the entire trends graph generated'''
	plt.figure(figsize=[15,10])
	'''Plotting the years along the X axis and the frequency along the Y axis'''
	plt.plot(list_of_years_to_be_plotted, frequencies_to_be_plotted)
	'''Plotting the frequencies again to make the frequency pivots visible'''
	plt.plot(list_of_years_to_be_plotted, frequencies_to_be_plotted, 'ro')
	'''Here, we are labeling each of the frequencies plotted to ensure better readability, instead of second-guessing Y axis values'''
	for element in range(0, len(list_of_years_to_be_plotted)):
		'''Avoiding the unnecessary clutter in the visualization by removing text boxes for frequency=0'''
		if(frequencies_to_be_plotted[element]!=0):
			plt.text(list_of_years_to_be_plotted[element], frequencies_to_be_plotted[element], "Frequency: "+str(frequencies_to_be_plotted[element]), bbox=dict(facecolor='orange', alpha=0.3), horizontalalignment='right', verticalalignment='top',size=8)

	'''Adds a label to the element being represented across the Y-axis (frequency of occurrence)'''
	plt.ylabel("Frequency of occurrence:"+" "+trend_keywords[0])
	'''Adds a label to the element being represented across the X-axis (years)'''
	plt.xlabel("Year of occurrence:"+" "+trend_keywords[0])
	'''Adds an overall title to the trends chart'''
	plt.title("Trends Chart:"+" "+trend_keywords[0])
	'''xticks() ensures that each and every year is plotted along the x axis and changing the rotation to ensure better readability'''
	plt.xticks(list_of_years_to_be_plotted, rotation=45)
	'''yticks() ensures that each and every frequency is plotted to ensure better readability in the resulting figure'''
	plt.yticks(y_ticks_frequency)
	'''Saves the graph generated to the disc for further analysis'''
	plt.savefig(logs_folder_name+"/"+"Data_Visualization_Trends_Graph"+"_"+trend_keywords[0]+".png")

	trends_histogram_end_status_key = "Generated the trends graph"+" "+logs_folder_name+"/"+"Data_Visualization_Trends_Graph"+"_"+trend_keywords[0]+".png"
	status_logger(status_logger_name, trends_histogram_end_status_key)

def	visualizer_main(lda_model, corpus, id2word, textual_data_lemmatized, num_topics, num_keywords, logs_folder_name, status_logger_name):
	visualizer_main_start_status_key = "Entering the visualizer_main() code"
	status_logger(status_logger_name, visualizer_main_start_status_key)

	'''This the main visualizer code. Reorging this portion of the code to ensure modularity later on as well.'''
	topic_order = visualizer_generator(lda_model, corpus, id2word, logs_folder_name, status_logger_name)

	'''We generate histograms here to present the frequency and weights of the keywords of each topic'''
	topic_builder(lda_model, topic_order, num_topics, num_keywords, textual_data_lemmatized, logs_folder_name, status_logger_name)

	visualizer_main_end_status_key = "Exiting the visualizer_main() code"
	status_logger(status_logger_name, visualizer_main_end_status_key)