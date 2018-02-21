from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(verbose_name="大纲", max_length=200)

    def __str__(self):
        return self.category_name

    class Meta():
        verbose_name = "编程类别"
        verbose_name_plural = verbose_name


class Point(models.Model):
    link = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="关联大纲")
    point_name = models.CharField(verbose_name="要点", max_length=200)

    def __str__(self):
        return self.point_name

    class Meta():
        verbose_name = "知识要点"
        verbose_name_plural = verbose_name


class Article(models.Model):
    belong = models.ForeignKey(Point, on_delete=models.CASCADE, verbose_name="关联要点")
    title = models.CharField(verbose_name="文章标题", max_length=200)
    content = UEditorField(verbose_name="文章内容", width=900, height=300, imagePath="", filePath="", default="")
    add_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "要点详情"
        verbose_name_plural = verbose_name