from sqlalchemy import create_engine



def ask_postgre():

    db_string = "postgres+psycopg2://postgres:1234@localhost/dvdrental"#.format(user, password,host,db_name)
    print("connecting to db")
    engine = create_engine(db_string)
    print("engine connected")
    return engine
