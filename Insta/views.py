from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from Insta.models import Post

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']
    login_url = 'login'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')