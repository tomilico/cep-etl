import requests
import pandas as pd
from numpy.ma.core import get_data


def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()
    else:
        return None


users_path = "1-bronze-raw/users.csv"
users_df = pd.read_csv(users_path)

cep_list = users_df['cep'].tolist()  # pandas method to transform object in list
cep_info_list=[]

for cep in cep_list:
    cep_info = get_data(cep)
    print(cep_info)
    if "erro" in cep_info:
        continue
    cep_info_list.append(cep_info)

cep_df = pd.DataFrame(cep_info_list)

cep_df.to_csv("1-bronze-raw/cep_info.csv", index=False)
