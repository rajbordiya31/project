# for Fetching data from sales table
from pooling_connection import get_cursor_connection

cur=None
con =None

cur,conn=get_cursor_connection()
if cur and conn:
    
                                        #  For retrive data


    # try:
    #     cur.execute('SELECT * FROM sale_data')
    #     rows=cur.fetchall()
    #     for row in rows:
    #         print(row)

    # except Exception as e:
    #     print("error : ",e)
    
    # finally:
    #         if cur:
    #             cur.close()
    #         if conn:
    #             conn.close()

                                         # For Inserting Data

    # def insert_data(date,amount):
    #     try:
            
    #         query='INSERT INTO sale_data (sale_date,amount) VALUES (%s,%s)'
    #         cur.execute(query,(date,amount))
    #         conn.commit()
    #         print("INSERTED : ",date,amount)
            
    #     except Exception as e:
    #         print("Error : ",e)

    #     finally:
    #         if cur:
    #             cur.close()
    #         if conn:
    #             conn.close()

    # insert_data('2024-01-04',1700)

                                            # For Delete Data

    # def delete_data(sid):
        
    #     try:
            
    #         query='DELETE FROM sale_data WHERE id=%s'
    #         cur.execute(query,(sid,))
    #         conn.commit()
    #         print(f"Deleted data of {sid} id")
            
    #     except Exception as e:
    #         print("Error : ",e)
        
    #     finally:
    #         if cur:
    #             cur.close()
    #         if conn:
    #             conn.close()
          
    # delete_data(12)

                                # For update  
    
    def update_data(sid,date,amount):
        try:
            
            query='UPDATE sale_data SET sale_date=%s,amount=%s WHERE id=%s'
            cur.execute(query,(date,amount,sid))
           
            conn.commit()
            print(f"Updated {sid} id")
            
        except Exception as e:
            print("Error : ",e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    update_data(4,'2024-01-20',3000)