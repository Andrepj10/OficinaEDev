# Generated by Django 4.2.3 on 2023-08-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0018_alter_fotografia_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fazermeta',
            name='modo',
            field=models.CharField(choices=[('Meta em andamento', 'Meta em andamento'), ('Meta Concluida', 'Meta Concluida')], default='Meta em andamento', max_length=20),
        ),
    ]
