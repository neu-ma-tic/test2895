# Generated by Django 3.1.2 on 2020-10-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0004_auto_20201022_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='amongusgame',
            name='text_message_id',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='Text message ID'),
        ),
    ]