# Generated by Django 4.1.6 on 2023-02-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supera_ecommece', '0002_alter_clientes_foto_alter_funcionarios_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='n_telefone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
