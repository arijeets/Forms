# Generated by Django 3.1 on 2020-10-01 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sha_final_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_mast',
            name='Source_name',
            field=models.ForeignKey(db_column='Source_ID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sha_final_app.sourcemaster'),
        ),
        migrations.AlterField(
            model_name='call_trans',
            name='Candidate_ID',
            field=models.ForeignKey(db_column='Candidate_ID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sha_final_app.call_mast'),
        ),
        migrations.AlterField(
            model_name='candidatetrainingmaster',
            name='Candidate_ID',
            field=models.ForeignKey(db_column='Candidate_ID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sha_final_app.call_mast'),
        ),
        migrations.AlterField(
            model_name='candidatetrainingmaster',
            name='Course_ID',
            field=models.ForeignKey(db_column='Course_ID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sha_final_app.coursemaster'),
        ),
        migrations.AlterField(
            model_name='training_trans',
            name='Course_ID',
            field=models.ForeignKey(db_column='Course_ID', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sha_final_app.coursemaster'),
        ),
    ]
