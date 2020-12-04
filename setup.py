from distutils.core import setup
from os import getcwd

'''Using the getcwd() to direct the .py file to the README.md to generate the project description on the pypi repo'''
description_location = getcwd() + '/README.md' 

'''Reading the README file and setting it to the long_description variable'''
with open(description_location, encoding = 'utf-8') as f:
  long_description = f.read()

setup(
  name = 'pyResearchInsights',         # How you named your package folder (MyLib)
  packages = ['pyResearchInsights'],   # Chose the same as "name"
  version = '1.51',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'End-to-end tool for scientific literature analysis',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Sarthak J. Shetty',                   # Type in your name
  author_email = 'sarthakshetty97@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/SarthakJShetty/pyResearchInsights',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/SarthakJShetty/pyResearchInsights/archive/v_151.tar.gz',    # I explain this later on
  keywords = ['Educational Tools', 'Analysis', 'Scraper', 'Natural Language Processing'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'matplotlib',
          'nltk',
          'pyLDAvis',
          'gensim',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)