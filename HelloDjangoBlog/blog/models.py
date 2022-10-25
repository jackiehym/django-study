from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章数据库"""
    title = models.CharField('标题', max_length=70)
    # 字符串较长的用Text
    body = models.TextField('正文', )
    create_time = models.DateTimeField('创建时间', )
    modified_time = models.DateTimeField('修改时间', )
    # 摘要
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    # 一对多，一篇文章只能对应一个分类，而一个分类下可以有多篇文章，用ForeignKey
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # User自带的
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
