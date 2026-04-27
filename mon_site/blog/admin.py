from django.contrib import admin
from .models import Article # On importe ton modèle Article

admin.site.register(Article) # On l'enregistre dans l'admin