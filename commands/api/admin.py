from django.contrib import admin

from .models import Member, Command


@admin.register(Command, Member)
class BlogAdmin(admin.ModelAdmin):
    pass
