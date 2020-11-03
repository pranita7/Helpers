from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from blog.views import post_list, post_create, like_post, post_edit
from .views import index, register, profile

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'home/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home/logout.html'), name="logout"),
    path('posts/', post_list, name='post_list'),
    path('post_create/', post_create, name='post_create'),
    path('like/', like_post, name='like_post'),
    url(r'(?P<id>\d+)/post_edit/$', post_edit, name="post_edit"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
