from django.contrib import admin
from gestionDesPlats.models import Categorie, Plat

class PlatAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'prix', 'categorie_id')
   list_filter    = ('nom','categorie_id',)
   ordering       = ('prix', )


admin.site.register(Categorie)
admin.site.register(Plat, PlatAdmin)
