# Generated by Django 2.1.8 on 2019-05-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_last_login_backend'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='_post_logout_redirect_uris',
            field=models.TextField(blank=True, default='', help_text='Enter each URI on a new line.', verbose_name='Post Logout Redirect URIs'),
        ),
    ]
