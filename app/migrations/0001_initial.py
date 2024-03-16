from django.db import migrations, models

class Migrations(migrations.Migration):
    
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]