from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusZen', '0015_question_ordre'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
