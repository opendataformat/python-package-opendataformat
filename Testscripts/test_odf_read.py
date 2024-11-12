# -*- coding: utf-8 -*-
'''
Created on Mon Nov 11 11:18:21 2024

@author: thartl
'''

import pandas as pd
import zipfile
import sys
#import opendataformat as odf
import os

sys.path.append('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/opendataformat')
import odf2pd as odf

os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts')
  
df = odf.read_odf('testdata/data.zip')

print(df) 

import unittest
#import odf  # Assuming the odf module has the read_odf function

class TestReadODF(unittest.TestCase):
    def test_read_odf_all_languages(self):
        # Load the data using read_odf with 'all' languages specified
        df = odf.read_odf('testdata/data.zip')

        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'type', 'description_en', 
            'description_de', 'url', 'labels_en', 'labels_de'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)

        # Dataset content attributes
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label_de'], 'Daten vom Personenfragebogen 2010')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description_en'], 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['description_de'], 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['url'], 'https://paneldata.org/soep-core/data/bap')

        # Variables content attributes for df.bap96
        self.assertEqual(df['bap96'].attrs['variable'], 'bap96')
        self.assertEqual(df['bap96'].attrs['label_de'], 'Körpergröße')
        self.assertEqual(df['bap96'].attrs['label_en'], 'Height')
        self.assertEqual(df['bap96'].attrs['description_de'], 'Körpergröße')
        self.assertEqual(df['bap96'].attrs['description_en'], 'Body size')
        self.assertEqual(df['bap96'].attrs['url'], 'https://paneldata.org/soep-core/data/bap/bap96')
        self.assertEqual(df['bap96'].attrs['labels_en'], {-2: 'Does not apply', -1: 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_de'], {-2: 'trifft nicht zu', -1: 'keine Angabe'})

    def test_read_odf_with_default_language(self):
        # Load the data with default language settings
        df = odf.read_odf('testdata/data_with_default.zip')

        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label', 'label_en', 'label_de', 
            'description', 'description_en', 'description_de', 'url',  
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label', 'label_en', 'label_de', 
            'type', 'description', 'description_en', 'description_de', 
            'url', 'labels', 'labels_en', 'labels_de'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)

        # Dataset content attributes
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label_de'], 'Daten vom Personenfragebogen 2010')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description_en'], 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['description_de'], 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['url'], 'https://paneldata.org/soep-core/data/bap')

        # Variables content attributes for df.bap96
        self.assertEqual(df['bap96'].attrs['variable'], 'bap96')
        self.assertEqual(df['bap96'].attrs['label'], 'Height')
        self.assertEqual(df['bap96'].attrs['label_de'], 'Körpergröße')
        self.assertEqual(df['bap96'].attrs['label_en'], 'Height')
        self.assertEqual(df['bap96'].attrs['description'], 'Body size')
        self.assertEqual(df['bap96'].attrs['description_de'], 'Körpergröße')
        self.assertEqual(df['bap96'].attrs['description_en'], 'Body size')
        self.assertEqual(df['bap96'].attrs['url'], 'https://paneldata.org/soep-core/data/bap/bap96')
        self.assertEqual(df['bap96'].attrs['labels'], {-2: 'Does not apply', -1: 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_en'], {-2: 'Does not apply', -1: 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels'], {-2: 'Does not apply', -1: 'No Answer'})

    def test_read_odf_de_language(self):
        # Load the data using read_odf with 'de' language specified
        df = odf.read_odf(file='testdata/data.zip', languages='de')

        # Expected dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_de', 
            'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df['bap87']
        expected_variable_attributes = [
            'variable', 'label_de', 
            'type', 'description_de', 
            'url', 'labels_de'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)

        # Dataset content assertions
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        
        self.assertEqual(df.attrs['description_de'], (
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich "
            "an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        ))
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")

        # Variables content assertions for df['bap96']
        self.assertEqual(df['bap96'].attrs['variable'], "bap96")
        self.assertEqual(df['bap96'].attrs['label_de'], "Körpergröße")
        self.assertEqual(df['bap96'].attrs['description_de'], "Körpergröße")
        self.assertEqual(df['bap96'].attrs['url'], "https://paneldata.org/soep-core/data/bap/bap96")

        # Label translations for df['bap96']
        self.assertEqual(df['bap96'].attrs.get('labels', None), None)
        self.assertEqual(df['bap96'].attrs.get('labels_de'), {-2: "trifft nicht zu", -1: "keine Angabe"})



if __name__ == '__main__':
    unittest.main()


