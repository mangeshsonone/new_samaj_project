# Generated by Django 4.2.20 on 2025-04-19 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_alter_familyhead_landmark_alter_member_landmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='family_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.familyhead'),
        ),
    ]
