# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:04:14 2024

@author: thartl
"""


import unittest
import zipfile
import io

#import opendataformat as odf
import os
import xml.etree.ElementTree as ET
import opendataformat as odf

os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts')
  

#odf.write_odf(x, path)
#odf.read_odf(xpath)


# function that checks whether csv-file are equal
# function ignores differences, if a number is stored as 1.0 or 1
# function ignores differences in quotes / doublequotes
def csvs_equal(zip_path1, zip_path2):
    def extract_csv_as_string(zip_path, filename="data.csv"):
        """Extracts the content of a CSV file from the ZIP archive as a string."""
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if filename not in zip_ref.namelist():
                raise FileNotFoundError(f"'{filename}' not found in {zip_path}")
            with zip_ref.open(filename) as file:
                return file.read().decode('utf-8')
    
    # Read both CSV files as strings
    csv1 = extract_csv_as_string(zip_path1)
    csv2 = extract_csv_as_string(zip_path2)
        
    difference_occured = False
    # Split into lines for comparison
    lines1 = csv1.splitlines()
    lines2 = csv2.splitlines()
    
    # Compare line by line
    for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        if line1.replace('"', '') != line2.replace('"', '').replace('.0,',','):
            print(f"Difference at line {i}:")
            print(f"O. csv-file: {line1}")
            print(f"N. csv-file: {line2}")
            difference_occured = True
            
    # Check if one file has extra lines
    if len(lines1) != len(lines2):
        print("Files have different number of lines.")
        print(f"Original csv-file has {len(lines1)} lines, new csv-file has {len(lines2)} lines.")
        difference_occured = True
    return not difference_occured

# Checks if the xml-files are equal
def xml_tree_equal(e1, e2, path="root"):
    """Recursively compare two elements and print detailed information about any differences."""
    level = 0
    
    differences_found = False
    
    if (ET.tostring(e1) != ET.tostring(e2)):
        differences_found = True
        if e1.attrib != e2.attrib:
            print(f"{'  ' * level}Difference at Level{level}:\n Tag names differ ({e1.attrib} != {e2.attrib})")
        level = 1
        if len(list(e1)) != len(list(e1)):
            print(f"{'  ' * level}Different number of elements on level {level}:\n e1: {[child.tag.split('}', 1)[-1] for child in list(e1)]}\n e2: {[child.tag.split('}', 1)[-1] for child in list(e2)]}")
        else:
            
            for child in list(range(len(list(e1)))):
                level = 1
                child1 = e1[child]
                child2 = e2[child]
                if child1.tag != child2.tag:
                    print(f"{'  ' * level}Difference at Level {level}:\n Tag element {child} for e1: {child1.tag.split('}', 1)[-1]}\n Tag element {child} for e1: {child1.tag.split('}', 1)[-1]}")
                if ET.tostring(child1) != ET.tostring(child2):
                    level = 2
                    print(f"{'  ' * level}Difference at Level {level}: differences in the {child1.tag.split('}', 1)[-1]}")
            
            for child in list(range(len(list(e1)))): 
                child1 = e1[child]
                child2 = e2[child]
                if ET.tostring(child1) != ET.tostring(child2):
                    level = 2
                    if (len(list(child1)) != len(list(child2))):
                        print(f"{'  ' * level}Different number of elements on level {level} in {child1.tag.split('}', 1)[-1]}")
                    for subchild in list(range(len(list(child1)))): 
                        level = 2
                        subchild1 = child1[subchild]
                        subchild2 = child2[subchild]
                        if ET.tostring(subchild1) != ET.tostring(subchild2):
                            print(f"{'  ' * level}Different number of elements on level {level} in {child1.tag.split('}', 1)[-1]} \n orig/new tree: {subchild1.tag.split('}', 1)[-1]} {subchild1.attrib}/{subchild2.tag.split('}', 1)[-1]} {subchild2.attrib} ")
                            for subsubchild in list(range(len(list(subchild1)))): 
                                level = 3
                                subsubchild1 = subchild1[subsubchild]
                                subsubchild2 = subchild2[subsubchild]
                                if ET.tostring(subsubchild1) != ET.tostring(subsubchild2):
                                    print(f"{'  ' * level}orig/new tree: {subsubchild1.tag.split('}', 1)[-1]}/{subsubchild2.tag.split('}', 1)[-1]}")                                    
    if (differences_found):
        return False
    else:
        return True
    
    
  

class TestWriteODF(unittest.TestCase):
    def test_write_odf_standard(self):
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data.zip')
        
        with zipfile.ZipFile('testoutput' + '/data.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
            
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data.zip','testoutput' + '/data.zip' ))
            
    def test_write_odf_default_lang(self):
        
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data_with_default.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_with_default.zip')
        
        with zipfile.ZipFile('testoutput' + '/data_with_default.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_with_default.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
        
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data_with_default.zip','testoutput' + '/data_with_default.zip' ))
        
        
    def test_write_odf_with_missings(self):
        

        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data_with_missings.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_with_missings.zip')
        
        with zipfile.ZipFile('testoutput' + '/data_with_missings.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_with_missings.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
            
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data_with_missings.zip','testoutput' + '/data_with_missings.zip' ))

    def test_write_odf_lang_standard(self):
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_de.zip', languages = "de")
        
        with zipfile.ZipFile('testoutput' + '/data_de.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_de.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data.zip','testoutput' + '/data_de.zip' ))

    def test_write_odf_lang_standard2(self):
         os.makedirs('testoutput', exist_ok=True)
         
         df = odf.read_odf(path = 'testdata/data.zip')
         
         
         odf.write_odf(x = df, path='testoutput' + '/data_de.zip', languages = ["de"])
         
         with zipfile.ZipFile('testoutput' + '/data_de.zip', 'r') as zip_file:
             self.assertTrue('data.csv' in zip_file.namelist())
             self.assertTrue('metadata.xml' in zip_file.namelist())
             rootnew=ET.fromstring(zip_file.read('metadata.xml'))
         with zipfile.ZipFile('testdata/data_de.zip', 'r') as zip_file:    
             rootorig=ET.fromstring(zip_file.read('metadata.xml'))

         # Test for element equality
         self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
         if (ET.tostring(rootorig) != ET.tostring(rootnew)):
             xml_tree_equal(rootorig, rootnew)
         # Check equality of CSV
         self.assertTrue(csvs_equal('testdata/data.zip','testoutput' + '/data_de.zip' ))

    def test_write_odf_lang_default(self):
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data_with_default.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_en_none.zip', languages = ["en", ''])
        
        with zipfile.ZipFile('testoutput' + '/data_en_none.zip', 'r') as zip_file:
            #self.assertTrue('data.csv' in zip_file.namelist())
            #self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_en_none.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
            
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data_with_default.zip','testoutput' + '/data_en_none.zip' ))
            
    def test_write_odf_lang_default2(self):
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data_with_default.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_en_none.zip', languages = ["en", None])
        
        with zipfile.ZipFile('testoutput' + '/data_en_none.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_en_none.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
            
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data_with_default.zip','testoutput' + '/data_en_none.zip' ))

    def test_write_odf_lang_with_missing(self):
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data_with_missings.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_with_missings_en.zip', languages = ["en"])
        
        with zipfile.ZipFile('testoutput' + '/data_with_missings_en.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_with_missings_en.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
         
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data_with_missings.zip','testoutput' + '/data_with_missings_en.zip' ))
        
    def test_write_odf_with_special_values(self):
        os.makedirs('testoutput', exist_ok=True)
        
        df = odf.read_odf(path = 'testdata/data_special_values.zip')
        
        
        odf.write_odf(x = df, path='testoutput' + '/data_special_values.zip')
        
        with zipfile.ZipFile('testoutput' + '/data_special_values.zip', 'r') as zip_file:
            self.assertTrue('data.csv' in zip_file.namelist())
            self.assertTrue('metadata.xml' in zip_file.namelist())
            rootnew=ET.fromstring(zip_file.read('metadata.xml'))
        with zipfile.ZipFile('testdata/data_special_values.zip', 'r') as zip_file:    
            rootorig=ET.fromstring(zip_file.read('metadata.xml'))

        # Test for element equality
        self.assertEqual(ET.tostring(rootorig), ET.tostring(rootnew))
        if (ET.tostring(rootorig) != ET.tostring(rootnew)):
            xml_tree_equal(rootorig, rootnew)
         
        # Check equality of CSV
        self.assertTrue(csvs_equal('testdata/data_special_values.zip','testoutput' + '/data_special_values.zip' ))
              
            
if __name__ == '__main__':
    unittest.main()


