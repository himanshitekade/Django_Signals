from django.urls import path
from .views import CreateUserView
from application import views

urlpatterns = [
    path('', CreateUserView.as_view(), name='create_new_user'),
]
