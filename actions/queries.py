import pandas as pd

import database_setup

if __name__ == '__main__':

    engine_client = database_setup.ask_postgre()
    


def abc():
    #engine_client = database_setup.ask_postgre()
    query = 'select max(tottm) from disaster_processed dp limit 10'
    df_client = pd.read_sql(query, engine_client)
    
    return df_client


print(abc())