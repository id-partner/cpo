from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Category, Tag, ArticleGallery


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'content',
        'short_description',
        )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ArticleGallery)
