# Generated by Django 4.2.3 on 2023-07-31 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_fotografia_categoria_fotografia_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='data_fotografia',
            new_name='data_evento',
        ),
    ]