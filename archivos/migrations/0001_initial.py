# Generated by Django 3.1.7 on 2021-04-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('fecha', models.DateTimeField(auto_created=True)),
                ('id_archivo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_archivo', models.CharField(max_length=20)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos/')),
            ],
            options={
                'db_table': 'archivos_archivos',
            },
        ),
    ]
