import pandas as pd

import database_setup

if __name__ == '__main__':

    engine_client = database_setup.ask_postgre()



def abc():
    engine_client = database_setup.ask_postgre()
    query = 'SELECT first_name,last_name FROM actor WHERE (actor_id >= 1 and actor_id <=5) '
    df_client = pd.read_sql(query, engine_client)
    first_name_list = list(df_client['first_name'])
    last_name_list = list(df_client['last_name'])
    n = len(first_name_list)
    temp_array = []
    for i in range(0,n):
        add = first_name_list[i] + " " +  last_name_list[i]
        temp_array.append(add)

    return temp_array


#print(abc())
