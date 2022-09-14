#!/usr/bin/env python
# coding: utf-8

# ## This code is specific to homd.org
# ### requires homd.org to be version 192.168.0.52
# ### requires chromedriver to be 105.0.5195.52
# ### requires a list of sequence IDs that you wish to extract from eHOMD, typically a BLAST result

# # Module 1
# ## extracting sequence identifiers from a BLAST file 

# In[1]:


import requests #list of every library used in the code
import urllib.request
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from pandas import DataFrame
import numpy as np


# In[2]:


file=open('Example.txt').read() #Text file taken for HOMD gene blast search. Includes the sequence IDs that are exrtacted from HOMD.  


# In[3]:


file1=file.split() #splitting each element in the document at each space
file1


# In[4]:


Final_file= [i for i in file1 if "SEQF" in i] #Searching for elements that begin with 'SEQF' to isolate Sequence IDs.
Final_file


# In[5]:


a=Final_file[0] # getting the species number by selecting the first 8 characters 
a[0:8]


# In[6]:


species=[] # Creating a list for the species numbers 
for species1 in range(len(Final_file)): 
    
    b=Final_file[species1]
    species.append(b[0:8])
#species


# # Module 2
# ## Creating a list of unique websites for each species

# In[9]:


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(r"C:\Users\sofia\.wdm\drivers\chromedriver\win32\105.0.5195.52\chromedriver.exe", options=options)#locating chromedriver on local computer location may change based on computer. 
#This uses chromedriver's 99.0.4844.51 version. Update version to newest if needed. 
#options=options allows chromedriver to work in headless mode


# In[10]:


Link2 = np.array(["https://v2.homd.org/modules.php?op=modload&name=GenomeExpGM&file=index&gprog=danno&org=PROKKA_"]) #Main website that requires a species number 
Websites1 = [] #empty list for each custom website
for a in Link2: #adding the website to each species name to create custom websites. 
    for b in species:
        print (a+b)
        Websites1.append((a+b))


# # Module 3 
# ## Looking through each website in module 2 and collecting the species name
# ## Removing special characters and creating a FASTA format file

# In[11]:


name = []
for a in range(len(Websites1)):  # Using Chrome to access web
    driver = webdriver.Chrome(r"C:\Users\sofia\.wdm\drivers\chromedriver\win32\105.0.5195.52\chromedriver.exe", options=options) #operating webpages in headless mode
    driver.get(Websites1[a]) # Open the website
    time.sleep(2)
    genome = driver.find_element_by_xpath("//html/body/div[2]/table[1]/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/font/b").text #finding the genome selected name
    name.append(">"+genome)
    driver.close()
name


# In[ ]:


# initializing special characters
special_char = '@_!#$%^&*()<?/\|}{~:;.[]-,='
 
# using join() + generator to remove special characters
name1 = [''.join(x for x in string if not x in special_char) for string in name]
 
# print list without special characters to ease FAFSTA format conversion. 
name1


# In[ ]:


name2=[n.replace(" ","_")for n in name1]
name2 #done to create FAFSTA format


# In[ ]:


textfile = open("name.txt", "w")
for element in name1:
    textfile.write(element + "\n")
textfile.close() #saving names as a textfile


# # Module 4 
# ## Looking through each website in module 2 and collecting amino acid seqences
# ## saving sequences as a .txt file

# In[ ]:


AA=[] #creating an empty list for AA sequences 
for a in range(len(Websites1)):  # Using Chrome to access web
    driver = webdriver.Chrome(r"C:\Users\sofia\.wdm\drivers\chromedriver\win32\105.0.5195.52\chromedriver.exe", options=options)
    # Open the website
    driver.get(Websites1[a]) # searching each individual website
    search_box = driver.find_element_by_id('keyword') #finding the searchbox
    search_box.clear() #clearing the box
    search_box.send_keys(Final_file[a]) # Send SEQF information
    search_box.send_keys(Keys.RETURN)  # Click Enter
    time.sleep(3) #allowing the website to load
    driver.find_elements_by_class_name('showstate3') #differentiating between NA and AA hyperlinks
    parentGUID = driver.current_window_handle#determining the ID of the current tab/window
    time.sleep(3) #letting the website load
    driver.find_elements_by_class_name("showstate3")[1].click() #Selecting the hyperlink for AA
    allGUID = driver.window_handles
    driver.switch_to_window(allGUID[1]) #switching to window 2
    text = driver.find_element_by_tag_name("pre").text #finding body of text   
    
    AA.append(text) #adding text to list 
    driver.close()
AA


# In[ ]:


textfile = open("AA.txt", "w")
for element in AA:
    textfile.write(element + "\n")
textfile.close() #saving AA list as a text file


# # Module 5 
# ## combining the species names and amino acid sequences into a single document

# In[ ]:


with open('AA.txt') as fo: #opening the file of AA sequences
    for line in fo:
        if "SEQF" in line: #locating each line that contains SEQF
            line="/t" #replacing the whole line with \t
        newfile=open("newAA.txt",'a')
        newfile.write(line) #creating new file with no sequence identifiers
        newfile.close()


# In[ ]:


AA1=open('newAA.txt').read()
AA2=AA1.split('/t') #splitting the document at every /t
AA3= AA2[1:] # skipping over the first /t


# In[ ]:


final1=list(zip(name2,AA3)) #combining the name list and the AA list 
print(final1)


# In[ ]:


f = open('finalfile.txt', 'w')
for t in final1:
    line = '\t'.join(str(x) for x in t)
    f.write(line)
f.close() # saving the final list as a text document.


# In[ ]:





# In[ ]:




