# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:24:04 2024

@author: xhan
"""

# ODF2pd

import pandas as pd
import zipfile
import xml.etree.ElementTree as ET
import os

def get_lang(root,xpath):
    lang = []
    for ele in root.findall(xpath):
        lang.append(ele.get('{http://www.w3.org/XML/1998/namespace}lang'))

    lang = set(list(filter(None, lang)))
    return lang

def make_dataset_dic(root):        
    dictionary = {}  # Initialize the dictionary to store label entries
    #study and dataset name
    dictionary['study'] = root.findtext(".//stdyDscr/citation/titlStmt/titl")
    dictionary['dataset'] = root.findtext(".//fileDscr/fileTxt/fileName")
    # labels
    titl_stmt = root.find('.//fileDscr/fileTxt/fileCitation/titlStmt')
    if titl_stmt is not None:
        # Loop through each child element in titlStmt
        for elem in titl_stmt:
            # Check if there is a language attribute
            lang = elem.get('{http://www.w3.org/XML/1998/namespace}lang')
            if lang:
                # Store text with 'label_<language>' key if lang attribute exists
                dictionary[f'label_{lang}'] = elem.text
            else:
                # Store text with 'label' key if no lang attribute exists
                dictionary['label'] = elem.text
    # Process descriptions in fileCont
    for file_cont in root.findall('.//fileDscr/fileTxt/fileCont'):
        lang = file_cont.get('{http://www.w3.org/XML/1998/namespace}lang')
        if lang:
            dictionary[f'description_{lang}'] = file_cont.text
        else:
            dictionary['description'] = file_cont.text
    #URL
    ExtLink = root.findall('.//fileDscr/notes/ExtLink')
    if len(ExtLink) == 1:
        ExtLink[0].get('URI')

    
    return dictionary

def make_variables_dic(root, variables):        
    dictionaries={}
    
    for var in root.findall('.//dataDscr/var'):
        varname = var.attrib.get('name')
        if varname not in variables:
            continue
        # dictionary
        dictionary = {}
        # variable
        dictionary['variable'] = var.attrib.get('name')
        
        
        # Process `labl` elements
        for labl_elem in var.findall('labl'):
            # Check if there is a language attribute
            lang = labl_elem.get('{http://www.w3.org/XML/1998/namespace}lang')
            if lang:
                # Store text with 'label_<language>' key if lang attribute exists
                dictionary[f'label_{lang}'] = labl_elem.text
            else:
                # Store text with 'label' key if no lang attribute exists
                dictionary['label'] = labl_elem.text
        
        # Process `txt` elements
        for txt_elem in var.findall('txt'):
            # Check if there is a language attribute
            lang = txt_elem.get('{http://www.w3.org/XML/1998/namespace}lang')
            if lang:
                # Store text with 'description_<language>' key if lang attribute exists
                dictionary[f'description_{lang}'] = txt_elem.text
            else:
                # Store text with 'description' key if no lang attribute exists
                dictionary['description'] = txt_elem.text
        
        # Process `catgry` elements to accumulate labels by language
        for catgry_elem in var.findall('catgry'):
            # Get the category value
            catValu_elem = catgry_elem.find('catValu')
            if catValu_elem is not None:
                cat_value = catValu_elem.text
            else:
                continue  # Skip if there's no category value
    
            # Loop through `labl` elements within `catgry`
            for labl_elem in catgry_elem.findall('labl'):
                lang = labl_elem.get('{http://www.w3.org/XML/1998/namespace}lang', 'default')
                # Construct the key for labels by language (e.g., 'labels_en', 'labels_de')
                labels_key = f'labels_{lang}' if lang != 'default' else 'labels'
                
                # Initialize the dictionary for this language if not already present
                if labels_key not in dictionary:
                    dictionary[labels_key] = {}
                
                # Add the category value and corresponding label to the dictionary for the language
                dictionary[labels_key][cat_value] = labl_elem.text
        
        # Process `varFormat` for type
        varFormat_elem = var.find('varFormat')
        if varFormat_elem is not None:
            dictionary['format_type'] = varFormat_elem.get('type')
        
        # Process `ExtLink` for external URL
        extLink_elem = var.find('.//notes/ExtLink')
        if extLink_elem is not None:
            dictionary['url'] = extLink_elem.get('URI')
        
        dictionaries[varname] = dictionary
        
    return dictionaries
      


def read_odf(path, languages = "all", usecols = None, skiprows=None, nrows=None, na_values = None):
    # if path has not suffix .zip" but a ".zip" file exists, .zip" is added to path
    # if no file zipped file exists, but a folder with the name exists, the function tries to read
    
    if (not path.endswith(".zip") and not os.path.exists(path)) or (not path.endswith(".zip") and os.path.exists(path + ".zip")) :
        path = path + ".zip"

    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} was not found.")
    
    if not path.endswith(".zip") and (not os.path.exists(path + "data.csv") or not os.path.exists(path + "metadata.xml")):
        raise FileNotFoundError(f"A file {path + '.zip'} was not found and in the folder {path} expected metadata.xml and data.csv.")
    
    if '.zip' not in path:
        file_not_zipped = True
    else:
        file_not_zipped = False


    if file_not_zipped == False:
        # Open zip data and xml file in it   
        with zipfile.ZipFile(path, 'r') as zip_ref:    
            if 'data.csv' not in zip_ref.namelist():
                    raise Exception(f"Expected data.csv in {path}")
            if 'metadata.xml' not in zip_ref.namelist():
                    raise Exception(f"Expected metadata.xml in {path}")
            try:
                root=ET.fromstring(zip_ref.read('metadata.xml'))
            except Exception as e:
                raise Exception(f"{type(e).__name__} in reading metadata.xml in {path}. Check the xml file in the data file")
            
            # Iterate through the tags in xml and remove prefix of each tag
            for i in root.iter():
                i.tag=i.tag.split('}')[-1]
                #print(i.tag)
         
            # Save the dictionaries to pandas dataframe
            with zip_ref.open('data.csv') as csv_file:            
                try:
                    if (skiprows != None):
                        if (type(skiprows) == int):
                            skiprows = list(range(skiprows))
                        skiprows = [x + 1 for x in skiprows]
                    df = pd.DataFrame(data=pd.read_csv(csv_file, encoding='UTF-8', usecols = usecols, skiprows=skiprows, nrows=nrows, na_values = na_values))
                except Exception as e:
                    raise Exception(f"{type(e).__name__} in reading data.csv in {path}. Check the CSV file.")
                
                # Make dataset dictionary
                dataset_dic=make_dataset_dic(root)
                
                # Make variables dictionary
                variables_dic=make_variables_dic(root, variables =  list(df.columns))

                if languages != "all":
                    if type(languages) == str:
                        languages = [languages]
                    for key in list(dataset_dic):
                        if 'label_' in key or 'description_' in key:
                            if key.split("_")[1] not in languages:
                                dataset_dic.pop(key)
                    for varname in (variables_dic):
                        var_dic = variables_dic[varname]
                        for key in list(var_dic):
                            if 'label_' in key or 'labels_' in key or 'description_' in key:
                                if key.split("_")[1] not in languages:
                                    var_dic.pop(key)
                            variables_dic[varname] = var_dic
                
                df.attrs=dataset_dic
                for var_name, attributes in variables_dic.items():
                    if var_name in df.columns:
                        df[var_name].attrs=attributes
    elif file_not_zipped == True:
        metadata_path = os.path.join(path, 'metadata.xml')
        data_csv_path = os.path.join(path, 'data.csv')

        # Ensure files exist
        if not os.path.exists(metadata_path) or not os.path.exists(data_csv_path):
            raise ValueError("Expected metadata.xml and data.csv in {path}")

        # Parse metadata.xml directly
        try:
            tree = ET.parse(metadata_path)
        except Exception as e:
            raise Exception(f"{type(e).__name__} in reading metadata.xml in {path}. Check the xml file in the data file")

        root = tree.getroot()

        # Process XML tags
        for i in root.iter():
            i.tag = i.tag.split('}')[-1]


        # Load data.csv from folder and save dictionaries to DataFrame
        try:
            if (skiprows != None):
                if (type(skiprows) == int):
                    skiprows = list(range(skiprows))
                skiprows = [x + 1 for x in skiprows]
            df = pd.read_csv(data_csv_path, encoding='UTF-8', usecols = usecols, skiprows=skiprows, nrows=nrows, na_values = na_values)
        except Exception as e:
            raise Exception(f"{type(e).__name__} in reading data.csv in {path}. Check the CSV file.")
        
        
        
        df.attrs = dataset_dic
        for var_name, attributes in variables_dic.items():
            if var_name in df.columns:
                df[var_name].attrs=attributes
    return df
        

