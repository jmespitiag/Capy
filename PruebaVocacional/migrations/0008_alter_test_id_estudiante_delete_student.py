# Generated by Django 4.2.4 on 2023-11-04 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('herramientas', '0004_alter_clase_id_estudiante_alter_nota_student'),
        ('chat', '0002_alter_chat_student'),
        ('PruebaVocacional', '0007_alter_test_id_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='id_estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID de estudiante'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]