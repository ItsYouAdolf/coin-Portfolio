from django.db import models

# Create your models here.

class country(models.Model):
    name = models.CharField('страна', max_length=100)
    description1 = models.TextField('страна')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

class  denomination(models.Model):
    name = models.CharField('номинал', max_length=100)
    description2 = models.TextField('номинал')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'номинал'
        verbose_name_plural = 'номиналы'

class age(models.Model):
    name = models.CharField('год', max_length=100)
    description3 = models.TextField('год')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'год'
        verbose_name_plural = 'года'

class metal(models.Model):
    name = models.CharField('металл', max_length=100)
    description4 = models.TextField('металл')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'металл'
        verbose_name_plural = 'металлы'


class description(models.Model):
    name = models.CharField('Монета', max_length=100)
    img = models.ImageField(upload_to='ImgOsnova')
    denomination = models.ManyToManyField(denomination, verbose_name='Номинал')
    country = models.ManyToManyField(country, verbose_name='Страна')
    age = models.ManyToManyField(age, verbose_name='Год')
    metal = models.ManyToManyField(metal, verbose_name='Металл')
    des = models.TextField('Описание')
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'описание'
        verbose_name_plural = 'описание'