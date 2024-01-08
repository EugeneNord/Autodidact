from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Course(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, verbose_name='Преподаватель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Module(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"


class Material(models.Model):
    objects = models.Manager()
    VIDEO = 'Видео'
    TEXT = 'Текст'
    DOCUMENT = 'Документ'
    TYPE_CHOICES = [
        (VIDEO, 'Видео'),
        (TEXT, 'Текст'),
        (DOCUMENT, 'Документ'),
    ]
    title = models.CharField(max_length=255, verbose_name='Наименование')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='Тип')
    content = models.TextField(max_length=10000, verbose_name='Содержание')
    video = models.FileField(upload_to='autodidact/static/autodidact/video/', null=True, blank=True)
    file = models.FileField(upload_to='autodidact/static/autodidact/file/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Модуль')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    enrollment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    STATUS_CHOICES = (
        ('active', 'active'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Модуль')
    progress = models.IntegerField(default=0, verbose_name='Прогресс')
    last_updated = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего обновления')

    def __str__(self):
        return self.progress

    class Meta:
        verbose_name = 'Прогресс пользователя'
        verbose_name_plural = 'Прогресс пользователя'
