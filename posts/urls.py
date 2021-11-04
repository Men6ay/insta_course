from posts.views import home,create,update,delete,detail
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail,name='detail'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/', delete,name='delete'),
]