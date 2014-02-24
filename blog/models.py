#-*- coding:utf-8 -*-
from django.db import models

class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField("分类", max_length=128, null=False, blank=False)
	def __unicode__(self):
		return self.name

class Tags(models.Model):
	"""docstring for Tags"""
	name = models.CharField("分类", max_length=128, null=False, blank=False)
	def __unicode__(self):
		return self.name

class Article(models.Model):
	"""docstring for Article"""
	title = models.CharField("标题", max_length=128,null=False,blank=False)
	content = models.TextField("内容", max_length=8192,null=False,blank=True)
	category = models.ForeignKey(Category, verbose_name="分类");
	tags = models.ForeignKey(Tags, verbose_name="标签")
	createTime = models.DateTimeField("创建时间",auto_now=False, auto_now_add=True)
	lastModified = models.DateTimeField("最近修改时间",auto_now=True, auto_now_add=False)
	vistCount = models.DecimalField("浏览量", max_digits=5,decimal_places=0)
	def __unicode__(self):
		return self.title
		