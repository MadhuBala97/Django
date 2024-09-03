# Generated by Django 5.0.6 on 2024-06-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apiapp", "0007_personwork_delete_superuser_alter_person_email_and_more"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="person",
            managers=[],
        ),
        migrations.AlterField(
            model_name="person",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="person_set",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="id",
            field=models.UUIDField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="person_set",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="personwork",
            name="id",
            field=models.UUIDField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
