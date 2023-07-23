from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Type)
admin.site.register(Room)
admin.site.register(Owner)
admin.site.register(Specification)
admin.site.register(Report)

