from dbConnection.pooling_connection import get_cursor_connection
from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/insert',methods=['POST'])

def add_student():
    data=request.get_json()
    id=data.get("id")
    name=data.get("name")
    age=data.get("age")
    mob=data.get("mob")

    cur,conn= get_cursor_connection()
    print("Connection stablished")
    if not cur:
         print("Connection Failed")
         return jsonify({"Error":"DB Connection Failed"})
    
    try:
        cur.execute("INSERT INTO studentinfo(id,name,age,mob_num) VALUES (%s,%s,%s,%s)",(id,name,age,mob))
        print("query Executed")
        conn.commit()
        return jsonify({"Message":"Student add succesfully"})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"Error":str(e)})
    
    finally:
        cur.close()
        conn.close()

@app.route('/reterive',methods=['GET'])

def get_data():
    print("Inside")
    
    cur,conn=get_cursor_connection()
    print("Connection stablished")
    if not cur:
        print("Connection Failed")
        return({"Error":"DB connection failed"})
    
    try:
        cur.execute("SELECT * FROM studentinfo")
        rows=cur.fetchall()
        print("query Executed")
        return jsonify(rows)
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"Error":str(e)})
    
    finally:
        cur.close()
        conn.close()

@app.route('/update/<int:id>',methods=['PUT'])
def update_data(id):
    
    data=request.get_json()

    name=data.get("name")
    age=data.get("age")
    mob=data.get("mob")

    cur,conn=get_cursor_connection()
    if not cur:
        return({"Error":"DB connection Failed"})
    try:
        cur.execute("UPDATE studentinfo SET name=%s,age=%s,mob_num=%s Where id=%s",(name,age,mob,id))
        conn.commit()
        return jsonify({"Message":"Updated Successfully"})
    
    except Exception as e:
        return jsonify({"Error":str(e)})
    
    finally:
        cur.close()
        conn.close()
    
@app.route('/delete/<int:id>',methods=['DELETE'])
def deletee_data(id):
    
    cur,conn=get_cursor_connection()
    if not cur:
        return({"Error":"DB connection Failed"})
    try:
        cur.execute("DELETE FROM studentinfo where id =%s",(id,))
        conn.commit()
        return jsonify({"Message":"Deleted Successfully"})
    
    except Exception as e:
        return jsonify({"Error":str(e)})
    
    finally:
        cur.close()
        conn.close()

    

if __name__=="__main__":
    app.run(debug= True)



