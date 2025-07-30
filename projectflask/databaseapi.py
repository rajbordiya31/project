from dbConnection.pooling_connection import get_cursor_connection
from flask import Flask, jsonify

app= Flask(__name__)
cur=None
con =None

cur,conn=get_cursor_connection()

if cur and conn:
    @app.route('/sale')
    def get_sale():
        try:
            query='SELECT * FROM sale_data'
            cur.execute(query)
            rows=cur.fetchall()
            
            return jsonify(rows)
                
        except Exception as e:
            print("Error is : ",e)
        
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

if __name__ == '__main__': 
    app.run(debug = True)