# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:25:16 2024

@author: thartl
"""

import pandas as pd
import os
import tempfile
import xml.etree.ElementTree as ET
import shutil
import zipfile


# Set the working directory
#os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python package/python package')
"""
import int_pd
import odf2pd


df = int_pd.int_pd("C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python package/python package/test_csv")

testdata = odf2pd.ODF2pd("C:\\Users\\thartl\\OneDrive - DIW Berlin\\Open Data Format Project\\Python\\Testdata\\data.zip")


print(df['bap87'].attrs)

df['pid'] = range(20)
df['pid'].attrs = {'name': 'pid',
                   'label_en': 'Personal Identifier', 
                   'label_de': 'Persönliche Identifikationsnummer', 
                   'description_en': 'example description ID', 
                   'description_de': 'Beispielbeschreigung ID', 
                   'type': 'numeric', 
                   'url': 'www.test.de',
                   'labels_en': {0: 'NA', 1: 'dummy'}, 
                   'labels_de': {0: 'NA', 1: 'Beispiel'}}





df.attrs = {'study': 'soep-core v38.1', 
            'dataset': 'bap',
            'label_en': 'Data from individual questionnaires 2010',
            'label_de': 'Daten vom Personenfragebogen 2010',
            'description_en': 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all". This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf',
            'description_de': 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf',
            'url': 'https://paneldata.org/soep-core/data/bap'}



