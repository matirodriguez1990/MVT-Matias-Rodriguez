# Generated by Django 4.0.4 on 2022-04-16 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.IntegerField()),
                ('fechaNac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppFamiliar.persona')),
                ('parentesco', models.CharField(max_length=40)),
            ],
            bases=('AppFamiliar.persona',),
        ),
    ]
