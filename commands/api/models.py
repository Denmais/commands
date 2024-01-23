from django.db import models


MAX_LENGTH = 100


class Command(models.Model):
    """Класс команды."""
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH
    )

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class Member(models.Model):
    """Класс участника."""
    name = models.CharField(
        verbose_name='Имя',
        max_length=MAX_LENGTH
    )
    command = models.ForeignKey(
        Command,
        verbose_name='Команда',
        on_delete=models.SET_NULL,
        related_name='members',
        null=True
    )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.name