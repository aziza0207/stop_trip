# Generated by Django 4.2.5 on 2023-10-02 07:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type_of_service', models.CharField(blank=True, choices=[('sale', 'Продажа'), ('rent', 'Аренда')], max_length=25, verbose_name='Тип услуги')),
                ('property_city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('property_district', models.CharField(blank=True, max_length=100, verbose_name='Район')),
                ('property_coords', location_field.models.plain.PlainLocationField(blank=True, max_length=63, verbose_name='Координаты')),
                ('property_building_max_floor', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество этажей в доме')),
                ('property_floor', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Номер этажа')),
                ('property_bathroom_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество санузлов')),
                ('property_bathroom_type', models.CharField(blank=True, choices=[('combined', 'Совмещённый'), ('separate', 'Раздельный')], max_length=100, verbose_name='Тип санузла')),
                ('property_area', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Общая площадь')),
                ('property_living_area', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Жилая площадь')),
                ('property_balcony', models.CharField(blank=True, choices=[('yes', 'Есть'), ('no', 'Нет'), ('loggia', 'Лоджия')], max_length=50, verbose_name='Балкон')),
                ('property_has_furniture', models.BooleanField(default=False, verbose_name='Мебель')),
                ('property_house_type', models.CharField(blank=True, choices=[('panel', 'Панельный'), ('brick', 'Кирпичный'), ('wooden', 'Деревянный'), ('block', 'Блочный')], max_length=100, verbose_name='Тип дома')),
                ('property_has_parking', models.BooleanField(default=False, verbose_name='Есть парковка')),
                ('property_rental_condition', models.CharField(blank=True, choices=[('family', 'Семье'), ('office', 'Под офис'), ('students', 'Студентам'), ('not_companies', 'Не компаниям')], max_length=100, verbose_name='Условия аренды')),
                ('property_prepayment', models.CharField(blank=True, choices=[('without', 'Без предоплаты'), ('month', 'Месяц'), ('two_months', 'Два месяца'), ('three_months', 'Три месяца'), ('half_a_year', 'Пол года')], max_length=50, verbose_name='Предоплата')),
                ('property_sleeping_places', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество спальных мест')),
                ('property_rooms_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество комнат')),
                ('transport_type_of_service', models.CharField(blank=True, choices=[('sale', 'Продажа'), ('rent', 'Аренда')], max_length=25, null=True, verbose_name='Тип услуги')),
                ('transport_type', models.CharField(blank=True, choices=[('ground', 'Наземный'), ('water', 'Водный')], max_length=50, null=True, verbose_name='Тип транспорта')),
                ('transport_category', models.CharField(blank=True, choices=[('motorcycle', 'Мотоцикл'), ('moped', 'Мопед'), ('car', 'Легковой автомобиль'), ('truck', 'Грузовой автомобиль'), ('bus', 'Автобус'), ('tricycle', 'Трицикл'), ('trailer', 'Трэйлер'), ('roadhouse', 'Дом на колёсах'), ('motorboat', 'Моторная лодка'), ('oar_boat', 'Вёсельная лодка'), ('boat', 'Катер'), ('other', 'Другое')], max_length=50, null=True, verbose_name='Категория транспорта')),
                ('transport_engine_type', models.CharField(blank=True, choices=[('fuel', 'Бензин'), ('diesel', 'Дизель'), ('gas', 'Газ'), ('electric', 'Электричество'), ('hybrid', 'Гибрид')], max_length=100, null=True, verbose_name='Тип двигателя')),
                ('transport_drive_type', models.CharField(blank=True, choices=[('front_wheel', 'Передний'), ('rear_wheel', 'Задний'), ('all_wheel', 'Постоянный полный'), ('four_wheel', 'Подключаемый полный')], max_length=50, null=True, verbose_name='Привод')),
                ('transport_engine_volume', models.FloatField(blank=True, choices=[(1.0, 1.0), (1.1, 1.1), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (1.5, 1.5), (1.6, 1.6), (1.7, 1.7), (1.8, 1.8), (1.9, 1.9), (2.0, 2.0), (2.1, 2.1), (2.2, 2.2), (2.3, 2.3), (2.4, 2.4), (2.5, 2.5), (2.6, 2.6), (2.7, 2.7), (2.8, 2.8), (2.9, 2.9), (3.0, 3.0), (3.1, 3.1), (3.2, 3.2), (3.3, 3.3), (3.4, 3.4), (3.5, 3.5), (3.6, 3.6), (3.7, 3.7), (3.8, 3.8), (3.9, 3.9), (4.0, 4.0), (4.1, 4.1), (4.2, 4.2), (4.3, 4.3), (4.4, 4.4), (4.5, 4.5), (4.6, 4.6), (4.7, 4.7), (4.8, 4.8), (4.9, 4.9), (5.0, 5.0), (5.1, 5.1), (5.2, 5.2), (5.3, 5.3), (5.4, 5.4), (5.5, 5.5), (5.6, 5.6), (5.7, 5.7), (5.8, 5.8), (5.9, 5.9), (6.0, 6.0), (6.1, 6.1), (6.2, 6.2), (6.3, 6.3), (6.4, 6.4), (6.5, 6.5), (6.6, 6.6), (6.7, 6.7), (6.8, 6.8), (6.9, 6.9), (7.0, 7.0), (7.1, 7.1), (7.2, 7.2), (7.3, 7.3), (7.4, 7.4), (7.5, 7.5), (7.6, 7.6), (7.7, 7.7), (7.8, 7.8), (7.9, 7.9), (8.0, 8.0), (8.1, 8.1), (8.2, 8.2), (8.3, 8.3), (8.4, 8.4), (8.5, 8.5), (8.6, 8.6), (8.7, 8.7), (8.8, 8.8), (8.9, 8.9), (9.0, 9.0), (9.1, 9.1), (9.2, 9.2), (9.3, 9.3), (9.4, 9.4), (9.5, 9.5), (9.6, 9.6), (9.7, 9.7), (9.8, 9.8), (9.9, 9.9)], null=True, verbose_name='Объём')),
                ('transport_year_of_production', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)], verbose_name='Год производства')),
                ('transport_transmission_type', models.CharField(blank=True, choices=[('mechanic', 'Механическая'), ('automatic', 'Автоматическая')], max_length=50, null=True, verbose_name='Тип коробки передач')),
                ('transport_body_type', models.CharField(blank=True, choices=[('sedan', 'Седан'), ('liftback', 'Лифтбэк'), ('coupe', 'Купе'), ('convertible', 'Кабриолет'), ('hatchback', 'Хэтчбэк'), ('SUV', 'Внедорожник'), ('limousine', 'Лимузин'), ('pickup', 'Пикап')], max_length=50, null=True, verbose_name='Тип кузова')),
                ('transport_condition', models.CharField(blank=True, choices=[('new', 'Новый'), ('used', 'Б/у'), ('salvage', 'Аварийный'), ('spare', 'На запчасти')], max_length=100, null=True, verbose_name='Состояние')),
                ('transport_passengers_quality', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во пассажиров')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания')),
                ('is_online', models.BooleanField(default=False, verbose_name='Онлайн')),
                ('job_type', models.CharField(blank=True, choices=[('full_time', 'Полный день'), ('part_time', 'Неполный день')], max_length=25, null=True, verbose_name='Тип работы')),
                ('job_duration', models.CharField(blank=True, choices=[('OneTimeTask', 'Разовое задание'), ('temporary', 'Временная работа'), ('permanent', 'Постоянная работа'), ('other', 'Другое')], max_length=25, null=True, verbose_name='Продолжительность работы')),
                ('job_payment_type', models.CharField(blank=True, choices=[('hourly_payment', 'почасовая оплата'), ('daily_payment', 'ежедневная оплата'), ('weekly_payment', 'еженедельная оплата'), ('monthly_payment', 'ежемесячная оплата'), ('other', 'другое')], max_length=25, null=True, verbose_name='Тип оплаты')),
                ('job_experience', models.BooleanField(default=False, verbose_name='С опытом')),
                ('home_visit', models.BooleanField(default=False, verbose_name='Выезд на дом')),
                ('taxi_unit', models.CharField(blank=True, choices=[('km', 'км'), ('hour', 'час'), ('route', 'маршрут')], max_length=20, null=True, verbose_name='Единица измерения')),
                ('taxi_type', models.CharField(blank=True, choices=[('economy', 'эконом'), ('comfort', 'комфорт'), ('business', 'бизнес'), ('station_wagon', 'универсал'), ('minivan', 'минивэн')], max_length=25, null=True, verbose_name='Вид такси')),
                ('category', models.CharField(choices=[('property', 'Недвижимость'), ('transport', 'Транспорт')], verbose_name='Категории')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликованно')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Слаг')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='PropertyAmenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Удобство',
                'verbose_name_plural': 'Удобства',
            },
        ),
        migrations.CreateModel(
            name='TransportBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TransportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='AdvertisementImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='offers/advertisement_image/image', verbose_name='Фотография')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='offers.advertisement', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='advertisement',
            name='property_amenities',
            field=models.ManyToManyField(blank=True, related_name='amenities', to='offers.propertyamenity', verbose_name='Удобства'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='transport_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transports', to='offers.transportbrand', verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='transport_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transports', to='offers.transportmodel', verbose_name='Модель'),
        ),
    ]
