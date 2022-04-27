from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import Registration, LogOut

urlpatterns = [
  path('login/', obtain_auth_token, name='login'),
  path('register/', Registration.as_view(), name='register'),
  path('logout/', LogOut.as_view(), name='logout'),
  
]