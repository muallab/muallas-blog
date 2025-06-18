from django.contrib import admin

# Register your models here.
from .models import Article
admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('title', 'content')