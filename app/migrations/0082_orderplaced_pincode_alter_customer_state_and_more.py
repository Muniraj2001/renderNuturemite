# Generated by Django 4.2.7 on 2024-01-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0081_remove_orderplaced_pincode_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='pincode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Gujrat', 'Gujrat'), ('Assam', 'Assam'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Goa', 'Goa'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Haryana', 'Haryana'), ('Bihar', 'Bihar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('Packed', 'packed'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('B12', 'Vitamin B12'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('C', 'Vitamin C'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('OG', 'Organic'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('B12', 'Vitamin B12'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('C', 'Vitamin C'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('OG', 'Organic'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('B12', 'Vitamin B12'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('C', 'Vitamin C'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('OG', 'Organic'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('B12', 'Vitamin B12'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('C', 'Vitamin C'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('OG', 'Organic'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('B12', 'Vitamin B12'), ('GH', 'General Health'), ('SH', 'Sexual health'), ('C', 'Vitamin C'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('OG', 'Organic'), ('AV', 'Ayurvedic')], max_length=3),
        ),
    ]
