import os
import pandas as pd

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '..', 'data-set', 'patients-data.csv')

raw_data = pd.read_csv(file_path)
data = raw_data
for arquivo in os.listdir(os.path.join(script_dir,'..','data-set')):
    if arquivo.endswith('_discretizacao.csv'):
        df = pd.read_csv(os.path.join(script_dir, '..', 'data-set', arquivo))
        mapping = df.set_index(df.columns[0])['ID'].to_dict()
        data[df.columns[0]] = data[df.columns[0]].map(mapping)

classes = data['PatientID']
features = data.drop(columns=['PatientID'])

