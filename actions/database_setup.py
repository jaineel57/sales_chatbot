from sqlalchemy import create_engine



def ask_postgre():
    host = input('\nPlease enter the host number: like: 127.0.0.1\n')
    db_name = input('\nPlease enter the db name: like: master\n')
    user = input('\nPlease enter the username: like: test_user\n')
    password = input('\nPlease enter the password: like: password\n')
    db_string = "postgres+psycopg2://{}:{}@{}/{}".format(user, password,
                                                         host,
                                                         db_name)
    engine = create_engine(db_string)
    return engine



