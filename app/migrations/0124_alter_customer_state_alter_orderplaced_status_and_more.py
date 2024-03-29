# Generated by Django 4.2.7 on 2024-01-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0123_productpricedrop_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Assam', 'Assam'), ('Chattisgarh', 'Chattisgarh'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Bihar', 'Bihar'), ('Haryana', 'Haryana'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Gujrat', 'Gujrat')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('On The Wey', 'On The Way'), ('Pending', 'Pending'), ('Packed', 'packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('E', 'Vitamin E'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('K', 'Vitamin K'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('IH', 'Immune Health'), ('C', 'Vitamin C'), ('GH', 'General Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('E', 'Vitamin E'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('K', 'Vitamin K'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('IH', 'Immune Health'), ('C', 'Vitamin C'), ('GH', 'General Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('E', 'Vitamin E'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('K', 'Vitamin K'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('IH', 'Immune Health'), ('C', 'Vitamin C'), ('GH', 'General Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('E', 'Vitamin E'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('K', 'Vitamin K'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('IH', 'Immune Health'), ('C', 'Vitamin C'), ('GH', 'General Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('E', 'Vitamin E'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('K', 'Vitamin K'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('IH', 'Immune Health'), ('C', 'Vitamin C'), ('GH', 'General Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
    ]
