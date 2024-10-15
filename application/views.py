from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages


 """This class-based view (CBV) handles both GET and POST requests for 
    creating a new user. It uses Django's built-in User model to register new 
    users and provides feedback via messages."""

class CreateUserView(View):
    def get(self, request):
        """Handles GET requests. This method renders the form for creating a new user.
        Rendering the form: When a user visits the page, we display a form 
        where they can input their desired username and password."""
   
        return render(request, 'create_user.html')

    def post(self, request):
        """ Handles POST requests. This method processes the form submission to 
        create a new user.It retrieves the submitted username and password, checks 
        for existing users, and creates a new user.Form submission: When the form is 
        submitted, this method is called to handle the data."""

        username = request.POST.get('username')
        password = request.POST.get('password')

        #  # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            # If the username exists, send an error message and reload the form
            messages.error(request, f"Username '{username}' is already taken. Please choose another one.")
            return render(request, 'create_user.html')

        # Try to create a new user with the provided username and password
        try:
            # Django's built-in create_user method handles user creation securely
            User.objects.create_user(username=username, password=password)
            messages.success(request, f"User {username} created successfully!")

            # Redirect to the same or another page after successful creation
            return redirect('create_new_user')  # Redirect to the same page or another page
        except Exception as e:
            # If any error occurs during user creation, display an error message
            messages.error(request, f"Error creating user: {e}")
            return render(request, 'create_user.html')

