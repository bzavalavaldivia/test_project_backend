from django.contrib import admin

from apps.surveys import models

admin.site.register(models.Survey)
admin.site.register(models.Question)
admin.site.register(models.Option)