from django.urls import path
from .views import UserView, UserIdView

urlpatterns = [
    path('users/general/',UserView.as_view(),),
    path('users/user/<int:pk>/', UserIdView.as_view(),),
]