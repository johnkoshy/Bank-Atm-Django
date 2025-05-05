from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('bankapp', '0002_alter_customer_balance_alter_customer_deposit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Customer',
            name='withdrawal',
            field=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True),
        ),
    ]