# HOMDscrape

HOMDscrape utilizes a Python-based software tool written in Jupyter Notebook to automate interaction with the [eHOMD](http://v2.homd.org/) webserver using an open-source API and the HTML code from eHOMD. It is used to automate the process of gathering species names and amino acid sequences from a BLAST result or sequence identifier file.Once the raw data is collected by HOMDscrape, it is converted into a FASTA format and saved as a plain text file that can be used for downstream analysis (ex. Phylogenetic tree construction, Multiple Sequence Alignment).


## CITATION 
**If you use HOMDscrape, please cite the following paper:**

Sofia T. Rocha, Dhara D. Shah, Qiyun Zhu, & Abhishek Shrivastava. The prevalence of motility within the human oral microbiota. bioRxiv 2023.07.17.549387 (2023) doi:10.1101/2023.07.17.549387.

# Local installation 
### System requirements
The code has been written in Jupyter Notebook on a Windows system. Please open an issue if you have problems with installation. 
### Dependencies
HOMDscrape relies on the following packages (which can be installed using pip if needed):
- [requests](https://pypi.org/project/requests/)
- [urllib.request](https://pypi.org/project/urllib3/)
- [time](https://docs.python.org/3/library/time.html)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [WebDriver](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver)
  
### Example Instructions
1. Install an [Anaconda](https://anaconda.org/anaconda/anaconda-navigator) navigator of Python.
2. Open a Jupyter Notebook (version 6.5.4) and Python 3 notebook (ipykernel).
3. Once opened, copy the notebook found [here](https://github.com/strocha1/HOMDscrape/blob/main/Main%20Code/SeqID_code_Main.%203.29.22.ipynb) and the example file found [here]() into the same folder.
5. Make sure that HOMD.org is version 192.168.0.51 and chromedriver is 123.0.6312.86
6. Run the notebook and 4 output files should be given: name.txt, AA.txt, newAA.txt, and finalfile.txt.
7. Once files are received, the code can be used for your files.
   
### Instructions for sequence ID files
1. Collect a BLAST file or Sequence Identifier file for the sequences that you need. 
2. Open a Jupyter Notebook (version 6.5.4) and Python 3 notebook (ipykernel).
3. Once opened, copy the notebook found [here](https://github.com/strocha1/HOMDscrape/blob/main/Main%20Code/SeqID_code_Main.%203.29.22.ipynb) and the example file found [here]() into the same folder. The example file can be switched out for your personal file of sequence ID's. 
5. Make sure that HOMD.org is version 192.168.0.51 and chromedriver is 123.0.6312.86
6. Make sure that the code pulls the sequence ID file (location of this command is annotated in the code. 
7. Run the notebook and 4 output files should be given: name.txt, AA.txt, newAA.txt, and finalfile.txt.
8. Once files are received, the finalfile.txt can be used for downstream analysis (ex. phylogenetic tree construction, Multiple Sequence Alignment)
