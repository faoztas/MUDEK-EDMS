# Generated by Django 2.1.7 on 2019-06-16 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edms', '0002_remove_requested_documents_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='requested_documents',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='edms.Lesson'),
            preserve_default=False,
        ),
    ]
