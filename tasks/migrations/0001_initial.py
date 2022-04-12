# Generated by Django 3.2 on 2022-04-12 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(blank=True)),
                ('starteddate', models.DateTimeField(auto_now_add=True)),
                ('upload', models.DateTimeField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('', ''), ('in progress', 'in progress'), ('completed', 'completed'), ('not completed', 'not completed')], default=False, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='task_images/')),
                ('checker', models.ManyToManyField(related_name='checkers', to='accounts.Employe')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creators', to='accounts.employe')),
                ('employe', models.ManyToManyField(blank=True, to='accounts.Employe')),
                ('section', models.ManyToManyField(to='accounts.Section')),
            ],
        ),
    ]
