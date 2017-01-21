#coding = utf-8
from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(u'标题', max_length=256,)
    author = models.CharField(u'作者', max_length=256)
    author_summary = models.TextField(u'作者简介')
    summary = models.TextField(u'摘要')
    tags = models.CharField(u'标签', max_length=50)
    content = models.TextField(u'内容')
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True,)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title
#
# class Blogs(models.Model):
#     title = models.CharField(u'标题', max_length=256, )
#     author = models.CharField(u'作者', max_length=256)
#     author_summary = models.TextField(u'作者简介')
#     summary = models.TextField(u'摘要')
#     tags = models.CharField(u'标签', max_length=50)
#     content = models.TextField(u'内容')
#     create_date = models.DateTimeField(u'创建时间', auto_now_add=True, )
#     update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
#
#     def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
#         return self.title

class Test(models.Model):
    name = models.CharField(max_length=256)
    score = models.CharField(max_length=20)


class SuperHero(models.Model):
    name = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1:%Y-%m-%d %H:%M:%S}".format(self.name,
                                                    self.added_on)

    def get_absolute_url(self):
        return reverse('superhero.views.details', args=[self.id])

    class Meta:
        ordering = ["-added_on"]
        verbose_name = "superhero"
        verbose_name_plural = "superheroes"