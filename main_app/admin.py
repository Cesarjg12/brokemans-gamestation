from django.contrib import admin
from .models import Game, Profile, File, Review, Tag

# add database models to admin portal
admin.site.register(Game)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(File)
admin.site.register(Tag)
