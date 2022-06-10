from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    patronymic = CharField('отчество', max_length=100, blank=True)

    def __str__(self):
        return self.get_full_name() or self.username

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        if self.patronymic:
            full_name = '%s %s %s' % (self.last_name, self.first_name, self.patronymic)
        else:
            full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()
