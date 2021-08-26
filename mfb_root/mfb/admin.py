from django.contrib import admin

# Register your models here with the admin interface.
# from .models import projects, tools, methodology, checklists
from .models import projects, tools, methodology, checklists

myModels = [projects, tools, methodology, checklists]

admin.site.register(myModels)
