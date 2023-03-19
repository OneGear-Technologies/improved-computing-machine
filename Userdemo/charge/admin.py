from django.contrib import admin
from .models import StatProfile

# Register your models here.


@admin.register(StatProfile)
class StatProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )