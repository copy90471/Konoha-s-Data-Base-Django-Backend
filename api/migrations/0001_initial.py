# Generated by Django 4.0.5 on 2022-07-15 15:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(default='', max_length=50)),
                ('pais_cliente', models.CharField(default='', max_length=30)),
                ('rango', models.CharField(default='', max_length=1)),
                ('recompensa', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('edad', models.IntegerField(default=12)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No se dice')], default='N', max_length=1)),
                ('clan', models.CharField(default='Konoha', max_length=50)),
                ('fecha_nacimiento', models.DateField(default=datetime.date(1, 1, 1))),
            ],
        ),
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('elemento', models.CharField(default='', max_length=30)),
                ('es_oculta', models.BooleanField(default=False)),
                ('cantidad_chakra', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.persona')),
                ('chakra_max', models.IntegerField(default=0)),
                ('sobrenombre', models.CharField(default='', max_length=50)),
            ],
            bases=('api.persona',),
        ),
        migrations.CreateModel(
            name='TecnicaAtaque',
            fields=[
                ('tecnica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.tecnica')),
                ('rango_ataque', models.IntegerField(default=0)),
            ],
            bases=('api.tecnica',),
        ),
        migrations.CreateModel(
            name='TecnicaCurativa',
            fields=[
                ('tecnica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.tecnica')),
                ('velocidad_curacion', models.IntegerField(default=0)),
            ],
            bases=('api.tecnica',),
        ),
        migrations.CreateModel(
            name='Chunin',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.ninja')),
                ('fecha_examen', models.DateField(default=datetime.date(1, 1, 1))),
                ('calificacion_examen', models.CharField(default='', max_length=100)),
            ],
            bases=('api.ninja',),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('nombre', models.CharField(default='', max_length=50)),
                ('ninja1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='exceptuar_ninja_1', serialize=False, to='api.ninja')),
                ('ninja2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exceptuar_ninja_2', to='api.ninja')),
            ],
        ),
        migrations.CreateModel(
            name='Genin',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.ninja')),
                ('fecha_graduacion', models.DateField(default=datetime.date(1, 1, 1))),
                ('valoracion', models.CharField(default='', max_length=200)),
            ],
            bases=('api.ninja',),
        ),
        migrations.CreateModel(
            name='Jounin',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.ninja')),
                ('fecha_examen', models.DateField(default=datetime.date(1, 1, 1))),
                ('calificacion_examen', models.CharField(default='', max_length=100)),
            ],
            bases=('api.ninja',),
        ),
        migrations.CreateModel(
            name='NinjaMedico',
            fields=[
                ('ninja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.ninja')),
            ],
            bases=('api.ninja',),
        ),
        migrations.CreateModel(
            name='Pergamino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sellado', models.DateField(default=datetime.date(1, 1, 1))),
                ('tecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tecnica')),
                ('ninja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ninja')),
            ],
        ),
        migrations.CreateModel(
            name='BestiaMitica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('tipo', models.CharField(default='', max_length=30)),
                ('invocador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ninja')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoEnMision',
            fields=[
                ('equipo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.equipo')),
                ('fecha_inicio', models.DateField(default=datetime.date(1, 1, 1))),
                ('fecha_fin', models.DateField(default=datetime.date(1, 1, 1))),
                ('resultado', models.CharField(choices=[('S', 'Satisfactorio'), ('NS', 'No Satisfactorio'), ('P', 'Pendiente')], default='P', max_length=20)),
                ('cantidad_shurikens', models.IntegerField(default=0)),
                ('cantidad_kunais', models.IntegerField(default=0)),
                ('cantidad_sellos', models.IntegerField(default=0)),
                ('capitan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jounin')),
                ('mision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mision')),
            ],
            options={
                'unique_together': {('equipo', 'mision')},
            },
        ),
        migrations.AddField(
            model_name='equipo',
            name='ninjamedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ninjamedico'),
        ),
        migrations.CreateModel(
            name='BestiaMisionPergamino',
            fields=[
                ('bestia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.bestiamitica')),
                ('mision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mision')),
                ('pergamino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pergamino')),
            ],
            options={
                'unique_together': {('bestia', 'mision', 'pergamino')},
            },
        ),
        migrations.CreateModel(
            name='NinjaTecnica',
            fields=[
                ('ninja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.ninja')),
                ('tecnica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tecnica')),
            ],
            options={
                'unique_together': {('ninja', 'tecnica')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='equipo',
            unique_together={('ninja1', 'ninja2', 'ninjamedico')},
        ),
        migrations.CreateModel(
            name='EquipoEnMisionPergamino',
            fields=[
                ('equipoenmision', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.equipoenmision')),
                ('pergamino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pergamino')),
            ],
            options={
                'unique_together': {('equipoenmision', 'pergamino')},
            },
        ),
    ]
