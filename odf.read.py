

import pandas as pd
import zipfile



zf = zipfile.ZipFile('C:\\Users\\thartl\\Documents\\test.zip') 
df = pd.read_csv(zf.open('data.csv'))