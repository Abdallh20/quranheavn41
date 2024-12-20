from django.contrib import admin
from .models import *
from .forms import *


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'author',
        'image',
        'published'
    ]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['title', 'subtitle', 'article_slug', 'series', 'author','image']}),
        ("Content", {"fields": ['content', 'notes']}),
        ("Date", {"fields": ['modified']})
    ]

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(order)
admin.site.register(Fatwa)
admin.site.register(ExchangeDetail)
