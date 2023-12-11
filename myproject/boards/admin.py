from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Board, Topic, Post



@admin.register(Board)
class BoardAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['subject', 'last_updated', 'board', 'starter', 'views']


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['message', 'topic', 'created_at', 'updated_at', 'created_by', 'updated_by']
