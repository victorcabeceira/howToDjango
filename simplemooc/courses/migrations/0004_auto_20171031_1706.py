# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_announcement_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Data de Liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em ')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name_plural': 'Aulas',
                'verbose_name': 'Aula',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('embedded', models.TextField(blank=True, verbose_name='Vídeo embutido')),
                ('file', models.FileField(blank=True, null=True, upload_to='lessons/materials')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Lesson', verbose_name='aula')),
            ],
            options={
                'verbose_name_plural': 'Materiais',
                'verbose_name': 'Material',
            },
        ),
        migrations.AlterField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='courses.Course', verbose_name='Curso'),
        ),
    ]
