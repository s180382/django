# Generated by Django 4.2.6 on 2024-01-04 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('category', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='app.question')),
            ],
            options={
                'db_table': 'answers',
            },
        ),
    ]
