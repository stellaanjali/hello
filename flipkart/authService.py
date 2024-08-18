# users/services.py
from django.contrib.auth.models import User

def register_user(username, email, password):
    # Manually check if the username or email already exists
    for user in User.objects.all():
        if user.username == username:
            return {"message": "Username already exists"}, False
        if user.email == email:
            return {"message": "Email already exists"}, False

    # Create the user with the plain text password
    user = User(username=username, email=email, password=password)
    user.save()

    return {"message": "User registered successfully"}, True

def login_user(email,password):
    for user in User.objects.all():
        if user.email == email and user.password == password:
            return{"message":"Logged in successfully"},True
        
    return{"message":"Please enter the correct login credentials"}, False
