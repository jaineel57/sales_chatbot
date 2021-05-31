import pandas as pd
import json as json
import database_setup






def total_sales():
    engine_client = database_setup.ask_postgre()
    query = '''select sum(sales_amount)::integer as totsales  from karamschema.sales  where invoice_date >= '2021-04-01' and invoice_date <= '2021-06-01' '''
    df_client = pd.read_sql(query, engine_client)
    temp = list(df_client.iloc[0])
    return str(temp[0])


def max_customer_return_info():
    engine_client = database_setup.ask_postgre()
    query = '''select distinct(name), abs(sum(sales_amount)) as "Q{qnum}_{yrfilter}"
                          from karamschema.sales as sl inner join
                          karamschema.client_description as cd
                          on sl.client_id = cd.client_id
                          inner join karamschema.product_description as pd
                          on pd.item_id = sl.item_id where
                          invoice_date >= '2021-04-01' and
                          invoice_date <= '2021-06-30' and
                          quantity < 0  group by name
                          order by "Q{qnum}_{yrfilter}" desc limit 1'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return df_client["name"][0]





def convert_json():

    engine_client = database_setup.ask_postgre()
    dic={"max_customer_return_info":max_customer_return_info(),"total_sales":total_sales()
    }
    json_object = json.dumps(dic, indent = 4)
    with open(json_object, "w") as fp:
        json.dump(dic,fp)
    # max_customer_return_info()
    # total_sales()


    return json_object
