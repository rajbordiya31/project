from fastapi import FastAPI 
from dbConnection.pooling_connection import get_cursor_connection
from pydantic import BaseModel,ValidationError

app=FastAPI()

class student(BaseModel):
    id:int
    name:str
    age:int
    mob_num : int

# Insert Data

@app.post("/insert")

def add_data(student:student):
    cur,conn=get_cursor_connection()
    print("connection stablished")

    if not cur:
        print("Connection Failed")
        return ("Connection failed")
    try:
        cur.execute("INSERT INTO studentinfo (id,name,age,mob_num) VALUES (%s,%s,%s,%s)",(student.id,student.name,student.age,student.mob_num))
        print("query executed")
        conn.commit()
        return ("Message: inserted successfully")
    
    except ValidationError as e:
        print(f"Error : {e}")
        return (f"Error : {e}")
    finally:
        cur.close()
        conn.close()
    
# Get Data
@app.get("/reterive")

def get_data():
    cur,conn=get_cursor_connection()
    print("connection stablished")

    if not cur:
        print("Connection Failed")
        return ("Connection Failed")
    try:
        cur.execute("SELECT * FROM studentinfo")
        print("query executed")
        row = cur.fetchall()
        return (row)
    
    except Exception as e:
        print(f"Exception : {e}")
        return (f"Exception : {e}")
    
    finally :
        cur.close()
        conn.close()

@app.put("/update/{sid}")
def update_data(sid:int,student:student):
    cur,conn=get_cursor_connection()
    print("connection stablished")

    if not cur:
        print("Connection Failed")
        return ("Connection Failed")
    try:
        cur.execute("UPDATE studentinfo SET name=%s,age=%s,mob_num=%s WHERE id=%s",(student.name,student.age,student.mob_num,sid))
        print("query executed")
        conn.commit()
        return("message: updated Successfully")
    
    except Exception as e:
        print(f"Exception : {e}")
        return (f"Exception : {e}")
    
    finally :
        cur.close()
        conn.close()

@app.delete("/delete/{sid}")

def delete_data(sid:int):
    cur,conn=get_cursor_connection()
    print("connection stablished")

    if not cur:
        print("Connection Failed")
        return ("Connection Failed")
    try:
        cur.execute("DELETE FROM studentinfo WHERE id=%s",(sid,))
        conn.commit()
        return("message: Deleted Successfully")
    
    except Exception as e:
        print(f"Exception : {e}")
        return (f"Exception : {e}")
    
    finally :
        cur.close()
        conn.close()


    

