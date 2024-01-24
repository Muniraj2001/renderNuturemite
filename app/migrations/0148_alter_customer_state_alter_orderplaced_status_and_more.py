# Generated by Django 4.2.7 on 2024-01-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0147_remove_product_new_field_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Chandigarh', 'Chandigarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Daman and Diu', 'Daman and Diu'), ('Haryana', 'Haryana'), ('Gujrat', 'Gujrat'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Goa', 'Goa'), ('Bihar', 'Bihar'), ('Assam', 'Assam'), ('Chattisgarh', 'Chattisgarh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Wey', 'On The Way'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Packed', 'packed')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('AV', 'Ayurvedic'), ('GH', 'General Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('DH', 'Digestive Health'), ('E', 'Vitamin E'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
    ]
