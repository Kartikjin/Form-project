from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserFormView.as_view(), name="user-form"),
    path('list/', views.UserListView.as_view(), name="user-form-list")
]
