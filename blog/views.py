#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from blog.models import Article,Tags,Category
from blog.module_view.articleViews import articleView,commentView,tagsView 

def home(request):
	artObjs = Article.objects.all()
	tagObjs = Tags.objects.all()
	catObjs = Category.objects.all()
	for obj in artObjs:
		tags = []
		ti = 0
		for t in obj.tags:
			
	return render_to_response("index.html",locals())
