# Generated by Django 4.2.7 on 2024-01-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0126_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Chattisgarh', 'Chattisgarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Assam', 'Assam'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Chandigarh', 'Chandigarh'), ('Bihar', 'Bihar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'packed'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('K', 'Vitamin K'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('PC', 'Personal Care'), ('DH', 'Digestive Health'), ('GH', 'General Health'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic')], max_length=3),
        ),
    ]
