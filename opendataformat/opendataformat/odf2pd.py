# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:24:04 2024

@author: xhan
"""

# ODF2pd

import pandas as pd
import zipfile
import xml.etree.ElementTree as ET


def get_lang(root,xpath):
    lang = []
    for ele in root.findall(xpath):
        lang.append(ele.get('{http://www.w3.org/XML/1998/namespace}lang'))

    lang = set(list(filter(None, lang)))
    return lang

def make_dataset_dic(root):        
    header = ['study','dataset']
    # labels
    for i in get_lang(root,'.//fileDscr/fileTxt/fileCitation/titlStmt/titl'):
        header.append('label_'+i)
    # descriptions
    for i in get_lang(root,'.//fileDscr/fileTxt/fileCont'):
        header.append('description_'+i)
    # url
    header.append('url')
        
    dictionary = {key:"" for key in header}
    # dataset
    dictionary['study'] = root.findtext(".//stdyDscr/citation/titlStmt/titl")
    dictionary['dataset'] = root.findtext(".//fileDscr/fileTxt/fileName")
    # labels
    for i in root.findall('.//fileDscr/fileTxt/fileCitation/titlStmt/titl'):
        for lang in get_lang(root,'.//fileDscr/fileTxt/fileCitation/titlStmt/titl'):
            if i.get('{http://www.w3.org/XML/1998/namespace}lang') == lang:
                dictionary['label_'+lang] = i.text
    # description
    for i in root.findall('.//fileDscr/fileTxt/fileCont'):
        for lang in get_lang(root,'.//fileDscr/fileTxt/fileCont'):
            if i.get('{http://www.w3.org/XML/1998/namespace}lang') == lang:
                dictionary['description_'+lang] = i.text
    # url
    for i in root.findall('.//fileDscr/notes/ExtLink'):
        dictionary['url'] = i.get('URI')
    return dictionary

def make_variables_dic(root):        
    dictionaries={}
    header = ['variable']
    # labels
    for i in get_lang(root,'.//dataDscr/var/labl'):
        header.append('label_'+i)
    # type
    header.append('type')
    # descriptions
    for i in get_lang(root,'.//dataDscr/var/txt'):
        header.append('description_'+i)
    # url
    header.append('url')

    for var in root.findall('.//dataDscr/var'):
        # dictionary
        dictionary = {key:"" for key in header}
        # variable
        dictionary['variable'] = var.attrib.get('name')
        # labels
        for i in var.findall('labl'):
            for lang in get_lang(root,'.//dataDscr/var/labl'):
                if i.get('{http://www.w3.org/XML/1998/namespace}lang') == lang:
                    dictionary['label_'+lang] = i.text
        # type
        for i in var.findall('varFormat'):
            dictionary['type'] = (i.attrib.get('type'))
        # descriptions
        for i in var.findall('txt'):
            for lang in get_lang(root,'.//dataDscr/var/txt'):
                if i.get('{http://www.w3.org/XML/1998/namespace}lang') == lang:
                    dictionary['description_'+lang]=i.text
        # url
        for i in var.findall('.//notes/ExtLink'):
            dictionary['url']=i.get('URI')

        for i in get_lang(root,'.//dataDscr/var/catgry/labl'):
            dictionary['labels_'+i]={}
        #check all availible language labels, and for each language:
            for cat in var.findall('catgry'):
                cat_value = cat.find('catValu').text
                for l in cat.findall('labl'):
                    if l.get ('{http://www.w3.org/XML/1998/namespace}lang')==i:               
                        dictionary['labels_'+i][cat_value] = l.text  
        
        #dictionary['label_'+i]= dict(value, value_labels)
        dictionaries[dictionary['variable']]=dictionary
        #pd.attrs[dictionary['variable']]=dictionary
    return dictionaries
      


def ODF2pd(path):
    if not path.endswith(".zip"):
        path = path + ".zip"

    # Open zip data and xml file in it   
    with zipfile.ZipFile(path, 'r') as zip_ref:      
        root=ET.fromstring(zip_ref.read('metadata.xml'))

        # Iterate through the tags in xml and remove prefix of each tag
        for i in root.iter():
            i.tag=i.tag.split('}')[-1]
            #print(i.tag)

        # Make dataset dictionary
        dataset_dic=make_dataset_dic(root)
        #print(dataset_dic)

        # Make variables dictionary
        variables_dic=make_variables_dic(root)
        #for i in variables_dic:
        #print(variables_dic['hgeqpnrj'])

        # Save the dictionaries to pandas dataframe
        with zip_ref.open('data.csv') as csv_file:            
            df= pd.DataFrame(data=pd.read_csv(csv_file,encoding='UTF-8'))
            df.attrs=dataset_dic
            for i in variables_dic.keys():
                df[i].attrs=variables_dic[i]
    return df
        

