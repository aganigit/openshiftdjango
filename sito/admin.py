from django.contrib import admin
from sito.models import *

from image_cropping import ImageCroppingMixin

# Register your models here.

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Categorie)
admin.site.register(Immagini, MyModelAdmin)
admin.site.register(Video, MyModelAdmin)
admin.site.register(Post, MyModelAdmin)
admin.site.register(Rai, MyModelAdmin)
admin.site.register(Vimeo, MyModelAdmin)
admin.site.register(Ricettario, MyModelAdmin)
