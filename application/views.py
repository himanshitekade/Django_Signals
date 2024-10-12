from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages


class CreateUserView(View):
    def get(self, request):
        # Render the form for creating a new user
        return render(request, 'create_user.html')

    def post(self, request):
        # Get username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken. Please choose another one.")
            return render(request, 'create_user.html')

        # Create the user
        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, f"User {username} created successfully!")
            return redirect('create_new_user')  # Redirect to the same page or another page
        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return render(request, 'create_user.html')

