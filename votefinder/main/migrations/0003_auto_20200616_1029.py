# Generated by Django 2.2.13 on 2020-06-16 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200608_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='post_lynches',
            new_name='post_executions',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='nolynch',
            new_name='no_execute',
        ),
    ]