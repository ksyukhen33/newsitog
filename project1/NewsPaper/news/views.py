

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Posts


class PostsList(ListView):
    model = Posts
    ordering = '-name_post'
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Posts
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'