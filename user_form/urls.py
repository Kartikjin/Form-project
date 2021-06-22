from django.urls import path
from . import views
urlpatterns = [
    path('/user-form', views.UserFormView.as_view(), name="user-form"),
    path('/user-form/list/', views.UserListView.as_view(), name="user-form-list")
]
