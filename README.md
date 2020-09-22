# ***pyResearchThemes:*** Analyzing research themes from academic publications

:warning: <strong>This package is under active development</strong> :warning:

### Contents
[**1.0 Introduction**](https://github.com/SarthakJShetty/Bias#10-introduction) <br>

[**2.0 Model Overview**](https://github.com/SarthakJShetty/Bias#20-model-overview) <br>

[**3.0 How it works**](https://github.com/SarthakJShetty/Bias#30-how-it-works) <br>

[**4.0 Installation Instructions**](https://github.com/SarthakJShetty/Bias#40-installation-instructions) <br>

[**5.0 Results**](https://github.com/SarthakJShetty/Bias#50-results) <br>

[**6.0 Citations**](https://github.com/SarthakJShetty/Bias#60-citations)

## 1.0 Introduction:

- Academic publishing has risen 2-fold in the past ten years, making it nearly impossible to sift through a large number of papers and identify broad areas of research within disciplines.

- In order to *understand* such vast volumes of research, there is a need for **automated text analysis tools**.

- However, existing tools such are **expensive and lack in-depth analysis of publications**.

- To address these issues, we developed ***pyResearchThemes***, an **open-source, automated text analysis tool** that:
	- **Scrape** papers from scientific repositories,
	- **Analyse** meta-data such as date and journal of publication,
	- **Visualizes** themes of research using natural language processing.

- To demonstrate the ability of the tool, we have analyzed the research themes from the field of Ecology & Conservation.

### 1.1 About:

This project is a collaboration between <a title="Sarthak" href="https://SarthakJShetty.github.io" target="_blank"> Sarthak J. Shetty</a>, from the <a title="Aerospace Engineering" href="https://aero.iisc.ac.in" >Department of Aerospace Engineering</a>, <a title="IISc" href="https://iisc.ac.in" target="_blank"> Indian Institute of Science</a> and <a title="Vijay" href="https://evolecol.weebly.com/" target="_blank"> Vijay Ramesh</a>, from the <a title="E3B" href="http://e3b.columbia.edu/" target="_blank">Department of Ecology, Evolution & Environmental Biology</a>, <a href="https://www.columbia.edu/" title="Columbia University" target="_blank">Columbia University</a>.

## 2.0 Model Overview:

- The model is made up of three parts:

	1. <strong><a title="Scraper" href="https://github.com/SarthakJShetty/Bias/tree/master/Scraper.py/">Scraper</a>:</strong> This component scrapes scientific repository for publications containing the specific combination of keywords.

	2. <strong><a title="Cleaner" href="https://github.com/SarthakJShetty/Bias/tree/master/Cleaner.py/">Cleaner</a>:</strong> This component cleans the corpus of text retreived from the repository and rids it of special characters that creep in during formatting and submission of manuscripts.

	3. <strong><a title="Analyzer" href="https://github.com/SarthakJShetty/Bias/tree/master/Analyzer.py/">Analyzer</a>:</strong> This component collects and measures the frequency of select keywords in the abstracts database.

	4. <strong><a title="NLP Engine" href="https://github.com/SarthakJShetty/Bias/tree/master/NLP_Engine.py/">NLP Engine</a>:</strong> This component extracts insights from the abstracts collected by presenting topic modelling.

	5. <strong><a title="Visualizer" href="https://github.com/SarthakJShetty/Bias/tree/master/Visualizer.py/">Visualizer</a>:</strong> This component presents the results and data from the Analyzer to the end user.

## 3.0 How it works:

<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Bias.png" alt="Bias Pipeline">

<i>***Figure 3.1*** Diagramatic representation of pipeline for collecting papers and generating visualizations.</i>

### 3.1 Scraper:
- The <a title="Scraper" href="https://github.com/SarthakJShetty/Bias/blob/master/Scraper.py">```Scraper.py```</a> currently scrapes only the abstracts from <a title="Springer" href="https://www.link.Springer.com" target="_blank">Springer</a>  using the <a title="BeautifulSoup" href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup</a> and <a title="urllib" href="https://docs.python.org/3/library/urllib.request.html#module-urllib.request" target="_blank">urllib</a> packages.

- A default URL is provided in the code. Once the keywords are provided, the URLs are queried and the resultant webpage is souped and ```abstract_id``` is scraped.

- A new <a title="Abstract ID" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Abstract_ID_Database_2019-04-24_19_35_1.txt">```abstract_id_database```</a> is prepared for each result page, and is referenced when a new paper is scraped.

- The <a title="Abstract Database" target="_blank" href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Abstract_Database_2019-04-24_19_35.txt">```abstract_database```</a> contains the abstract along with the title, author and a complete URL from where the full text can be downloaded. They are saved in a ```.txt``` file

- A <a title="Status Logger" href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Status_Logger_2019-04-24_19_35.txt" target="_blank">```status_logger```</a> is used to log the sequence of commands in the program.

<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Scraper.png" alt="Scraper grabbing the papers from Springer">

<i> **Figure 3.2** <a title="Scraper" href="https://github.com/SarthakJShetty/Bias/blob/master/Scraper.py">```Scraper.py```</a> script grabbing the papers from <a title="Springer" href="https://www.link.Springer.com" target="_blank">Springer</a>.</i>

### 3.2 Cleaner:
- The <a title="Cleaner" href="https://github.com/SarthakJShetty/Bias/tree/master/Cleaner.py/">```Cleaner.py```</a> cleans the corpus scrapped from the repository, before the  topic models are generated.

- This script creates a clean variant of the ```.txt``` corpus file that is then stored as <a href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Abstract_Database_2019-04-24_19_35_ANALYTICAL.txt" title="Analytical File">```_ANALYTICAL.txt```</a>, for further analysis and modelling

<img src='https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Cleaner.png' alt="Cleaner.py cleaned up text">

<i> **Figure 3.3** <a title="Cleaner" href="https://github.com/SarthakJShetty/Bias/tree/master/Cleaner.py/">```Cleaner.py```</a> script gets rid of formatting and special characters present in the corpus.</i>

### 3.3 Analyzer:
- The <a title="Analyzer" href="https://github.com/SarthakJShetty/Bias/tree/master/Analyzer.py/">```Analyzer.py```</a> analyzes the frequency of different words used in the abstract, and stores it in the form of a <a title="Pandas" href="https://pandas.pydata.org/">pandas</a> dataframe.

- It serves as an intermediary between the Scraper and the Visualizer, preparing the scraped data into a <a title="Analyzer CSV file" href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Abstract_Database_2019-04-24_19_35.csv">```.csv```</a>.

- This ```.csv``` file is then passed on to the <a title="Visualizer" href="https://github.com/SarthakJShetty/Bias/blob/master/Visualizer.py">```Visualizer.py```</a> to generate the "Trends" <a href="https://github.com/SarthakJShetty/Bias/tree/journal#53-trends-result-" title="Trends Charts">chart</a>.

<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Analyzer.png" alt="Analyzer sorting the frequency of each word occuring in the corpus">

<i>**Figure 3.4** <a title="Analyzer" href="https://github.com/SarthakJShetty/Bias/tree/master/Analyzer.py/">```Analyzer.py```</a> script generates this ```.csv``` file for analysis by other parts of the pipeline.</i>

### 3.4 NLP Engine:

- The NLP Engine is used to generate the topic modelling charts for the [Visualizer.py](https://github.com/SarthakJShetty/Bias/tree/master/Visualizer.py) script. 

- The language models are generated from the corpus for analysis using <a title="Gensim" href="https://pypi.org/project/gensim/">gensim</a> and <a title="spaCy" href="https://spacy.io">spaCy</a> packages that employ the <a href="https://dl.acm.org/doi/10.5555/944919.944937" title="LDA Modelling">Latent dirichlet allocation (LDA)</a> method <a title="LDA Modelling" href="">[2]</a>.

- The corpus and model generated are then passed to the [Visualizer.py](https://github.com/SarthakJShetty/Bias/tree/master/Visualizer.py) script.

- The top modelling chart can be pulled from here [here](https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Data_Visualization_Topic_Modelling.html).

	**Note:** The <a title="Topic Modelling .html" href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Data_Visualization_Topic_Modelling.html">```.html```</a> file linked above has to be downloaded and opened in a JavaScript enabled browser to be viewed.

### 3.5 Visualizer:

- The <a title="Visualizer" href="https://github.com/SarthakJShetty/Bias/blob/master/Visualizer.py">```Visualizer.py```</a> code is responsible for generating the visualization associated with a specific search, using the <a title="Gensim" href="https://pypi.org/project/gensim/" target="_blank">gensim</a> and <a title="spaCy" href="https://spacy.io" target="_blank">spaCy</a> for research themes and <a title="Matplotlib" href="https://http://matplotlib.org/" target="_blank">matplotlib</a> library for the trends.

- The research theme visualization is functional are presented under the <a title="Results Section" href="https://github.com/SarthakJShetty/Bias/tree/journal#50-results">5.0 Results</a> section.

- The research themes data visualization is stored as a <a title="Data Visualization" href="https://github.com/SarthakJShetty/Bias/blob/journal/LOGS/LOG_2019-04-24_19_35_East_Melanesian_Islands/Data_Visualization_Topic_Modelling.html">.html file</a> in the LOGS directory and can be viewed in the browser.

## 5.0 Usage:

To install the package from ```pip``` use the command:

		pip install pyResearchInsights

*This command installs ```pyResearchInsights``` alongwith ```pyLDAvis```, ```numpy```, ```matplotlib```, ```spaCy``` and ```gensim```*


```pyResearchInsights``` is modular in nature. Each part of the module described in the previous section can be run independently or part of a larger pipeline.

### 5.1 Scraper:

```python
from pyResearchInsights.common_functions import pre_processing
from pyResearchInsights.Scraper import scraper_main

keywords_to_search = "Valdivian Forests Conservation"
trend_keywords = "Conservation"

abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, logs_folder_name, status_logger_name = pre_processing(keywords_to_search)
scraper_main(abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, trend_keywords, keywords_to_search, status_logger_name)
```
- This script downloads abstracts from [Springer](https://link.springer.com) containing "Valdivian Forests Conservation", and generates a ```.CSV``` file containing the frequency of occurance of the term "Conservation".*

### 5.2 Cleaner:

```python
from pyResearchInsights.Cleaner import cleaner_main

abstracts_log_name = "/location/to/txt/file/to/be/cleaned"
status_logger_name = "Status_Logger_Name"

cleaner_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` is the ```.txt``` file containing the abstracts to be cleaned before generating research themes.
- ```status_logger_name``` is a file that contains the LOG folder from the code run for debugging.

- This script cleans the ```.txt``` generated by the ```Scraper``` function and generates a ```file_name_CLEANED.txt``` file. Abstracts available online are often riddled with poor formatting and special characters.

### 5.3 Analyzer:

```python
from pyResearchInsights.Analyzer import analyzer_main

abstracts_log_name = "/location/to/txt/file/to/be/analyzed"
status_logger_name = "Status_Logger_Name"

analyzer_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` is the ```.txt``` file containing the abstracts to be analyzed for frequency of various keywords.
- ```status_logger_name``` is a file that contains the LOG folder from the code run for debugging.

- This script analyzes the frequency of different keywords occuring in the corpus of text provided at ```abstracts_log_name```, for meta-analysis and plotting frequency charts.
- A ```_FREQUENCY_CSV.csv``` file is generated once the process is complete

### 5.3 NLP_Engine:

```python
from pyResearchInsights.NLP_Engine import nlp_engine_main

abstracts_log_name = "/location/to/txt/file/to/be/analyzed"
status_logger_name = "Status_Logger_Name"

nlp_engine_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` is the ```.txt``` file containing the abstracts to be cleaned before generating research themes.
- ```status_logger_name``` is a file that contains the LOG folder from the code run for debugging.

- This script generates the topic modelling charts for the abstracts in the ```abstracts_log_name``` file.

### Example Pipeline:

```python
from pyResearchInsights.common_functions import pre_processing
from pyResearchInsights.Scraper import scraper_main
from pyResearchInsights.Cleaner import cleaner_main
from pyResearchInsights.Analyzer import analyzer_main
from pyResearchInsights.NLP_Engine import nlp_engine_main

keywords_to_search = "Western Ghats Conservation"
trend_keywords = '''Conservation'''

'''Generating the LOG folders where the output files will be saved'''
abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, logs_folder_name, status_logger_name = pre_processing(keywords_to_search)
	
'''Scraping the abstracts here'''
scraper_main(abstract_id_log_name, abstracts_log_name, start_url, abstract_url, query_string, trend_keywords, keywords_to_search, status_logger_name)

'''Cleaning the corpus of special characters'''
cleaner_main(abstracts_log_name, status_logger_name)

'''Analyzing the frequency of occurence of various words in the corpus'''
analyzer_main(abstracts_log_name, status_logger_name)

'''NLP to generate the topics of discussion in the abstracts'''
nlp_engine_main(abstracts_log_name, status_logger_name)
```

## 6.0 Results:

### 6.1 Topic Modelling Results:

The ```NLP_Engine.py``` module creates topic modelling charts such as the one shown below.

<img src='https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Topics.png' alt='Topic Modelling Chart'>

<i>***Figure 5.1*** Distribution of topics discussed in publications pulled from <a title="Ecology Journals" href="journals.md">8 conservation and ecology themed journals</a></i>.

- Circles indicate topics generated from the ```.txt``` file supplied to the ```NLP_Engine.py```, as part of the ```Bias``` pipeline.
- Each topic is made of a number of top keywords that are seen on the right, with an adjustable relevancy metric on top.
- More details regarding the visualizations and the udnerlying mechanics can be checked out [here](https://nlp.stanford.edu/events/illvi2014/papers/sievert-illvi2014.pdf).

### 6.2 Weights and Frequency Results:

<img src = 'https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/WeightsAndFrequency.png' alt= "Weights and Frequncy">

<i>***Figure 5.2*** Here, we plot the variation in the weights and frequency of keywords falling under topic one from the chart <a title="Link to Topic Modelling charts" href="https://github.com/SarthakJShetty/Bias/tree/journal/#51-topic-modelling-results">above</a>.</i>

- Here, "weights" is a proxy for the importance of a specific keyword to a highlighted topic. The weight of a keyword is calculated by: i) absolute frequency and, ii) frequency of occurance with other keywords in the same topic.

- Factors i) and ii) result in variable weights being assigned to different keywords and emphasize it's importance in the topic.