# ***pyResearchInsights:*** An open-source Python package for scientific text analysis

## Contents 
[1.0 Introduction](#introduction)

[2.0 Installation](#installation)

[3.0 How it works](#how)

[4.0 Results](#results)

[Citation](#cite)

## <a title='Introduction' id='introduction'>1.0 Introduction</a>:

- Academic publishing has risen 2-fold in the past ten years, making it nearly impossible to sift through a large number of papers and identify broad areas of research within disciplines.

- In order to *understand* such vast volumes of research, there is a need for **automated content analysis (ACA)** tools.

- However, existing ACA tools such are **expensive and lack in-depth analysis of publications**.

- To address these issues, we developed ```pyResearchInsights``` an end-to-end, open-source, automated content analysis tool that:
	- **Scrapes** abstracts from scientific repositories,
	- **Cleans** the abstracts collected,
	- **Analyses** temporal frequency of keywords,
	- **Visualizes** themes of discussions using natural language processing.

### <a title='About' id='about-the-project'>1.1 About</a>:

This project is a collaboration between <a title="Sarthak" href="https://SarthakJShetty.github.io" target="_blank"> Sarthak J. Shetty</a>, from the <a title="Aerospace Engineering" href="http://ces.iisc.ac.in" >Center for Ecological Sciences</a>, <a title="IISc" href="https://iisc.ac.in" target="_blank"> Indian Institute of Science</a> and <a title="Vijay" href="https://evolecol.weebly.com/" target="_blank"> Vijay Ramesh</a>, from the <a title="E3B" href="http://e3b.columbia.edu/" target="_blank">Department of Ecology, Evolution & Environmental Biology</a>, <a href="https://www.columbia.edu/" title="Columbia University" target="_blank">Columbia University</a>.

## <a title='Installation' id='installation'>2.0 Installation</a>:

:warning: **Note: `pyLDAvis` one of the dependencies of `pyResearchInsights`, depends on `sklearn`. `sklearn` has now been renamed to `scikit-learn`. To install the `pyResearchInsights`, set this environment variable and continue with the installation** :warning:

```
export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
```
To install the package using ```pip```, use the command:

```bash
pip install pyResearchInsights
```

**Note:** `pyResearchInsights` requires `python 3.7` to run. If you're unsure about the local dependencies on your system, please use package on [Google Colab](https://colab.research.google.com/) or create a `python 3.7` [Conda](https://docs.conda.io/en/latest/) environment and install `pyResearchInsights` inside that environment.

Since ```pyResearchInsights``` is available on ```pip```, it can be run on [Google Colab](https://colab.research.google.com/drive/1gZjOKr5pfwVMuxCSaGYw20ldFpV4gVws?usp=sharing) as well where users can leverage Google's powerful CPU and GPU hardware.

[![Run on Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gZjOKr5pfwVMuxCSaGYw20ldFpV4gVws?usp=sharing)

[![Cite This!](https://zenodo.org/badge/294472065.svg)](https://onlinelibrary.wiley.com/doi/10.1002/ece3.8098)

## <a title='How it works' id='how'>3.0 How it works</a>:

<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Bias.png" alt="Bias Pipeline">

<i>***Figure 3.1*** Diagrammatic representation of the pipeline.</i>

```pyResearchInsights``` is modular in nature. Each part of the package can be run independently or part of a larger pipeline.

### <a title='Example Pipeline' id='how-example'>Example Pipeline</a>:

This is an example pipeline, where we scrape abstracts from Springer pertaining to the conservation efforts in the Western Ghats.

```python
from pyResearchInsights.common_functions import pre_processing
from pyResearchInsights.Scraper import scraper_main
from pyResearchInsights.Cleaner import cleaner_main
from pyResearchInsights.Analyzer import analyzer_main
from pyResearchInsights.NLP_Engine import nlp_engine_main

'''Abstracts containing these keywords will be queried from Springer'''
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

Each module of the pacakage can be run independtely, as described in the following sections:

### <a title='Scraper' id='how-scraper'>3.1 Scraper</a>:

```python
'''Importing pre_processing() which generates LOG files during the code run'''
from pyResearchInsights.common_functions import pre_processing

'''Importing the scraper_main() which initiates the scraping process'''
from pyResearchInsights.Scraper import scraper_main

'''Abstracts containing these keywords will be scraped from Springer'''
keywords_to_search = "Valdivian Forests Conservation"

'''The refernce to the LOG folder and the status_logger are returned by pre_processing() here'''
abstracts_log_name, status_logger_name = pre_processing(keywords_to_search)

'''Calling the scraper_main() to start the scraping processing'''
scraper_main(keywords_to_search, abstracts_log_name, status_logger_name)
```

Here,

- ```keywords``` - Abstracts queried from Springer will contain these keywords.
- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts downloaded.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script downloads abstracts from [Springer](https://link.springer.com) containing the ```keywords``` "Valdivian Forests Conservation".

### <a title='Cleaner' id='how-cleaner'>3.2 Cleaner</a>:

```python
'''Importing the cleaner_main() to clean the txt file of abstracts'''
from pyResearchInsights.Cleaner import cleaner_main

'''The location of the file to be cleaned is mentioned here'''
abstracts_log_name = "/location/to/txt/file/to/be/cleaned"

'''status_logger() logs the seequence of functions executed during the code run'''
status_logger_name = "Status_Logger_Name"

'''Calling the cleaner_main() here to clean the text file provided'''
cleaner_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts to be cleaned before generating research themes.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script cleans the ```file_name.txt```  and generates a ```file_name_CLEANED.txt``` file. Abstracts available online are often riddled with poor formatting and special characters.

<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Cleaner_1.png">
<i> <b>Figure 3.2.1a</b> The text collected by the Scraper consists of special characters (second last line in figure above, '30\xc2\xa0cm'), which has to be cleaned before performing topic-modelling</i>


<img src="https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Cleaner_2.png">
<i><b>Figure 3.2.1b</b> The Cleaner gets rid of the special characters seen throughout the corpus as in Figure 3.2.1a, and thereby ensures legible topic-modelling results</i>

### <a title='Analyzer' id='how-analyzer'>3.3 Analyzer</a>:

```python
'''Importing the analyzer_main() to analyze the frequency of keywords encountered in the text file'''
from pyResearchInsights.Analyzer import analyzer_main

'''The location of the file to be analyzed is mentioned here'''
abstracts_log_name = "/location/to/txt/file/to/be/analyzed"

'''status_logger() logs the seequence of functions executed during the code run'''
status_logger_name = "Status_Logger_Name"

'''Calling the cleaner_main() here to analyze the text file provided'''
analyzer_main(abstracts_log_name, status_logger_name)
```
Here,

- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts to be analyzed for temporal frequency of various keywords.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script analyzes the frequency of different keywords occuring in texts contained in ```file_name.txt```, and generates a ```file_name_FREQUENCY_CSV.csv``` file.

### <a title='NLP Engine' id='how-nlp'>3.4 NLP_Engine</a>:

```python
'''Importing the nlp_engine_main() to generate the interactive topic modelling charts'''
from pyResearchInsights.NLP_Engine import nlp_engine_main

'''The location of the abstracts which will be used to train the language models'''
abstracts_log_name = "/location/to/txt/file/to/be/analyzed"

'''status_logger() logs the seequence of functions executed during the code run'''
status_logger_name = "Status_Logger_Name"

'''Calling the nlp_engine_main() here to train the language models on the texts provided'''
nlp_engine_main(abstracts_log_name, status_logger_name)
```

**Note**: The ```Visualizer``` is integrated within the ```NLP_Engine``` function.

Here,

- ```abstracts_log_name``` - The ```.txt``` file containing the abstracts from which research themes are to be generated.
- ```status_logger_name``` - File that contains logs the sequence of functions executed for later debugging.

- This script generates the <a title = 'Result - 1' href = '#topic-modelling-results'>topic modelling</a> and the <a title = 'Result - 2' href = '#frequency-charts'>frequency/weight</a> charts for the abstracts in the ```abstracts_log_name``` file.

## <a title='Results' id='results'>4.0 Results</a>:

### <a title = 'Topic Modelling Results' id = 'results-topic'>4.1 Topic Modelling Results</a>:

<img src='https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/Topics.png' alt='Topic Modelling Chart'>

<i>***Figure 4.1*** Distribution of topics presented as pyLDAvis charts</i>

- Circles indicate topics generated from the ```.txt``` file supplied to the ```NLP_Engine.py```. The number of topics here can be varied usine the ```--num_topics``` flag of the ```NLP_Engine```.
- Each topic is made of a number of keywords, seen on the right.
- More details regarding the visualizations and the udnerlying mechanics can be checked out [here](https://nlp.stanford.edu/events/illvi2014/papers/sievert-illvi2014.pdf).

### <a title = 'Weights/Frequency Chart' id = 'results-frequency-weight'>4.2 Weights and Frequency Results</a>:

<img src = 'https://raw.githubusercontent.com/SarthakJShetty/Bias/master/assets/WeightsAndFrequency.png' alt= "Weights and Frequncy">

<i>***Figure 4.2*** Here, we plot the variation in the weights and frequency of topic keywords</i>.

- The weight of a keyword is calculated by its: i) frequency of occurance in the corpus and, ii) its frequency of co-occurance with other keywords in the same topic.

## <a title='Citation' id='cite'>Citation</a>:
If you use `pyReasearchInsights` for your research, please cite us! Here is the BibTex entry for our 2021 Ecology & Evolution [paper](https://onlinelibrary.wiley.com/doi/10.1002/ece3.8098).

		@article{shetty2021pyresearchinsights,
		title={pyResearchInsights—An open-source Python package for scientific text analysis},
		author={Shetty, Sarthak J and Ramesh, Vijay},
		journal={Ecology and Evolution},
		volume={11},
		number={20},
		pages={13920--13929},
		year={2021},
		publisher={Wiley Online Library}
		}