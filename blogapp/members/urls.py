from django.urls import path
from .views import UserRegisterView,UserEditView,ChangePasswordView

urlpatterns = [
    path('register',UserRegisterView.as_view(),name = 'register'),
    path('edit_profile',UserEditView.as_view(),name = 'edit_profile'),
    path('password',ChangePasswordView.as_view(),name = 'password_change'),
]