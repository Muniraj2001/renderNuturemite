# Generated by Django 4.2.7 on 2023-11-10 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_customer_alter_product_category_delete_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Goa', 'Goa'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Assam', 'Assam'), ('Gujrat', 'Gujrat'), ('Chattisgarh', 'Chattisgarh'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Bihar', 'Bihar'), ('Haryana', 'Haryana'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Chandigarh', 'Chandigarh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]