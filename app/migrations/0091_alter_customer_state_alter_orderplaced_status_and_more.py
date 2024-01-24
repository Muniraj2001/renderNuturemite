# Generated by Django 4.2.7 on 2024-01-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0090_remove_client_email_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Chandigarh', 'Chandigarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Goa', 'Goa'), ('Haryana', 'Haryana'), ('Daman and Diu', 'Daman and Diu'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chattisgarh', 'Chattisgarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujrat'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Packed', 'packed'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic'), ('OG', 'Organic'), ('D3', 'Vitamin D3'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('DH', 'Digestive Health')], max_length=3),
        ),
    ]