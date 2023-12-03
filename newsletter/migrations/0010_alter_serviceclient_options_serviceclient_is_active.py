# Generated by Django 4.2.7 on 2023-12-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_alter_mailing_options_remove_mailing_is_block_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceclient',
            options={'permissions': [('set_active_client', 'Can active mailing')], 'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AddField(
            model_name='serviceclient',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]