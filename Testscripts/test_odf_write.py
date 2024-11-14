# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:04:14 2024

@author: thartl
"""


import pandas as pd
import pandas.testing as pd_testing
import unittest
import zipfile
import pickle

#import opendataformat as odf
import os
import xml.etree.ElementTree as ET
import opendataformat as odf

os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts')
  

#odf.write_odf(x, path)
#odf.read_odf(xpath)


def elements_equal(e1, e2, path="root"):
    """Recursively compare two elements and print details about any differences."""
    if e1.tag != e2.tag:
        print(f"Difference at {path}: Tag names differ ({e1.tag} != {e2.tag})")
        return False
    
    if (e1.text or '').strip() != (e2.text or '').strip():
        print(f"Difference at {path}: Text differs ({e1.text.strip()} != {e2.text.strip()})")
        return False
    
    if e1.attrib != e2.attrib:
        print(f"Difference at {path}: Attributes differ ({e1.attrib} != {e2.attrib})")
        return False
    
    # Recursively compare children
    children1 = list(e1)
    children2 = list(e2)
    
    if len(children1) != len(children2):
        print(f"Difference at {path}: Number of child elements differ ({len(children1)} != {len(children2)})")
        return False
    
    # Compare each pair of children, updating the path to reflect the XML hierarchy
    for index, (c1, c2) in enumerate(zip(children1, children2), start=1):
        child_path = f"{path}/{c1.tag}[{index}]"
        if not elements_equal(c1, c2, path=child_path):
            return False
    
    return True
def elements_equal(e1, e2, path="root", level=0):
    """Recursively compare two elements and print detailed information about any differences."""
    
    indent = " " * (level * 4)  # Adjust indentation for readability at each level
    
    # Compare tags
    if e1.tag != e2.tag:
        print(f"{indent}Difference at {path}: Tag names differ ({e1.tag} != {e2.tag})")
    
    # Compare text (ignoring surrounding whitespace)
    if (e1.text or '').strip() != (e2.text or '').strip():
        print(f"{indent}Difference at {path}: Text differs")
        print(f"{indent}  Text1: {e1.text.strip() if e1.text else 'None'}")
        print(f"{indent}  Text2: {e2.text.strip() if e2.text else 'None'}")
    
    # Compare attributes
    if e1.attrib != e2.attrib:
        print(f"{indent}Difference at {path}: Attributes differ")
        for key in set(e1.attrib.keys()).union(e2.attrib.keys()):
            value1 = e1.attrib.get(key, None)
            value2 = e2.attrib.get(key, None)
            if value1 != value2:
                print(f"{indent}  Attribute '{key}' differs (Value1: {value1} | Value2: {value2})")
    
    # Compare children
    children1 = list(e1)
    children2 = list(e2)
    if len(children1) != len(children2):
        print(f"{indent}Difference at {path}: Number of child elements differ ({len(children1)} != {len(children2)})")
    
    # Recursively compare each child pair
    for index, (c1, c2) in enumerate(zip(children1, children2), start=1):
        child_path = f"{path}/{c1.tag}[{index}]"
        elements_equal(c1, c2, path=child_path, level=level + 1)
    
    # Check if any extra children exist in either element
    if len(children1) > len(children2):
        for extra_child in children1[len(children2):]:
            print(f"{indent}Extra element in File1 at {path}/{extra_child.tag}: {ET.tostring(extra_child, encoding='unicode').strip()}")
    elif len(children2) > len(children1):
        for extra_child in children2[len(children1):]:
            print(f"{indent}Extra element in File2 at {path}/{extra_child.tag}: {ET.tostring(extra_child, encoding='unicode').strip()}")


def compare_xml_files(root1, root2):
    """Compare two XML files element-by-element with detailed reporting."""
    # Parse the XML files
    #tree1 = ET.parse(file1)
    #tree2 = ET.parse(file2)

    # Get the root elements
    #root1 = tree1.getroot()
    #root2 = tree2.getroot()
    
    # Compare root elements
    if elements_equal(root1, root2):
        print("The XML files are identical.")
    else:
        print("The XML files have differences.")

    
class TestWriteODF(unittest.TestCase):
    def test_write_odf_standard(self):
        
        #with open('testdata/data.pkl', 'rb') as f:
        #    df = pickle.load(f)
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '\data.zip')
        
        with tempfile.TemporaryDirectory() as temp_dir:
            print(temp_dir)
            odf.write_odf(df, path=temp_dir + '\data.zip')
            with zipfile.ZipFile(temp_dir + '\data.zip', 'r') as zip_file:    
                #self.assertTrue('data.csv' in zip_ref.namelist())
                #self.assertTrue('metadata.xml' in zip_ref.namelist())
                with zip_file.open('metadata.xml') as xml_file:
                    xml_content = xml_file.read().decode('utf-8')
                
                root1=ET.fromstring(zip_file.read('metadata.xml'))
        
        with zipfile.ZipFile('testdata' + '\data.zip', 'r') as zip_file:    
            #self.assertTrue('data.csv' in zip_ref.namelist())
            #self.assertTrue('metadata.xml' in zip_ref.namelist())
            with zip_file.open('metadata.xml') as xml_file:
                xml_content_orig = xml_file.read().decode('utf-8')

            root2=ET.fromstring(zip_file.read('metadata.xml'))
        #print(xml_content[0:200])
        #print(xml_content_orig[0:200])
        #self.assertEqual(xml_content, xml_content_orig)
        
        
if __name__ == '__main__':
    unittest.main()




# Use the function with your XML files


compare_xml_files(root1, root2)