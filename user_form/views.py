from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls.base import reverse_lazy
from .forms import UserCreationForm
from .models import CustomUser

# Create your views here.
class Home(TemplateView):
    template_name = 'user_form/home.html'
 
class UserFormView(CreateView):

    template_name = 'user_form/form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user-form-list')
    email_template_name = None
    subject_template_name = None

class UserListView(ListView):
    model = CustomUser
    ordering = ['id']
    template_name = 'user_form/form-list.html'
    context_object_name = "userforms"
    paginate_by = 10
    allow_empty_first_page = True
    