from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusZen', '0016_questionnaire_actif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personne',
            old_name='emailPers',
            new_name='login',
        ),
        migrations.AlterField(
            model_name='personne',
            name='login',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
