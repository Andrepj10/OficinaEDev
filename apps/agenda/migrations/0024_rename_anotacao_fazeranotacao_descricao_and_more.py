# Generated by Django 4.2.3 on 2023-08-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0023_remove_fazeranotacao_campo1_fazeranotacao_anotacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fazeranotacao',
            old_name='anotacao',
            new_name='descricao',
        ),
        migrations.AlterField(
            model_name='fazeranotacao',
            name='nomeAnotacao',
            field=models.CharField(max_length=100),
        ),
    ]
