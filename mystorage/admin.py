from django.contrib import admin

from .models import Essay
from .models import Album
from .models import Files

admin.site.register(Essay)
admin.site.register(Album)
admin.site.register(Files)