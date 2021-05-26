import pandas as pd

import database_setup

if __name__ == '__main__':

    engine_client = database_setup.ask_postgre()

    
    table_name = input('\nInput the table name to fetch:\n')
    query = 'select * from {}'.format(table_name)
    df_client = pd.read_sql(query, engine_client)

