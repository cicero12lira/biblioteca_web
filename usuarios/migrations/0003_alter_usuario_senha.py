# Generated by Django 4.1.7 on 2023-03-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=64),
        ),
    ]