"""

def write_odf(x, path):
    if (not isinstance(x, pd.DataFrame)):
        raise TypeError("Input not a pandas.core.frame.DataFrame")
    path = os.path.realpath(path)
    if not path.endswith(".zip"):
        path = path + ".zip"

    # Extract the filename from the path using os.path.basename (cross-platform)
    filename = os.path.basename(path)

    # Get the path of the system's temporary directory
    temp_dir = tempfile.gettempdir()

    # Create the full path for the temporary directory based on filename
    temp_subdir = os.path.join(temp_dir, filename.split('.')[0])

    # Remove the directory if it already exists
    if os.path.exists(temp_subdir):
        shutil.rmtree(temp_subdir)

    # Create the directory
    os.makedirs(temp_subdir, exist_ok=True)


    # write raw data as csv to the output folder
    x.to_csv(temp_dir + "/" + filename.split('.')[0] + "/data.csv", index = False)
    
    # Create the root element
    root = ET.Element("codeBook", {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xmlns": "ddi:codebook:2_5",
        "xsi:schemaLocation": "ddi:codebook:2_5 http://www.ddialliance.org/Specification/DDI-Codebook/2.5/XMLSchema/codebook.xsd",
        "version": "2.5"
    })
    
    # Add study description section
    stdyDscr = ET.SubElement(root, "stdyDscr")
    citation = ET.SubElement(stdyDscr, "citation")
    titlStmt = ET.SubElement(citation, "titlStmt")
    ET.SubElement(titlStmt, "titl").text = x.attrs.get('study', "")
    
    # Add file description section
    fileDscr = ET.SubElement(root, "fileDscr")
    fileTxt = ET.SubElement(fileDscr, "fileTxt")
    ET.SubElement(fileTxt, "fileName").text = x.attrs.get('dataset', "")
    
    fileCitation = ET.SubElement(fileTxt, "fileCitation")
    titlStmtFile = ET.SubElement(fileCitation, "titlStmt")
    
    # Get labels
    labels = {}
    for k,v in x.attrs.items():
        if (k == "label" or k.startswith("label_")):
            labels[k] = v
    # order label_en first:
    if labels.get('label_en',None) != None:
        labels_reordered = {'label_en': labels.pop('label_en')}
        labels_reordered.update(labels)
        labels = labels_reordered.copy()
        
    first_label = True
    for key,value in labels.items():   
        if (len(key.split("_"))==1):
            lang = "NA"
            if first_label == True:
                ET.SubElement(titlStmtFile, "titl").text = value
                first_label = False
            else:
                ET.SubElement(titlStmtFile, "parTitl").text = value
        else:
            lang = key.split("_")[1]
            if first_label == True:
                ET.SubElement(titlStmtFile, "titl", {"xml:lang": lang}).text = value
            else:
                ET.SubElement(titlStmtFile, "parTitl", {"xml:lang": lang}).text = value
    
    # Get descriptions
    descriptions = {}
    for k,v in x.attrs.items():
        if (k == "description" or k.startswith("description_")):
            descriptions[k] = v
    # order description_en first:
    if descriptions.get('description_en', None) != None:
        descriptions_reordered = {'description_en': descriptions.pop('description_en')}
        descriptions_reordered.update(descriptions)
        descriptions = descriptions_reordered.copy()
    # Add file content descriptions in multiple languages
    for key, value in descriptions.items():   
        if (len(key.split("_"))==1):
            lang = "NA"
            ET.SubElement(fileTxt, "fileCont").text = value

        else:
            lang = key.split("_")[1]
            ET.SubElement(fileTxt, "fileCont", {"xml:lang": lang}).text = value

    
    # Add external link to the dataset
    notes = ET.SubElement(fileDscr, "notes")
    ET.SubElement(notes, "ExtLink", {"URI": x.attrs.get('url', "")})


    # Add data description with variable Metadata
    dataDscr = ET.SubElement(root, "dataDscr")
    for col in list(x.columns):
        var = ET.SubElement(dataDscr, "var", {"name": col})
        if x[col].attrs == x.attrs:
            continue
        metadata_dict = x[col].attrs
        # Add English and German labels for the variable
        # Get labels
        labels = {}
        for k,v in metadata_dict.items():
            if (k == "label" or k.startswith("label_")):
                labels[k] = v
        # order label_en first:
        if labels.get('label_en',None) != None:
            labels_reordered = {'label_en': labels.pop('label_en')}
            labels_reordered.update(labels)
            labels = labels_reordered.copy()
            
        for key,value in labels.items():   
            if (len(key.split("_"))==1):
                lang = "NA"
                ET.SubElement(var, "labl").text = value
            else:
                lang = key.split("_")[1]
                ET.SubElement(var, "labl", {"xml:lang": lang}).text = value
                    
                    

        # Add English and German descriptions for the variable
        descriptions = {}
        for k,v in metadata_dict.items():
            if (k == "description" or k.startswith("description_")):
                descriptions[k] = v
        # order description_en first:
        if descriptions.get('description_en', None) != None:
            descriptions_reordered = {'description_en': descriptions.pop('description_en')}
            descriptions_reordered.update(descriptions)
            descriptions = descriptions_reordered.copy()
        # Add file content descriptions in multiple languages
        for key, value in descriptions.items():   
            if (len(key.split("_"))==1):
                lang = "NA"
                ET.SubElement(var, "txt").text = value
            else:
                lang = key.split("_")[1]
                ET.SubElement(var, "txt", {"xml:lang": lang}).text = value
        
        
        valuelabels = {}
        for k,v in metadata_dict.items():
            if (k == "labels" or k.startswith("labels_")):
                valuelabels[k] = v
        # order label_en first:
        if valuelabels.get('labels_en',None) != None:
            valuelabels_reordered = {'labels_en': valuelabels.pop('labels_en')}
            valuelabels_reordered.update(valuelabels)
            valuelabels = valuelabels_reordered.copy()
        
        labelled_values = []
        for key1, val1 in valuelabels.items():
            for key2 in val1.keys():
                labelled_values.append(key2)
        labelled_values = list(set(labelled_values))
        
        for val in labelled_values:   
            catgry = ET.SubElement(var, "catgry")
            ET.SubElement(catgry, "catValu").text = val
            for key, value in valuelabels.items():
                if (len(key.split("_"))==1):
                    lang = "NA"
                    ET.SubElement(catgry, "labl").text = value[val]
                else:
                    lang = key.split("_")[1]
                    ET.SubElement(catgry, "labl", {"xml:lang": lang}).text = value[val]


        # Add variable format
        ET.SubElement(var, "varFormat", {"type": x[col].attrs.get('type', "")})
        
        # Add external link to the variable
        var_notes = ET.SubElement(var, "notes")
        ET.SubElement(var_notes, "ExtLink", {"URI": x[col].attrs.get('url', "")})
    
    
    # Convert the ElementTree to a string
    tree = ET.ElementTree(root)
    
    # Write the XML structure to a file
    tree.write(temp_dir + "/" + filename.split('.')[0] + "/metadata.xml", encoding='utf-8', xml_declaration=True)
    

    dataset_dir = os.path.join(temp_dir, filename.split('.')[0])
    zip_path = os.path.join(path)

    # Create a zip file and add files to it
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(os.path.join(dataset_dir, 'metadata.xml'), arcname='metadata.xml')
        zipf.write(os.path.join(dataset_dir, 'data.csv'), arcname='data.csv')

    print(f"File sucessfully written to {zip_path}.")
    
    
    

#df_new = df.copy()
#df_new.drop(columns=['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'], inplace=True)

#print(df_new)
#write_odf(df_new, "test.zip")

#write_odf(x=testdata, path="test2.zip")
