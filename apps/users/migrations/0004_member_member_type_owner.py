# Generated by Django 5.0.4 on 2024-04-08 19:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_comment'),
        ('users', '0003_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_type',
            field=models.CharField(choices=[('Dir', 'Director'), ('Ger', 'Gerente'), ('Jun', 'Junior'), ('Sup', 'Supervisor'), ('Dev', 'Desarrollador')], default='Dev', max_length=13),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
