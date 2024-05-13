# Generated by Django 4.0.3 on 2024-04-04 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_capital_alternative_names'),
        ('general', '0013_alter_polity_degree_of_centralization_degree_of_centralization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='polity_capital',
            name='polity_cap',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polity_caps', to='core.capital'),
        ),
        migrations.AlterField(
            model_name='polity_degree_of_centralization',
            name='degree_of_centralization',
            field=models.CharField(choices=[('loose', 'loose'), ('confederated state', 'confederated state'), ('unitary state', 'unitary state'), ('nominal', 'nominal'), ('quasi-polity', 'quasi-polity'), ('none', 'none'), ('unknown', 'unknown'), ('uncoded', 'uncoded')], max_length=500),
        ),
    ]
