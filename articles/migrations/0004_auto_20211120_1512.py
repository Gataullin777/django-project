# Generated by Django 3.1.2 on 2021-11-20 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211102_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
