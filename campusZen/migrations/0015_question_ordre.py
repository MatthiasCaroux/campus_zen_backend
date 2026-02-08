from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusZen', '0014_alter_question_typequestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ordre',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['ordre']},
        ),
    ]
