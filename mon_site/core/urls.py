from django.contrib import admin
from django.urls import path
from blog.views import home, detail
from django.conf import settings # Ajoute ça
from django.conf.urls.static import static # Ajoute ça

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('article/<int:pk>/', detail, name='article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Et ça
