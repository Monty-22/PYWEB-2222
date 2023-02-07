from django.urls import path
from .views import ViewBlog, ViewBlogSingle

app_name = 'blog'

urlpatterns = [
   path('', ViewBlog.as_view(), name='blog'),
   path('', ViewBlogSingle.as_view(), name='blog-single'),

]