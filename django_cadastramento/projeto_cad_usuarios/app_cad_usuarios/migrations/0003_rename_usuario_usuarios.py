# Generated by Django 4.2.2 on 2023-06-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Usuarios',
        ),
    ]