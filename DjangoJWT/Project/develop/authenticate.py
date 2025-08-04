from .jwtapp import decode
from django.http import JsonResponse

def token_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        token = None  

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return JsonResponse({'error': 'Token missing'})
        decode_data = decode(token)
        
        if isinstance(decode_data, dict) and decode_data.get("Message"):
            return JsonResponse({'error': decode_data["Message"]})
        return view_func(request, *args, **kwargs)
    return wrapper
        
    