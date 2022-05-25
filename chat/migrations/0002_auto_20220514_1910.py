# Generated by Django 3.2 on 2022-05-14 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('message_detail', models.JSONField()),
            ],
            options={
                'ordering': ['-message_detail__timestamp'],
            },
        ),
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1_name', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chat Message',
                'unique_together': {('user1', 'user2')},
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('surname', models.CharField(blank=True, max_length=20, null=True)),
                ('is_online', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='group_chat',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='group_chat',
            name='author',
        ),
        migrations.RemoveField(
            model_name='group_chat',
            name='members',
        ),
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='message',
            name='dialog',
        ),
        migrations.RemoveField(
            model_name='message',
            name='group',
        ),
        migrations.DeleteModel(
            name='Dialog_chat',
        ),
        migrations.DeleteModel(
            name='Group_chat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='chat_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='chat.chatsession'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='message_sender'),
        ),
    ]