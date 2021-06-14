import pandas as pd
import json as json
import database_setup


engine_client = database_setup.ask_postgre()



def total_sales():
    query = '''select sum(sales_amount)::integer as totsales  from karamschema.sales  where invoice_date >= '2021-04-01' and invoice_date <= '2021-06-01' '''
    df_client = pd.read_sql(query, engine_client)
    print("running total sales query")
    temp = list(df_client.iloc[0])
    return temp[0]



def max_customer_return_info():
    print("running max_customer_return_info query")

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



def max_client_info():

    print("running max_client_info query")

    query = '''select distinct(name), sum(sales_amount) as "Q{qnum}_{yrfilter}" 
                              from karamschema.sales as sl inner join 
                              karamschema.client_description as cd 
                              on sl.client_id = cd.client_id 
                              inner join karamschema.product_description as pd on sl.item_id = pd.item_id
                              where 
                              invoice_date >= '2021-04-01' and 
                              invoice_date <= '2021-06-30' group by name 
                              order by "Q{qnum}_{yrfilter}" desc limit 1'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return df_client["name"][0]


def region_product_info():

    print("running region_product_info query")

    query = '''select region as "Territory",round(sum(sales_amount)) from karamschema.sales as ks join karamschema.client_description as kc on ks.client_id=kc.client_id join karamschema.product_description as kp
                            on ks.item_id=kp.item_id
                            where invoice_date >= '2021-04-01' and invoice_date <= '2021-06-30'
                            group by "Territory" order by round desc limit 1'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return df_client["Territory"][0]



def total_returns():


    print("running total_returns query")

    query = '''select sum(sales_amount)::integer as totret from karamschema.sales
                            inner join karamschema.product_description as cd on 
                            sales.item_id=cd.item_id 
                            where  sales_amount < 0
                            and invoice_date >= '2021-04-01' and invoice_date <= 
                            '2021-06-30' '''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return float(abs(df_client["totret"][0]))



def returns_category_amount():
 
    engine_client = database_setup.ask_postgre()

    print("running returns_category_amount query")
    query = '''select category,sum(sales_amount)::integer as totret from karamschema.sales
                            inner join karamschema.product_description as cd on 
                            sales.item_id=cd.item_id 
                            where  sales_amount < 0
                            and invoice_date >= '2021-04-01' and invoice_date <= 
                            '2021-06-30' group by category order by totret limit 1'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return df_client["category"][0]


def returns_category_quantity():

    print("running returns_category_quantity query")

    query = '''select category,sum(quantity)::integer as totret from karamschema.sales
                            inner join karamschema.product_description as cd on 
                            sales.item_id=cd.item_id 
                            where  sales_amount < 0
                            and invoice_date >= '2021-04-01' and invoice_date <= 
                            '2021-06-30' group by category order by totret limit 1'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return float(abs(df_client["totret"][0]))


def yearly_sales_distribution_category():

    engine_client = database_setup.ask_postgre()

    print("running yearly_sales_distribution_category query")

    query = '''select * from (select distinct extract(year from date(invoice_date))::int as year ,sum(sales_amount) as "Sales"
    from karamschema.sales
  join karamschema.client_description 
  on karamschema.sales.client_id = karamschema.client_description.client_id
  join karamschema.product_description
  on karamschema.sales.item_id=karamschema.product_description.item_id
where  sales_amount>0 and extract(year from date(invoice_date)) < extract(year from now()) 
group by year order by year) as k where k.year >2019 and k.year<2022

'''
    df_client = pd.read_sql(query, engine_client)
    return df_client["Sales"][0]




def monthly_sales_distribution_category():

    print("running monthly_sales_distribution_category query")

    query = '''select foo2.month, foo2."Sales" from (
select foo.month, to_date(foo.month,'Mon-YYYY') as month_sortkey ,foo."Sales"
from (
select to_char(invoice_date, 'Mon-YYYY') as Month
, sum(sales_amount) as "Sales" from karamschema.sales 
  join karamschema.client_description 
  on karamschema.sales.client_id = karamschema.client_description.client_id
  join karamschema.product_description
  on karamschema.sales.item_id=karamschema.product_description.item_id
where sales_amount>0 and invoice_date>= '2021-04-01' and invoice_date <='2021-06-30'
group by Month order by Month asc) as foo order by month_sortkey) as foo2'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return df_client["Sales"][0]


def dealer_sales_info():
        
    print("running dealer_sales_info query")
    
    query = '''select upper(item_code) as "Item Code", sum(sales_amount) as "Sales"
from karamschema.sales 
join karamschema.client_description 
  on karamschema.sales.client_id = karamschema.client_description.client_id
  join karamschema.product_description
  on karamschema.sales.item_id=karamschema.product_description.item_id
  where invoice_date >= '2021-04-01' and invoice_date <= 
                            '2021-06-30'
  group by "Item Code" order by "Sales" desc 
  limit 1'''
    df_client = pd.read_sql(query, engine_client)
#    temp = list(df_client.iloc[0])
    return df_client["Item Code"][0]





if __name__ == '__main__':

    dic={
    "max_customer_return_info":max_customer_return_info(),"total_sales":total_sales(),
    "max_client_info":max_client_info(),"region_product_info":region_product_info(),
    "total_returns":total_returns(),"returns_category_amount":returns_category_amount(),
    "returns_category_quantity":returns_category_quantity(),
    "yearly_sales_distribution_category":yearly_sales_distribution_category(),"monthly_sales_distribution_category":monthly_sales_distribution_category(),
    "dealer_sales_info":dealer_sales_info()
    }
    print("creating json object")
    json_object = json.dumps(dic, indent = 4)
    print("dumping json into local")  
    with open("karam_data_dump.json", "w") as fp:
        json.dump(dic,fp)
    print("data dumping done, json is created")
