import pandas as pd
import json as json
import database_setup






def total_sales():
    engine_client = database_setup.ask_postgre()
    query = '''select sum(sales_amount)::integer as totsales  from karamschema.sales  where invoice_date >= '2021-04-01' and invoice_date <= '2021-06-01' '''
    df_client = pd.read_sql(query, engine_client)
    temp = list(df_client.iloc[0])
    return str(temp[0])

def change_sales():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client

def clients_info():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client

def max_client_info():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client



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


def region_product_info():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client

def total_returns():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client


def returns_category_amount():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client

def returns_category_quantity():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client


def yearly_sales_distribution_category():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client

def monthly_sales_distribution_category():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client


def dealer_sales_info():
    engine_client = database_setup.ask_postgre()
    query = ""
    df_client = pd.read_sql(query, engine_client)

    return df_client



def convert_json():

    engine_client = database_setup.ask_postgre()
    dic={"total_sales":total_sales(),"change_sales":change_sales(),"clients_info":clients_info(),"max_client_info":max_client_info(),"max_customer_return_info":max_customer_return_info()
    ,"region_product_info":region_product_info(),"total_returns":total_returns(),"returns_category_amount":returns_category_amount(),
    "returns_category_quantity":returns_category_quantity(),"yearly_sales_distribution_category":yearly_sales_distribution_category(),
    "monthly_sales_distribution_category":monthly_sales_distribution_category(),"dealer_sales_info":dealer_sales_info()}
    json_object = json.dumps(dic, indent = 4)
    with open(json_object, "w") as fp:
        json.dump(dic,fp)


    return json_object
