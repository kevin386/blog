#-*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
	"""docstring for ArticleAdmin"""
	pass
class TagsAdmin(admin.ModelAdmin):
	"""docstring for TagsAdmin"""
	pass
class CategoryAdmin(admin.ModelAdmin):
	"""docstring for CategoryAdmin"""
	pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Category, CategoryAdmin)
		