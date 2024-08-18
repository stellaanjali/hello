#users/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .authService import register_user, login_user
from rest_framework.decorators import api_view

@api_view(['POST'])
def register(request):
    #Extract data from the request
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    # Validate the inputs 
    if not username or not email or not password:
        return Response({"error": "Username,email,and password are required"},status = status.HTTP_400_BAD_REQUEST)
    #Call the service layer to register the user
    result,success = register_user(username,email,password)
    #Return the appropriate response
    if success:
        return Response(result, status =status.HTTP_201_CREATED)
    else:
        return Response(result, status =status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Enter the email and password"}, status = status.HTTP_400_BAD_REQUEST)
    result,success = login_user(email,password)
    if success:
         return Response(result, status =status.HTTP_200_OK)
    else:
        return Response(result, status =status.HTTP_400_BAD_REQUEST)