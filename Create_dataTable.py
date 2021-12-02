import sys
import os
sys.path.append('Z:\\python3.8\\Lib\\site-packages')
import sqlite3
import shutil
import pandas as pd 



os.chdir('Z:\Aseren\REST_API')
conn = sqlite3.connect('GeneticGroup_Akshaydatabase.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved


c.execute('''CREATE TABLE PEOPLE
            ([fname] String PRIMARY KEY, [lname] nchar)''')

conn.commit()