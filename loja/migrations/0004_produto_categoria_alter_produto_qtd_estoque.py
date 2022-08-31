# Generated by Django 4.1 on 2022-08-24 12:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_produto_qtd_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='loja.categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd_estoque',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'O estoque deve ser igual ou superior a 0'), django.core.validators.MaxValueValidator(100, 'O estoque deve ser igual ou superior a 100')]),
        ),
    ]
