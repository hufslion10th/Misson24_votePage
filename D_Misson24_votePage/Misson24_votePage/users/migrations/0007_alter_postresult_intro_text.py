# Generated by Django 4.1 on 2022-08-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_personalvote_dict_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postresult',
            name='intro_text',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='한줄소개'),
        ),
    ]
