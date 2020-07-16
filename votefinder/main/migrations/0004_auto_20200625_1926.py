# Generated by Django 2.2.13 on 2020-06-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200616_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='uid',
            new_name='sa_uid'
        ),
        migrations.AddField(
            model_name='player',
            name='bnr_uid',
            field=models.IntegerField(db_index=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sa_uid',
            field=models.IntegerField(db_index=True, null=True, unique=True),
        ),
    ]