from django.db.models import CharField, ForeignKey, CASCADE
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name = CharField('название', max_length=1000)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    name = CharField('название', max_length=1000)
    category = ForeignKey(Category, verbose_name='категория', on_delete=CASCADE)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.name
