from django.urls import path
from .views import landing_page, create_contact, edit_contact, delete_contact, logout_view, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('new-contact', create_contact, name='new-contact'),
    path('edit-contact/<int:contact_id>/', edit_contact, name='edit-contact'),
    path('delete-contact/<int:contact_id>/', delete_contact, name='delete-contact'),
    path('logout/', logout_view, name='logout'),


    # Authentication URLs
    path('login/', CustomLoginView.as_view(template_name='phonebook/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
