from django.urls import path
from .views import add_student, get_student,update_data,delete_data
from.authapp import login_page

urlpatterns = [
    path ('add/',add_student),
    path('get/' ,get_student),
    path('update/<int:id>',update_data),
    path('delete/<int:id>',delete_data),
    path('login/',login_page)
]