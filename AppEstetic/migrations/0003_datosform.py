# Generated by Django 4.1.3 on 2022-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEstetic', '0002_esteticista_rename_estetica_contacto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
    ]