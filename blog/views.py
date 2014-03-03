#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from blog.models import Article,Tag,Comment,Category
from blog.modules.articleViews import articleView,commentView,urlView

def home(request):
	artObjs = Article.objects.all()
	comObjs = Comment.objects.all()
	categorys = Category.objects.all()
	articles = []
	monthblogs = []
	for obj in artObjs:
		tags = []
		for t in obj.tags.all():
			tag = Tag.objects.get(id=t.id)
			tags.append(urlView("tags/"+str(tag.id),tag.name))
		coms = []
		cat = urlView("cat/"+str(obj.category.id),obj.category.name)
		title = urlView("art/"+str(obj.id),obj.title)
		art = articleView(title=title,
				tags=tags,
				content=obj.content,
				pub_date=obj.pub_date,
				vist_times=obj.vist_times,
				comment=coms,
				category=cat)
		articles.append(art)
	iamge = urlView("images/", "我多博客")
	return render_to_response("index.html",locals())
