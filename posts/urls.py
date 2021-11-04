from posts.views import home,create,update,delete,detail,get_profile
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home,name='home'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail,name='detail'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/', delete,name='delete'),
    path('profile/<int:id>/', get_profile, name='profile'),
    path('logout/', LogoutView.as_view(),name='logout'),
]