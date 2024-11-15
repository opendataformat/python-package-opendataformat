# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:26:14 2024

@author: thartl
"""


import unittest


#import opendataformat as odf
import os
import opendataformat as odf

os.chdir('C:/Users/thartl/OneDrive - DIW Berlin/Open Data Format Project/Python/python-package-opendataformat/Testscripts')
  

#odf.write_odf(x, path)
#odf.read_odf(xpath)





class TestDocuODF(unittest.TestCase):
    def test_write_odf_default_args(self):
        
        df = odf.read_odf(path = 'testdata/data.zip')
        docu_odf(df)  
        df = odf.read_odf('testdata/data_with_default.zip')
        docu_odf(df)  
        df = odf.read_odf('testdata/data_with_missings.zip')
        docu_odf(df)  
        
        df = odf.read_odf(path = 'testdata/data.zip')
        docu_odf(df['bap87'])  
        df = odf.read_odf('testdata/data_with_default.zip')
        docu_odf(df['bap87'])  
        df = odf.read_odf('testdata/data_with_missings.zip')
        docu_odf(df['bap87'])  
    def test_write_odf_lang(self):
        
        df = odf.read_odf(path = 'testdata/data.zip')
        docu_odf(df, languages = 'de')  
        df = odf.read_odf('testdata/data_with_default.zip')
        docu_odf(df, languages = [None, 'en'])  
        docu_odf(df, languages = '')  
        df = odf.read_odf('testdata/data_with_missings.zip')
        docu_odf(df, languages = ['de', 'en'])  
        
        df = odf.read_odf(path = 'testdata/data.zip')
        docu_odf(df['bap87'], languages = ['de'])  
        df = odf.read_odf('testdata/data_with_default.zip')
        docu_odf(df['bap87'], languages = [None, 'en'])  
        df = odf.read_odf('testdata/data_with_missings.zip')
        docu_odf(df['bap87'], languages = ['de', 'en'])
        
    def test_write_odf_metadata(self):
        self.maxDiff = None
        df = odf.read_odf(path = 'testdata/data.zip')
        self.assertEqual(docu_odf(df, metadata = 'labels'), 
                         {'label_en': 'Data from individual questionnaires 2010',
                          'label_de': 'Daten vom Personenfragebogen 2010'})
        self.assertEqual(docu_odf(df, metadata = 'type'), {})
        df = odf.read_odf('testdata/data_with_default.zip')
        self.assertEqual(docu_odf(df, metadata = 'description'), 
                         {'description': 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf',
                          'description_en': 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf',
                          'description_de': 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf'})  
        self.assertEqual(docu_odf(df, metadata = 'url'), 
                         'https://paneldata.org/soep-core/data/bap')  
        df = odf.read_odf('testdata/data_with_missings.zip')
        self.assertEqual(docu_odf(df, metadata = 'Label'),
                         'Data from individual questionnaires 2010')
        
        df = odf.read_odf(path = 'testdata/data.zip')
        self.assertEqual(docu_odf(x = df['bap87'], metadata = 'Label'),  
                         {'label_en': 'Current Health', 'label_de': 'Gesundheitszustand gegenwärtig'})  
        self.assertEqual(docu_odf(x = df['bap87'], metadata = 'type'), 
                         'numeric')
        df = odf.read_odf('testdata/data_with_default.zip')
        self.assertEqual(docu_odf(df['bap87'], metadata = 'description'),
                         {'description': 'Question: How would you describe your current health?',
                          'description_en': 'Question: How would you describe your current health?',
                          'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?'})
        self.assertEqual(docu_odf(x = df['bap87'], metadata = 'Value Label'),
                         {'labels': {'-2': 'Does not apply',
                           '-1': 'No Answer',
                           '1': 'Very good',
                           '2': 'Good',
                           '3': 'Satisfactory',
                           '4': 'Poor',
                           '5': 'Bad'},
                          'labels_en': {'-2': 'Does not apply',
                           '-1': 'No Answer',
                           '1': 'Very good',
                           '2': 'Good',
                           '3': 'Satisfactory',
                           '4': 'Poor',
                           '5': 'Bad'},
                          'labels_de': {'-2': 'trifft nicht zu',
                           '-1': 'keine Angabe',
                           '1': 'Sehr gut',
                           '2': 'Gut',
                           '3': 'Zufriedenstellend',
                           '4': 'Weniger gut',
                           '5': 'Schlecht'}})
        df = odf.read_odf('testdata/data_with_missings.zip')
        self.assertEqual(docu_odf(df['bap87'], metadata = 'url'), '')    
        self.assertEqual(docu_odf(df['bap87'], metadata = 'label'), 
                         {'label_en': 'Current Health', 'label_de': 'Gesundheitszustand gegenwärtig'})      
        
    def test_write_odf_metadata_lang(self):
        self.maxDiff = None
        df = odf.read_odf(path = 'testdata/data.zip')
        self.assertEqual(docu_odf(df, metadata = 'labels', languages = 'de'),
                         'Daten vom Personenfragebogen 2010')
        self.assertEqual(docu_odf(df, metadata = 'type', languages = ['en', 'de']), 'Not found')
        df = odf.read_odf('testdata/data_with_default.zip')
        self.assertEqual(docu_odf(df, metadata = 'description', languages = [None, 'de']), 
                         {'description': 'The data were collected as part of the SOEP-Core study using the questionnaire "Living in Germany - Survey 2010 on the social situation - Personal questionnaire for all. This questionnaire is addressed to the individual persons in the household. A view of the survey instrument can be found here: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf',
                          'description_de': 'Die Daten wurden im Rahmen der Studie SOEP-Core mittels des Fragebogens „Leben in Deutschland – Befragung 2010 zur sozialen Lage - Personenfragebogen für alle“ erhoben. Dieser Fragebogen richtet sich an die einzelnen Personen im Haushalt. Eine Ansicht des Erhebungsinstrumentes finden Sie hier: https://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.369781.de/soepfrabo_personen_2010.pdf'})  
        df = odf.read_odf('testdata/data_with_missings.zip')
        self.assertEqual(docu_odf(df, metadata = 'Label', languages = ['de']),
                         'Not found')
        
        df = odf.read_odf(path = 'testdata/data.zip')
        self.assertEqual(docu_odf(x = df['bap87'], metadata = 'Label', languages = 'en'),  
                         'Current Health')  
        self.assertEqual(docu_odf(x = df['bap87'], metadata = 'type', languages = 'fr'), 
                         'numeric')
        df = odf.read_odf('testdata/data_with_default.zip')
        self.assertEqual(docu_odf(df['bap87'], metadata = 'description', languages = ['en', 'de']),
                         {'description_en': 'Question: How would you describe your current health?',
                          'description_de': 'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?'})
        self.assertEqual(docu_odf(x = df['bap87'], metadata = 'Value Label', languages = 'en'),
                         {'-2': 'Does not apply',
                          '-1': 'No Answer',
                          '1': 'Very good',
                          '2': 'Good',
                          '3': 'Satisfactory',
                          '4': 'Poor',
                          '5': 'Bad'})
        df = odf.read_odf('testdata/data_with_missings.zip')
        self.assertEqual(docu_odf(df['bap87'], metadata = 'url', languages = 'en'), '')    
        self.assertEqual(docu_odf(df['bap87'], metadata = 'description', languages = 'de'), 
                         'Frage: Wie würden Sie Ihren gegenwärtigen Gesundheitszustand beschreiben?')       
                        
            
if __name__ == '__main__':
    unittest.main()
