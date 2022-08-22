from django.conf import settings
from django.db.models import CharField, TextField, ForeignKey, CASCADE, SET_NULL
from model_utils.models import TimeStampedModel

from apps.crm.models import Client


class Survey(TimeStampedModel):
    name = CharField('название', max_length=500, unique=True)

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.name


class Question(TimeStampedModel):
    text = TextField('текст вопроса')
    survey = ForeignKey(Survey, on_delete=CASCADE, editable=False, related_name='questions')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        unique_together = [('survey', 'text')]

    def __str__(self):
        return self.text


class Choice(TimeStampedModel):
    text = TextField('текст варианта ответа')
    question = ForeignKey(Question, on_delete=CASCADE, editable=False, related_name='choices')

    class Meta:
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответа'
        unique_together = [('question', 'text')]

    def __str__(self):
        return self.text[:15]


class Interview(TimeStampedModel):
    survey = ForeignKey(Survey, on_delete=CASCADE, editable=False, related_name='interviews')
    client = ForeignKey(Client, on_delete=SET_NULL, editable=False, verbose_name='гражданин', null=True)
    operator = ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True, editable=False,
                          verbose_name='оператор')

    class Meta:
        verbose_name = 'результат опроса'
        verbose_name_plural = 'результаты опроса'

    def __str__(self):
        return f'результат #{self.id}'


class Answer(TimeStampedModel):
    interview = ForeignKey(Interview, on_delete=CASCADE, related_name='answers')
    question = ForeignKey(Question, on_delete=CASCADE, related_name='answers')
    choice = ForeignKey(Choice, on_delete=CASCADE, related_name='answers')

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
        unique_together = [('interview', 'question')]

    def __str__(self):
        return self.text
