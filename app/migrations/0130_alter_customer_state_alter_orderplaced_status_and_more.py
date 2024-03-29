# Generated by Django 4.2.7 on 2024-01-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0129_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Goa', 'Goa'), ('Assam', 'Assam'), ('Chattisgarh', 'Chattisgarh'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Chandigarh', 'Chandigarh'), ('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Bihar', 'Bihar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('On The Wey', 'On The Way'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('E', 'Vitamin E')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('A', 'Vitamin A'), ('B12', 'Vitamin B12'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('E', 'Vitamin E')], max_length=3),
        ),
    ]
