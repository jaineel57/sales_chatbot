import pandas as pd

import database_setup

if __name__ == '__main__':

    engine_client = database_setup.ask_postgre()



def abc():
    engine_client = database_setup.ask_postgre()
    query = 'SELECT first_name FROM actor WHERE (actor_id = 1) '
    df_client = pd.read_sql(query, engine_client)
    temp = list(df_client.iloc[0])

    return temp[0]


#print(abc())
