# -*- coding: utf-8 -*-
'''
Created on Mon Nov 11 11:18:21 2024

@author: thartl
'''

#import pandas as pd
import pandas.testing as pd_testing
import unittest

#import zipfile
#import sys
import opendataformat as odf
import os

#sys.path.append('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/opendataformat')
#import odf2pd as odf

os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts')



class TestReadODF(unittest.TestCase):
    def test_read_odf_all_languages_v100(self):
        # Load the data using read_odf with 'all' languages specified
        df = odf.read_odf(filepath = 'testdata/data.odf.zip')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        
        
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)


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
        self.assertEqual(df['bap87'].attrs['label_en'], 'Current Health')
        self.assertEqual(df['bap96'].attrs['description_de'], 'Körpergröße')
        self.assertEqual(df['bap96'].attrs['description_en'], 'Body size')
        self.assertEqual(df['bap96'].attrs['url'], 'https://paneldata.org/soep-core/data/bap/bap96')
        self.assertEqual(df['bap96'].attrs['labels_en'], {'-2': 'Does not apply', '-1': 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_de'], {'-2': 'trifft nicht zu', '-1': 'keine Angabe'})
        
        
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_en': 'Firstname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])

    def test_read_odf_with_default_language(self):
        # Load the data with default language settings
        df = odf.read_odf('testdata/data_with_default.odf.zip')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

    
        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label', 'label_en', 'label_de', 
            'description', 'description_en', 'description_de', 'url',  
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label', 'label_en', 'label_de', 
            'description', 'description_en', 'description_de', 
            'labels', 'labels_en', 'labels_de', 'type', 'url'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)

        # Dataset content attributes
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['label_de'], 'Daten vom Personenfragebogen 2010')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description'], 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
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
        self.assertEqual(df['bap96'].attrs['labels'], {'-2': 'Does not apply', '-1': 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_en'], {'-2': 'Does not apply', '-1': 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_de'], {'-2': 'trifft nicht zu', '-1': 'keine Angabe'})


    def test_read_odf_with_missings(self):
        # Load the data with default language settings
        df = odf.read_odf('testdata/data_with_missings.odf.zip')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

    
        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 
            'description_de', 'url',  
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 
            'description_de', 
            'labels_en', 'labels_de', 'type', 'url'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)

        # Dataset content attributes
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description_de'], 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['url'], '')

        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': None,
                    '-1': None,
                    '1': 'Very good',
                    '2': 'Good',
                    '3': 'Satisfactory',
                    '4': 'Poor',
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe',
                    '1': 'Sehr gut',
                    '2': 'Gut',
                    '3': 'Zufriedenstellend',
                    '4': 'Weniger gut',
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': None,
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer',
                    '1': 'Always',
                    '2': 'Often',
                    '3': 'Sometimes',
                    '4': 'Almost Never',
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe',
                    '1': 'Immer',
                    '2': 'Oft',
                    '3': None,
                    '4': None,
                    '5': None
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': None,
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer',
                    '1': 'Always',
                    '2': 'Often',
                    '3': 'Sometimes',
                    '4': 'Almost Never',
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe',
                    '1': 'Immer',
                    '2': 'Oft',
                    '3': 'Manchmal',
                    '4': 'Fast nie',
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_de': None,
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer',
                    '1': 'Always',
                    '2': 'Often',
                    '3': 'Sometimes',
                    '4': 'Almost Never',
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': None,
                    '-1': None,
                    '1': None,
                    '2': None,
                    '3': None,
                    '4': None,
                    '5': None
                },
                'type': 'numeric',
                'url': ''
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': ''
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])


    def test_read_odf_de_language(self):
        # Load the data using read_odf with 'de' language specified
        df = odf.read_odf(filepath = 'testdata/data.odf.zip', languages='de')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

    
        # Expected dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_de', 
            'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for variables
        expected_variable_attributes = [
            'variable', 'label_de', 
            'description_de', 'labels_de', 'type', 'url'
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
        self.assertEqual(df['bap96'].attrs.get('labels_de'), {'-2': "trifft nicht zu", '-1': "keine Angabe"})

    def test_read_odf_unzipped(self):
        # Load the data using read_odf with 'de' language specified
        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data_unzipped",
            languages = "en",
            nrows = 13,
            skiprows = 3,
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns

        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 
            'description_en', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'description_en', 
            'labels_en', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'description_en': 'Question: How would you describe your current health?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'description_en': 'Frequency of feeling balance',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'description_en': 'Body size',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])

    def test_read_odf_specific_rows(self):
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows=10
        )
        
        self.assertEqual(df.shape, (10, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Variable attributes for variables
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)



        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")
        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the "
            "questionnaire \"Living in Germany - Survey 2010 on the social "
            "situation - Personal questionnaire for all. This questionnaire is "
            "addressed to the individual persons in the household. A view of the "
            "survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/"
            "soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des "
            "Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen "
            "Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen "
            "richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht "
            "des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/"
            "soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")

        # Variable content
     
        
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_en': 'Firstname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])
        
    
    def test_read_odf_skiprows_nrows(self):
        # Set maximum difference to None to display full diff on failure

        # Call the odf.read_odf function with a test file
        df = odf.read_odf('testdata/data.odf.zip',
                          nrows = 13,
                          skiprows= 3)


        self.assertEqual(df.shape, (13, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        
        # Check attributes for each variable in df
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset-level attribute values
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label_de'], 'Daten vom Personenfragebogen 2010')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description_en'], 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['description_de'], 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['url'], 'https://paneldata.org/soep-core/data/bap')
        
        
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_en': 'Firstname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])

    def test_read_odf_specific_variables_index(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            usecols=[1, 2, 4, 5]
        )
        
        self.assertEqual(df.shape, (20, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap9201', 'bap9001', 'bap9003', 'bap96'])  # columns
    
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset content and attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        
    def test_read_odf_specific_variables_names(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data_unzipped",
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (20, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns
    
    
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        
    def test_read_odf_specific_rows_columns(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=[1, 2, 4, 5]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap9201', 'bap9001', 'bap9003', 'bap96'])  # columns
        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])                                     
       
    def test_read_odf_specific_rows_columns2(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns

        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])                                     
    
    def test_read_odf_specific_rows_columns_language(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            languages = "en",
            nrows = 13,
            skiprows = 3,
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns

        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 
            'description_en', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'description_en', 
            'labels_en', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'description_en': 'Question: How would you describe your current health?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'description_en': 'Frequency of feeling balance',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'description_en': 'Body size',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])

    def test_read_odf_nas(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=[1, 2, 4, 5],
            na_values=list(range(-2,0))
        )
        
        df2 = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=[1, 2, 4, 5]
        )
        
        
        pd_testing.assert_frame_equal(((df2 < 0) | df.isna()), df.isna())  # Check number of rows and columns


        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap9201', 'bap9001', 'bap9003', 'bap96'])  # columns
        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        

        
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96']) 

        df3 = odf.read_odf(
            filepath = "testdata/data.zip",
            skiprows = 3,
            usecols=[1, 2, 4, 5, 6],
            na_values=list(range(-2,0))
        )
        df4 = odf.read_odf(
            filepath = "testdata/data.zip",
            skiprows = 3,
            usecols=[1, 2, 4, 5, 6]
        )
        neg_values = list((df4['name'] == '-1') | (df4['name'] == '-2') | df4['name'].isna())
        na_values = list(df3['name'].isna())
        
        self.assertEqual(neg_values, na_values)  # Check number of rows and columns 
        
        
    ################################# Tests for old file fersions
    def test_read_odf_all_languages_v100(self):
        # Load the data using read_odf with 'all' languages specified
        df = odf.read_odf(filepath = 'testdata/data.zip')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        
        
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)


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
        self.assertEqual(df['bap87'].attrs['label_en'], 'Current Health')
        self.assertEqual(df['bap96'].attrs['description_de'], 'Körpergröße')
        self.assertEqual(df['bap96'].attrs['description_en'], 'Body size')
        self.assertEqual(df['bap96'].attrs['url'], 'https://paneldata.org/soep-core/data/bap/bap96')
        self.assertEqual(df['bap96'].attrs['labels_en'], {'-2': 'Does not apply', '-1': 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_de'], {'-2': 'trifft nicht zu', '-1': 'keine Angabe'})
        
        
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_en': 'Firstname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])

    def test_read_odf_with_default_language_v100(self):
        # Load the data with default language settings
        df = odf.read_odf('testdata/data_with_default.zip')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

    
        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label', 'label_en', 'label_de', 
            'description', 'description_en', 'description_de', 'url',  
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label', 'label_en', 'label_de', 
            'description', 'description_en', 'description_de', 
            'labels', 'labels_en', 'labels_de', 'type', 'url'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)

        # Dataset content attributes
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['label_de'], 'Daten vom Personenfragebogen 2010')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description'], 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
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
        self.assertEqual(df['bap96'].attrs['labels'], {'-2': 'Does not apply', '-1': 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_en'], {'-2': 'Does not apply', '-1': 'No Answer'})
        self.assertEqual(df['bap96'].attrs['labels_de'], {'-2': 'trifft nicht zu', '-1': 'keine Angabe'})


    def test_read_odf_with_missings_v100(self):
        # Load the data with default language settings
        df = odf.read_odf('testdata/data_with_missings.zip')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

    
        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 
            'description_de', 'url',  
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for df.bap87
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 
            'description_de', 
            'labels_en', 'labels_de', 'type', 'url'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        expected_variable_attributes = [
            'variable',
            'label_en',
            'label_de',
            'description_de',
            'labels_en',
            'labels_de',
            'type',
            'url']
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)

        # Dataset content attributes
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description_de'], 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['url'], '')

        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': None,
                    '-1': None,
                    '1': 'Very good',
                    '2': 'Good',
                    '3': 'Satisfactory',
                    '4': 'Poor',
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe',
                    '1': 'Sehr gut',
                    '2': 'Gut',
                    '3': 'Zufriedenstellend',
                    '4': 'Weniger gut',
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': None,
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer',
                    '1': 'Always',
                    '2': 'Often',
                    '3': 'Sometimes',
                    '4': 'Almost Never',
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe',
                    '1': 'Immer',
                    '2': 'Oft',
                    '3': None,
                    '4': None,
                    '5': None
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': None,
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer',
                    '1': 'Always',
                    '2': 'Often',
                    '3': 'Sometimes',
                    '4': 'Almost Never',
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe',
                    '1': 'Immer',
                    '2': 'Oft',
                    '3': 'Manchmal',
                    '4': 'Fast nie',
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': ''
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_de': None,
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer',
                    '1': 'Always',
                    '2': 'Often',
                    '3': 'Sometimes',
                    '4': 'Almost Never',
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': None,
                    '-1': None,
                    '1': None,
                    '2': None,
                    '3': None,
                    '4': None,
                    '5': None
                },
                'type': 'numeric',
                'url': ''
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': ''
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply',
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu',
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])


    def test_read_odf_de_language_v100(self):
        # Load the data using read_odf with 'de' language specified
        df = odf.read_odf(filepath = 'testdata/data.zip', languages='de')
        
        self.assertEqual(df.shape, (20, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

    
        # Expected dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_de', 
            'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)

        # Variable attributes for variables
        expected_variable_attributes = [
            'variable', 'label_de', 
            'description_de', 'labels_de', 'type', 'url'
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
        self.assertEqual(df['bap96'].attrs.get('labels_de'), {'-2': "trifft nicht zu", '-1': "keine Angabe"})

    def test_read_odf_unzipped_v100(self):
        # Load the data using read_odf with 'de' language specified
        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data_unzipped",
            languages = "en",
            nrows = 13,
            skiprows = 3,
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns

        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 
            'description_en', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'description_en', 
            'labels_en', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'description_en': 'Question: How would you describe your current health?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'description_en': 'Frequency of feeling balance',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'description_en': 'Body size',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])

    def test_read_odf_specific_rows_v100(self):
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows=10
        )
        
        self.assertEqual(df.shape, (10, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

        # Dataset attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url', 
        ]
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Variable attributes for variables
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)



        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")
        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the "
            "questionnaire \"Living in Germany - Survey 2010 on the social "
            "situation - Personal questionnaire for all. This questionnaire is "
            "addressed to the individual persons in the household. A view of the "
            "survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/"
            "soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des "
            "Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen "
            "Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen "
            "richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht "
            "des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/"
            "soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")

        # Variable content
     
        
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_en': 'Firstname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])
        
    
    def test_read_odf_skiprows_nrows_v100(self):
        # Set maximum difference to None to display full diff on failure

        # Call the odf.read_odf function with a test file
        df = odf.read_odf('testdata/data.zip',
                          nrows = 13,
                          skiprows= 3)


        self.assertEqual(df.shape, (13, 7))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap9201', 'bap9001', 'bap9002', 'bap9003', 'bap96', 'name'])  # columns

        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        
        # Check attributes for each variable in df
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['name'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset-level attribute values
        self.assertEqual(df.attrs['dataset'], 'bap')
        self.assertEqual(df.attrs['label_de'], 'Daten vom Personenfragebogen 2010')
        self.assertEqual(df.attrs['label_en'], 'Data from individual questionnaires 2010')
        self.assertEqual(df.attrs['description_en'], 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['description_de'], 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf')
        self.assertEqual(df.attrs['url'], 'https://paneldata.org/soep-core/data/bap')
        
        
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            },
            'name': {
                'variable': 'name',
                'label_en': 'Firstname',
                'label_de': 'Vorname',
                'description_en': 'Firstname',
                'description_de': 'Vorname',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'character',
                'url': ''
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        self.assertEqual(df['name'].attrs, expected_metadata['name'])

    def test_read_odf_specific_variables_index_v100(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            usecols=[1, 2, 4, 5]
        )
        
        self.assertEqual(df.shape, (20, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap9201', 'bap9001', 'bap9003', 'bap96'])  # columns
    
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset content and attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        
    def test_read_odf_specific_variables_names_v100(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data_unzipped",
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (20, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns
    
    
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])
        
    def test_read_odf_specific_rows_columns_v100(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=[1, 2, 4, 5]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap9201', 'bap9001', 'bap9003', 'bap96'])  # columns
        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])                                     
       
    def test_read_odf_specific_rows_columns2_v100(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns

        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'label_de': 'Gesundheitszustand gegenwärtig',
                'description_en': 'Question: How would you describe your current health?',
                'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Sehr gut', 
                    '2': 'Gut', 
                    '3': 'Zufriedenstellend', 
                    '4': 'Weniger gut', 
                    '5': 'Schlecht'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'label_de': 'Niedergeschlagen letzten 4 Wochen',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'description_de': 'Häufigkeit der Niedergeschlagenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])                                     
    
    def test_read_odf_specific_rows_columns_language_v100(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            languages = "en",
            nrows = 13,
            skiprows = 3,
            usecols=["bap87", "bap96", "bap9002", "bap9003"]
        )
        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap87', 'bap96', 'bap9002', 'bap9003'])  # columns

        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 
            'description_en', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'description_en', 
            'labels_en', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap87'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9002'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap87': {
                'variable': 'bap87',
                'label_en': 'Current Health',
                'description_en': 'Question: How would you describe your current health?',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Very good', 
                    '2': 'Good', 
                    '3': 'Satisfactory', 
                    '4': 'Poor', 
                    '5': 'Bad'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap87'
            },
            'bap9002': {
                'variable': 'bap9002',
                'label_en': 'Run-down, Melancholy Last 4 Weeks',
                'description_en': 'Frequency of feeling a sad and depressed state',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9002'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'description_en': 'Frequency of feeling balance',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'description_en': 'Body size',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        
        self.assertEqual(df['bap87'].attrs, expected_metadata['bap87'])
        self.assertEqual(df['bap9002'].attrs, expected_metadata['bap9002'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96'])

    def test_read_odf_nas_v100(self):

        # Call the odf.read_odf function with a test file and selected columns
        df = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=[1, 2, 4, 5],
            na_values=list(range(-2,0))
        )
        
        df2 = odf.read_odf(
            filepath = "testdata/data.zip",
            nrows = 13,
            skiprows = 3,
            usecols=[1, 2, 4, 5]
        )
        
        
        pd_testing.assert_frame_equal(((df2 < 0) | df.isna()), df.isna())  # Check number of rows and columns


        
        self.assertEqual(df.shape, (13, 4))  # Check number of rows and columns
        self.assertEqual(list(df.columns), ['bap9201', 'bap9001', 'bap9003', 'bap96'])  # columns
        
        # Define expected dataset-level attributes
        expected_dataset_attributes = [
            'study', 'dataset', 'label_en', 'label_de', 
            'description_en', 'description_de', 'url'
        ]

        # Check if df.attrs contains the expected dataset-level attributes
        self.assertEqual(list(df.attrs.keys()), expected_dataset_attributes)
        
        # Define expected variable-level attributes
        expected_variable_attributes = [
            'variable', 'label_en', 'label_de', 'description_en', 
            'description_de', 'labels_en', 'labels_de', 'type', 'url'
        ]
        # caeck variable attributes for each variable
        self.assertEqual(list(df['bap9201'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9001'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap9003'].attrs.keys()), expected_variable_attributes)
        self.assertEqual(list(df['bap96'].attrs.keys()), expected_variable_attributes)
        
        # Verify specific dataset attributes
        self.assertEqual(df.attrs['dataset'], "bap")
        self.assertEqual(df.attrs['label_de'], "Daten vom Personenfragebogen 2010")
        self.assertEqual(df.attrs['label_en'], "Data from individual questionnaires 2010")

        self.assertEqual(
            df.attrs['description_en'],
            "The data were collected as part of the SOEP-Core study using the questionnaire "
            "\"Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. "
            "This questionnaire is addressed to the individual persons in the household. "
            "A view of the survey instrument can be found here: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(
            df.attrs['description_de'],
            "Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – "
            "Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet "
            "sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: "
            "https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf"
        )
        self.assertEqual(df.attrs['url'], "https://paneldata.org/soep-core/data/bap")


        # Verify variable attributes 
        expected_metadata = {
            'bap9201': {
                'variable': 'bap9201',
                'label_en': 'hours of sleep, normal workday',
                'label_de': 'Stunden Schlaf, normaler Werktag',
                'description_en': 'Sleep hours per weekday',
                'description_de': 'Schlafstunden pro Wochentag',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9201'
            },
            'bap9001': {
                'variable': 'bap9001',
                'label_en': 'Pressed For Time Last 4 Weeks',
                'label_de': 'Eile, Zeitdruck letzten 4 Wochen',
                'description_en': 'Frequency of feeling time pressure in the past 4 weeks',
                'description_de': 'Häufigkeit des Gefühls von Zeitdruck in den letzten 4 Wochen',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9001'
            },
            'bap9003': {
                'variable': 'bap9003',
                'label_en': 'Well-balanced Last 4 Weeks',
                'label_de': 'Ausgeglichen letzten 4 Wochen',
                'description_en': 'Frequency of feeling balance',
                'description_de': 'Häufigkeit der Ausgeglichenheit',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer', 
                    '1': 'Always', 
                    '2': 'Often', 
                    '3': 'Sometimes', 
                    '4': 'Almost Never', 
                    '5': 'Never'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe', 
                    '1': 'Immer', 
                    '2': 'Oft', 
                    '3': 'Manchmal', 
                    '4': 'Fast nie', 
                    '5': 'Nie'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap9003'
            },
            'bap96': {
                'variable': 'bap96',
                'label_en': 'Height',
                'label_de': 'Körpergröße',
                'description_en': 'Body size',
                'description_de': 'Körpergröße',
                'labels_en': {
                    '-2': 'Does not apply', 
                    '-1': 'No Answer'
                },
                'labels_de': {
                    '-2': 'trifft nicht zu', 
                    '-1': 'keine Angabe'
                },
                'type': 'numeric',
                'url': 'https://paneldata.org/soep-core/data/bap/bap96'
            }
        }
        
        

        
        self.assertEqual(df['bap9201'].attrs, expected_metadata['bap9201'])
        self.assertEqual(df['bap9001'].attrs, expected_metadata['bap9001'])
        self.assertEqual(df['bap9003'].attrs, expected_metadata['bap9003'])
        self.assertEqual(df['bap96'].attrs, expected_metadata['bap96']) 

        df3 = odf.read_odf(
            filepath = "testdata/data.zip",
            skiprows = 3,
            usecols=[1, 2, 4, 5, 6],
            na_values=list(range(-2,0))
        )
        df4 = odf.read_odf(
            filepath = "testdata/data.zip",
            skiprows = 3,
            usecols=[1, 2, 4, 5, 6]
        )
        neg_values = list((df4['name'] == '-1') | (df4['name'] == '-2') | df4['name'].isna())
        na_values = list(df3['name'].isna())
        
        self.assertEqual(neg_values, na_values)  # Check number of rows and columns                             
        
if __name__ == '__main__':
    unittest.main()