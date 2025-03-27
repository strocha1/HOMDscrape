# HOMDscrape

HOMDscrape utilizes a Python-based software tool written in Jupyter Notebook to automate interaction with the [eHOMD](https://www.homd.org/) webserver using an open-source API and the HTML code from eHOMD. It is used to automate the process of gathering species names and amino acid sequences from a BLAST result or xml file.Once the raw data is collected by HOMDscrape, it is converted into a FASTA format and saved as a plain text file that can be used for downstream analysis (ex. Phylogenetic tree construction, Multiple Sequence Alignment).


## CITATION 
**If you use HOMDscrape, please cite the following paper:**

Rocha ST, Shah DD, Zhu Q, Shrivastava A.2025.The prevalence of motility-related genes within the human oral microbiota. Microbiol Spectr13:e01264-24.https://doi-org.ezproxy1.lib.asu.edu/10.1128/spectrum.01264-24

# Local installation 
### System requirements
The code has been written in Jupyter Notebook on a Windows system. Please open an issue if you have problems with installation. 
### Dependencies
HOMDscrape relies on the following packages (which can be installed using pip if needed):
- [re](https://docs.python.org/3/howto/regex.html)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#)
### Example Instructions
1. Install an [Anaconda](https://anaconda.org/anaconda/anaconda-navigator) navigator of Python.
2. Open a Jupyter Notebook (version 6.5.4) and Python 3 notebook (ipykernel).
3. Once opened, copy the notebook found in V3 HOMDscrape and the example xml file into the same folder.
4. Run the notebook and the output file should be ina  FASTA format
   
### Instructions for sequence ID files
1. Collect a BLAST file or Sequence Identifier file for the sequences that you need using the Sequence Server found on [eHOMD](https://www.homd.org/genome/blast_sserver?type=refseq). 
2. Open a Jupyter Notebook (version 6.5.4) and Python 3 notebook (ipykernel).
3. Once opened, copy the notebook found in the V3 HOMDscrape folder and the xml file of your choosing.  
7. Run the notebook and 1 output files should be given: finalfile.txt.
8. Once files are received, the finalfile.txt can be used for downstream analysis (ex. phylogenetic tree construction, Multiple Sequence Alignment)
