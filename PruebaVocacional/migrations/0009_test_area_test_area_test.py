# Generated by Django 4.2.4 on 2023-11-11 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PruebaVocacional', '0008_alter_test_id_estudiante_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='area',
            field=models.CharField(choices=[('Administrativas y contables', 'Administrativas y contables'), ('Humanísticas, Ciencias Jurídicas y Sociales', 'Humanísticas, Ciencias Jurídicas y Sociales'), ('Artísticas', 'Artísticas'), ('Ciencias de la salud', 'Ciencias de la salud'), ('Ingenierías, carreras técnicas y computación', 'Ingenierías, carreras técnicas y computación'), ('Ciencias exactas', 'Ciencias exactas'), ('N/A', 'N/A')], default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='test',
            name='area_test',
            field=models.CharField(choices=[('Administrativas y contables', 'Administrativas y contables'), ('Humanísticas, Ciencias Jurídicas y Sociales', 'Humanísticas, Ciencias Jurídicas y Sociales'), ('Artísticas', 'Artísticas'), ('Ciencias de la salud', 'Ciencias de la salud'), ('Ingenierías, carreras técnicas y computación', 'Ingenierías, carreras técnicas y computación'), ('Ciencias exactas', 'Ciencias exactas'), ('N/A', 'N/A')], default='N/A', max_length=50),
        ),
    ]
