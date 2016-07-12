#encoding=utf-8
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField('类别',max_length=15)
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	tagName = models.CharField('标签',max_length=15)
	def __unicode__(self):
		return self.tagName

class Blog(models.Model):
	title = models.CharField('标题',max_length=50)
	author = models.CharField('作者',max_length=20)
	content = models.TextField('正文')
	category = models.ForeignKey(Category,verbose_name='类别')
	tags = models.ManyToManyField(Tag,verbose_name='标签',null=True)
	pubTime = models.DateTimeField('发布时间',auto_now_add = True)


	def __unicode__(self):
		return self.title

class Comment(models.Model):
	blog = models.ForeignKey(Blog,verbose_name='博客')
	name = models.CharField('称呼',max_length=30)
	content = models.TextField('评论内容')
	comTime = models.DateTimeField('评论时间',auto_now_add=True)

	def __unicode__(self):
		return self.blog.title

class Info(models.Model):
	title = models.CharField('标题',max_length=50)
	author = models.CharField('发布人',max_length=50)
	content = models.TextField('发布内容')
	infoTime = models.DateTimeField('发布时间',auto_now_add=True)

	def __unicode__(self):
		return self.title

class MyUser(models.Model):
	username = models.CharField('用户名',max_length=50)
	password = models.CharField('密码',max_length=50)
	email = models.EmailField('电子邮箱')

	def __unicode__(self):
		return self.username




	


# Create your models here.
