#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyPDF2 import PdfFileReader #  These libraries have to be installed
from datetime import timedelta,date,datetime
from time import mktime, strptime

# return dictionary with metadata
# precondion: if impossible to read , None will be returned

def get_exif(f):

    dct={}   # metadata will be stored here
    
    try:
        pdf_toread = PdfFileReader(f)
        pdf_info = pdf_toread.getDocumentInfo() # dictionary of all possible metadata
        
        for a in pdf_info:
            if(a=="/Creator" or a=="/CreationDate" or a=="/Producer"): # requested keys
                if(a == "/CreationDate"):
                    
                    datestring = pdf_info[a][2:16]
                    
                    # converting date object to readable string
                    ts = strptime(datestring, "%Y%m%d%H%M%S")
                    dt = datetime.fromtimestamp(mktime(ts))
                    dct[a.strip("/")] = dt.strftime("%m/%d/%Y %H:%M:%S")  
                else:   
                    dct[a.strip("/")] = pdf_info[a]

    except:
        return None  #no metadata
    
    dct=dict(sorted(dct.items())) # sorting by keys
    return dct


# In[ ]:




