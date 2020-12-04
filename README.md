# ***pyResearchInsights:*** Analyzing research themes from academic publications

:warning: <strong>This package is under active development</strong> :warning:

## 1.0 Introduction:

- Academic publishing has risen 2-fold in the past ten years, making it nearly impossible to sift through a large number of papers and identify broad areas of research within disciplines.

- In order to *understand* such vast volumes of research, there is a need for **automated content analysis (ACA)** tools.

- However, existing ACA tools such are **expensive and lack in-depth analysis of publications**.

- To address these issues, we developed ```pyResearchInsights``` an end-to-end, open-source, automated content analysis tool that:
	- **Scrapes** abstracts from scientific repositories,
	- **Cleans** the abstracts collected,
	- **Analyses** temooral frequency of keywords,
	- **Visualizes** themes of research using natural language processing.

### 1.1 About:

This project is a collaboration between <a title="Sarthak" href="https://SarthakJShetty.github.io" target="_blank"> Sarthak J. Shetty</a>, from the <a title="Aerospace Engineering" href="https://aero.iisc.ac.in" >Department of Aerospace Engineering</a>, <a title="IISc" href="https://iisc.ac.in" target="_blank"> Indian Institute of Science</a> and <a title="Vijay" href="https://evolecol.weebly.com/" target="_blank"> Vijay Ramesh</a>, from the <a title="E3B" href="http://e3b.columbia.edu/" target="_blank">Department of Ecology, Evolution & Environmental Biology</a>, <a href="https://www.columbia.edu/" title="Columbia University" target="_blank">Columbia University</a>.

## 2.0 Installation:

To install the package using ```pip```, use the command:

```bash
pip install pyResearchInsights
```

## 3.0 How it works:

<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Bias.png" alt="Bias Pipeline">

<i>***Figure 3.1*** Diagrammatic representation of the pipeline.</i>

```pyResearchInsights``` is modular in nature. Each part of the package can be run independently or part of a larger pipeline.

### 3.1 Scraper:

```python
from pyResearchInsights.common_functions import pre_processing

from pyResearchInsights.Scraper import scraper_main

keywords_to_search = "Valdivian Forests Conservation"

abstracts_log_name, status_logger_name = pre_processing(keywords_to_search)

scraper_main(keywords_to_search, abstracts_log_name, status_logger_name)
```

Here,

- ```keywords``` - Abstracts queried from Springer will contain these keywords.
- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts downloaded.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script downloads abstracts from [Springer](https://link.springer.com) containing the ```keywords``` "Valdivian Forests Conservation".

### 3.2 Cleaner:

```python
from pyResearchInsights.Cleaner import cleaner_main
abstracts_log_name = "/location/to/txt/file/to/be/cleaned"
status_logger_name = "Status_Logger_Name"
cleaner_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts to be cleaned before generating research themes.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script cleans the ```file_name.txt```  and generates a ```file_name_CLEANED.txt``` file. Abstracts available online are often riddled with poor formatting and special characters.

### 3.3 Analyzer:

```python
from pyResearchInsights.Analyzer import analyzer_main

abstracts_log_name = "/location/to/txt/file/to/be/analyzed"

status_logger_name = "Status_Logger_Name"

analyzer_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts to be analyzed for temporal frequency of various keywords.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script analyzes the frequency of different keywords occuring in texts contained in ```file_name.txt```, and generates a ```file_name_FREQUENCY_CSV.csv``` file.

### 3.4 NLP_Engine:

```python
from pyResearchInsights.NLP_Engine import nlp_engine_main

abstracts_log_name = "/location/to/txt/file/to/be/analyzed"

status_logger_name = "Status_Logger_Name"

nlp_engine_main(abstracts_log_name, status_logger_name)
```

**Note**: The ```Visualizer``` is integrated within the ```NLP_Engine``` function.

Here,

- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts from which research themes are to be generated.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script generates the topic modelling charts for the abstracts in the ```abstracts_log_name``` file.

### Example Pipeline:

This is an example pipeline, where we scrape abstracts from Springer pertaining to the conservation efforts in the Western Ghats.

```python
from pyResearchInsights.common_functions import pre_processing
from pyResearchInsights.Scraper import scraper_main
from pyResearchInsights.Cleaner import cleaner_main
from pyResearchInsights.Analyzer import analyzer_main
from pyResearchInsights.NLP_Engine import nlp_engine_main

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
```

## 4.0 Results:

### 4.1 Topic Modelling Results:

<img src='https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Topics.png' alt='Topic Modelling Chart'>

<i>***Figure 5.1*** Distributiom of topics presented as pyLDAvis charts</i>

- Circles indicate topics generated from the ```.txt``` file supplied to the ```NLP_Engine.py```, after cleaning and analysis.
- Each topic is made of a number of keywords, seen on the right.
- More details regarding the visualizations and the udnerlying mechanics can be checked out [here](https://nlp.stanford.edu/events/illvi2014/papers/sievert-illvi2014.pdf).

### 4.2 Weights and Frequency Results:

<img src = 'https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/WeightsAndFrequency.png' alt= "Weights and Frequncy">

<i>***Figure 5.2*** Here, we plot the variation in the weights and frequency of topic keywords</i>.

- The weight of a keyword is calculated by its: i) frequency of occurance in the corpus and, ii) its frequency of co-occurance with other keywords in the same topic.