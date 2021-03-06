# Generated by Django 3.0.4 on 2020-03-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(default='Description')),
                ('keywords', models.CharField(default='Key words', max_length=120)),
                ('aim', models.FileField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sort_type', models.CharField(choices=[('Buble', 'Buble'), ('Merge', 'Merge'), ('Inserts', 'Inserts')], default='Buble', max_length=20)),
            ],
            options={
                'ordering': ['-id', '-timestamp'],
                'abstract': False,
            },
        ),
    ]
