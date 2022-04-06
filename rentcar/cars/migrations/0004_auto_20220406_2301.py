# Generated by Django 3.2.9 on 2022-04-06 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_auto_20220116_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес доставки')),
                ('delivery_time', models.DateTimeField(verbose_name='Время доставки')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
        migrations.CreateModel(
            name='DeliveryZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100, verbose_name='Название района')),
                ('area_price', models.IntegerField(verbose_name='Тариф')),
            ],
            options={
                'verbose_name': 'Тариф на доставку',
                'verbose_name_plural': 'Тарифы на доставку',
            },
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_amount', models.IntegerField(verbose_name='Количество дней')),
            ],
            options={
                'verbose_name': 'Продление',
                'verbose_name_plural': 'Продления',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=70, verbose_name='Тип страхования')),
            ],
            options={
                'verbose_name': 'Тип страхования',
                'verbose_name_plural': 'Типы страхований',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_getting', models.DateField(verbose_name='Дата сдачии')),
                ('period', models.IntegerField(verbose_name='Период аренды')),
                ('order_price', models.IntegerField(verbose_name='Стоимость')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('condition', models.ManyToManyField(to='cars.Condition', verbose_name='Условия аренды')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.customer')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.delivery')),
                ('insurance', models.ManyToManyField(to='cars.Insurance', verbose_name='Тип страхования')),
                ('order_extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.extension')),
            ],
            options={
                'verbose_name': 'Сервис аренды',
                'verbose_name_plural': 'Сервис Аренды',
            },
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.deliveryzone', verbose_name='Зоны доставки'),
        ),
    ]
