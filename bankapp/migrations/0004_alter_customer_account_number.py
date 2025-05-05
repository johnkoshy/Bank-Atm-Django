from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('bankapp', '0003_alter_customer_withdrawal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Customer',
            name='account_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]