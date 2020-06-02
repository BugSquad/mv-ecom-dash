# Generated by Django 2.2.11 on 2020-06-02 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20200602_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('vendor_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('badges', models.PositiveIntegerField()),
                ('category_id', models.PositiveIntegerField()),
                ('num_stock', models.PositiveIntegerField()),
                ('num_views', models.PositiveIntegerField()),
                ('num_purchases', models.PositiveIntegerField()),
                ('num_added_cart', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('a', 'active'), ('ia', 'inactive')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]