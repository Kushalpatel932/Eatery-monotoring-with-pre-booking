# Generated by Django 2.1.5 on 2020-02-05 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(choices=[('vage', 'Veg Food'), ('nonvage', 'Non Veg Food')], default='Select', max_length=30)),
                ('category', models.CharField(choices=[('Fast_Food', 'Fast Food'), ('Break_Fast', 'Break Fast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Select', max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='upload/')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.Meal'),
        ),
    ]
