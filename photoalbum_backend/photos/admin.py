# from django.contrib import admin

# Register your models here.
# photos/admin.py
from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('upload_date',)