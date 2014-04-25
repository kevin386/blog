#-*- coding:utf-8 -*-
from django.db import models

class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField("分类", max_length=128, null=False, blank=False)
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	"""docstring for Tag"""
	name = models.CharField("标签", max_length=128, null=False, blank=False)
	def __unicode__(self):
		return self.name


class Article(models.Model):
	"""docstring for Article"""
	title = models.CharField("标题", max_length=128,null=False,blank=False)
	content = models.TextField("内容", max_length=8192,null=False,blank=True)
	category = models.ForeignKey(Category, verbose_name="分类");
	tags = models.ManyToManyField(Tag, verbose_name="标签")
	pub_date = models.DateTimeField("发布时间",auto_now=False, auto_now_add=True)
	last_date = models.DateTimeField("最近修改时间",auto_now=True, auto_now_add=False)
	vist_times = models.DecimalField("浏览量", null=True, blank=True,max_digits=5,decimal_places=0)
	def __unicode__(self):
		return self.title
		
class Comment(models.Model):
	"""docstring for Tag"""
	article = models.ForeignKey(Article,verbose_name="评论")
	content = models.CharField("评论", max_length=256, null=False, blank=False)
	def __unicode__(self):
		return self.content
