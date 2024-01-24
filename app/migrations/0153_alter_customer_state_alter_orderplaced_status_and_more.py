# Generated by Django 5.0.1 on 2024-01-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0152_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam'), ('Chattisgarh', 'Chattisgarh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Delhi', 'Delhi'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Chandigarh', 'Chandigarh'), ('Daman and Diu', 'Daman and Diu'), ('Gujrat', 'Gujrat'), ('Bihar', 'Bihar'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Haryana', 'Haryana'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Goa', 'Goa')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Packed', 'packed'), ('On The Wey', 'On The Way'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('GH', 'General Health'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3')], max_length=3),
        ),
    ]
