from django.contrib import admin
from .models import Tutorials

# Register your models here.



class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_name",
              "tutorial_published",
              "tutorial_content"]
admin.site.register(Tutorials,TutorialAdmin)