from django.db.models import CharField, ForeignKey, PROTECT
from model_utils.models import TimeStampedModel


class Organization(TimeStampedModel):
    name = CharField('наименование', max_length=1000)
    region = ForeignKey('geo.Region', verbose_name='регион', on_delete=PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'медицинская организация'
        verbose_name_plural = 'медицинские организации'
        ordering = ['name']
        unique_together = [('name', 'region')]

    def __str__(self):
        return self.name
