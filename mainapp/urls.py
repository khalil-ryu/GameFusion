# mainapp/urls.py
from django.urls import path
from .views import home, game, profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('game/', game, name='game'),
    path('profile/', profile, name='profile'),
    
    # Add more paths for other views as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
