# Generated by Django 4.0.4 on 2022-04-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_categories_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipements',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='core.categories'),
        ),
    ]