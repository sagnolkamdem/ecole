from django.contrib import admin
from inscription.models import profile, Serie, Eleve, Classe, Intendant, Inscription, Article

# Register your models here.

admin.site.register(profile)
admin.site.register(Serie)
admin.site.register(Eleve)
admin.site.register(Classe)
admin.site.register(Intendant)
admin.site.register(Inscription)
admin.site.register(Article)