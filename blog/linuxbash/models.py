from django.db import models


# Модель таблицы категорий
class Category(models.Model):
    categName = models.CharField(max_length=100, null=False, verbose_name=u"Category")
    categHumanName = models.CharField(max_length=100, null=False, verbose_name=u"Name category")

    def __str__(self):
        return self.categHumanName


# Модель таблицы подкатегорий
class SubCategory(models.Model):
    keyCateg = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, verbose_name=u"Category")
    subCategName = models.CharField(max_length=100, null=False, verbose_name=u"Subcategory")
    subCategHumanName = models.CharField(max_length=100, null=False, verbose_name=u"Name subcategory")

    def __str__(self):
        return self.keyCateg.categHumanName + ': ' + self.subCategHumanName


# Модель таблицы статей
class Post(models.Model):
    keyCateg = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, verbose_name=u"Subcategory")
    title = models.CharField(max_length=1000, null=False, verbose_name=u"Title")
    post = models.TextField(max_length=99999, null=False, verbose_name=u"Article")
    url = models.CharField(max_length=200, null=False, verbose_name=u"URL")
    description = models.TextField(max_length=1000, null=False, verbose_name=u"Description article")
    datePost = models.DateField(null=False, verbose_name=u"Date")

    def __str__(self):
        return self.title


# Модель таблицы загружаемых файлов (например фото для отображения в статьях)
# Процесс загрузки:
# создать пост;
# загрузить фото через админку выбрав файл и ранее созданный пост;
# на основании показанного пути хранения файла добавить в пост, например:
# <img src="../static/files/blog/2022/04/19/python.png">
class UploadFile(models.Model):
    imagesPost = models.FileField(upload_to='blog/%Y/%m/%d', null=False, verbose_name=u"Load file")
    keyPost = models.ForeignKey(Post, on_delete=models.PROTECT, null=False, verbose_name=u"Article")

    def __str__(self):
        return self.keyPost.title + ': static/files/' + str(self.imagesPost)
