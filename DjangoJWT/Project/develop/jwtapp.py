import jwt
from datetime import datetime,timedelta

Secret_key = '12345'

def generate(payload,expiry_minutes=1):
    payload['exp']=datetime.utcnow()+timedelta(minutes=expiry_minutes)
    return jwt.encode(payload,Secret_key,algorithm='HS256')

def decode(token):
    try:
        return jwt.decode(token,Secret_key,algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        return ({"Message " : "Session Expired"})
    
    except jwt.InvalidTokenError:
        return ({"Message " : "Invalid Token"})
