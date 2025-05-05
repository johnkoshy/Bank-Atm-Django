from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('bankapp', '0004_alter_customer_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Customer',
            name='customer_name',
            field=models.CharField(max_length=20, default="Unknown"),
        ),
    ]