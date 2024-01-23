# Generated by Django 3.2.3 on 2024-01-22 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('command', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='api.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
    ]
