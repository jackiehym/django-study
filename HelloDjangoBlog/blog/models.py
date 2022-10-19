from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章数据库"""
    title = models.CharField(max_length=70)
    # 字符串较长的用Text
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 一对多，一篇文章只能对应一个分类，而一个分类下可以有多篇文章，用ForeignKey
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    # User自带的
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
