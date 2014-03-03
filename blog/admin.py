#-*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Article,Tag,Category,Comment

class ArticleAdmin(admin.ModelAdmin):
	"""docstring for ArticleAdmin"""
	pass
class TagAdmin(admin.ModelAdmin):
	"""docstring for TagAdmin"""
	pass
class CategoryAdmin(admin.ModelAdmin):
	"""docstring for CategoryAdmin"""
	pass
class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
		
