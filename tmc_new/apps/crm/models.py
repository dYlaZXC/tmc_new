from django.conf import settings
from django.core.validators import RegexValidator
from django.db.models import CharField, ForeignKey, PROTECT, TextField, ManyToManyField, SET_NULL, \
    OneToOneField, DateTimeField, BooleanField
from django.urls import reverse
from model_utils import Choices
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


class Client(TimeStampedModel):
    user = ForeignKey(User, on_delete=PROTECT, verbose_name='пользователь')
    phone = CharField('телефон', max_length=255)
    first_name = CharField('имя', max_length=255, blank=True)
    last_name = CharField('фамилия', max_length=255, blank=True)
    patronymic = CharField('отчество', max_length=255, blank=True)
    iin = CharField('ИИН', max_length=12, validators=[
        RegexValidator(r'\d{12}', message='корректный ИИН должен состоять из 12 цифр')], blank=True)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return self.phone

    def get_full_name(self):
        return ' '.join((self.last_name, self.first_name, self.patronymic)).rstrip()


class Topic(TimeStampedModel):
    """Тематика обращения"""
    name = CharField('название', max_length=500, unique=True)
    text = TextField('пояснение', help_text='если нужно', blank=True)

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'

    def __str__(self):
        return self.name


class Complaint(TimeStampedModel):
    RESULTS = Choices(
        ('explanations', 'даны разъяснения'),
        ('justified', 'жалоба обоснована'),
        ('not_justified', 'жалоба не обоснована')
    )

    operator = ForeignKey(User, on_delete=PROTECT, verbose_name='оператор',
                          editable=False, related_name='created_complaints')
    assignor = ForeignKey(User, on_delete=PROTECT, verbose_name='поручитель',
                          null=True, editable=False, related_name='assigned_complaints')
    executor = ForeignKey(User, on_delete=PROTECT, verbose_name='исполнитель',
                          null=True, editable=False, related_name='completed_complaint')
    topics = ManyToManyField(Topic, verbose_name='темы', blank=True)
    status = CharField('статус обращения', max_length=500, blank=True)
    actions = TextField('принятые меры', blank=True)
    result = CharField('результат', max_length=100, choices=RESULTS, blank=True)

    class Meta:
        verbose_name = 'жалоба'
        verbose_name_plural = 'жалобы'

    def __str__(self):
        return f'жалоба №{self.id}'


class Consultation(TimeStampedModel):
    category = ForeignKey('handbook.Category', verbose_name='категория', on_delete=SET_NULL,
                          null=True, blank=True)
    article = ForeignKey('handbook.Article', verbose_name='статья', on_delete=SET_NULL,
                         null=True, blank=True)

    class Meta:
        verbose_name = 'консультация'
        verbose_name_plural = 'консультации'


class ClientCall(TimeStampedModel):
    KINDS = Choices(
        ('consultation', 'консультация'),
        ('complaint', 'жалоба'),
        ('thanks', 'благодарность'),
        ('wrong_call', 'ошибочный звонок'),
        ('interrupted_call', 'прерывание связи'),
        ('proposal', 'предложение'),
    )
    user = ForeignKey(User, on_delete=PROTECT, verbose_name='пользователь')
    client = ForeignKey(Client, on_delete=PROTECT, verbose_name='клиент', null=True)
    organization = ForeignKey('organizations.Organization', on_delete=PROTECT, verbose_name='МО',
                              null=True, blank=True)
    region = ForeignKey('geo.Region', on_delete=PROTECT, verbose_name='регион', null=True, blank=True)
    text = TextField('текст обращения', blank=True)
    answer = TextField('ответ', blank=True)
    kind = CharField('вид', max_length=100, choices=KINDS, default=KINDS.consultation)
    complaint = OneToOneField(Complaint, verbose_name='жалоба', on_delete=SET_NULL, null=True, editable=False)
    consultation = OneToOneField(Consultation, verbose_name='консультация', on_delete=SET_NULL,
                                 null=True, editable=False)


    sub_kind = CharField(max_length=55555, blank=True, null=True)
    address = CharField(max_length=55555, blank=True, null=True)
    fio = CharField(max_length=55555, blank=True, null=True)
    phone = CharField(max_length=55555, blank=True, null=True)
    city = CharField(max_length=55555, blank=True, null=True)
    pmsp = CharField(max_length=55555, blank=True, null=True)
    phone_number = CharField(max_length=55555, blank=True, null=True)
    reason = CharField(max_length=55555, blank=True, null=True)
    fio_agent = CharField(max_length=55555, blank=True, null=True)
    fio_aktivam = CharField(max_length=55555, blank=True, null=True)
    komu = CharField(max_length=55555, blank=True, null=True)
    result = CharField(max_length=55555, blank=True, null=True)
    result_more = CharField(max_length=55555, blank=True, null=True)
    sex = CharField(max_length=55555, blank=True, null=True)
    iin = CharField(max_length=55555, blank=True, null=True)
    

    class Meta:
        verbose_name = 'обращение в КЦ'
        verbose_name_plural = 'обращения в КЦ'
        ordering = ['-created']

    def __str__(self):
        return f'обращение №{self.id}'

    def get_absolute_url(self):
        return reverse('crm:clientcall_detail', kwargs={'pk': self.pk})
