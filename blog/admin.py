#-*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Article,Tag,Category,Comment

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','category')
	search_fields = ('title',)
	list_filter = ('pub_date',)
	ordering = ('-pub_date',)
	fields = ('title','content','category','tags')
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
		
