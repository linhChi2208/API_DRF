from rest_framework.views import APIView
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app import models

class Registration(APIView):
  
  def post(self, request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
      account = serializer.save()

      data['response'] = 'Registration successful!'
      data['username'] = account.username
      data['email'] = account.email

      token = Token.objects.get(user=account).key
      data['token'] = token
    else:
      data = serializer.errors
    return Response(data)


class LogOut(APIView):

  def post(self, request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


