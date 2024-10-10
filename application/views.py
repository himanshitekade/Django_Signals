from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse



class CreateUserView(View):
    def get(self, request):
        # Render the form for creating a new user
        return render(request, 'create_user.html')

    def post(self, request):
        # Create a new user and handle form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)

        # Optionally, you can return a success message as JSON
        return JsonResponse({"message": "User created successfully."})
