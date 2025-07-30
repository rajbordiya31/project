from mysql.connector import pooling

db_config={
'host':'localhost',
'port':3306,
'user':'root',
'password':'Root@123',
'database':'practice'
}

# CREATE CONNECTION POOLING
pool=pooling.MySQLConnectionPool(
    pool_name='mypool',
    pool_size=10,
    pool_reset_session= True,
    **db_config
)

def get_cursor_connection():

    try:
        conn =pool.get_connection()
        cur= conn.cursor()
        return cur, conn

    except Exception as e:
        print ("Error : ",e)
        return None, None
    

