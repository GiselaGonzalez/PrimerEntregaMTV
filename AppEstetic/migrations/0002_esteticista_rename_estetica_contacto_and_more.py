# Generated by Django 4.1.3 on 2022-11-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEstetic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esteticista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estetica',
            new_name='Contacto',
        ),
        migrations.DeleteModel(
            name='Esteticista_Corporal',
        ),
    ]
