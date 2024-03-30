from django.core.management.base import BaseCommand, CommandError
from gp8app.models import Car
from django.core.files import File

image_path1 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/black_accord_2018.jpg"
image_path2 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/white_camry_2019.jpg"
image_path3 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/silver_fusion_2020.jpg"
image_path4 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/red_impala_2017.jpg"
image_path5 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/blue_altima_2018 .jpg"
image_path6 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/gray_sonata_2019.jpg"
image_path7 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/black_optima_2020.jpg"
image_path8 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/white_passat_2017.jpg"
image_path9 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/silver_3series_2018.jpg"
image_path10 = "/Users/anningtian/Desktop/Desktop/Grad School(NEU)/CS5200/ProjectNew/car_image/red_a4_2019.jpg"

class Command(BaseCommand):
    help = 'Upload images for cars'

    def handle(self, *args, **options):
        car_images = [
            ('1HGCM82633A004352', image_path1),
            ('1HGCM82633A004353', image_path2),
            ('1HGCM82633A004354', image_path3),
            ('1HGCM82633A004355', image_path4),
            ('1HGCM82633A004356', image_path5),
            ('1HGCM82633A004357', image_path6),
            ('1HGCM82633A004358', image_path7),
            ('1HGCM82633A004359', image_path8),
            ('1HGCM82633A004360', image_path9),
            ('1HGCM82633A004361', image_path10),
            # Add tuples for each car and image path
        ]

        for vin, image_path in car_images:
            try:
                car = Car.objects.get(vin=vin)
                with open(image_path, 'rb') as img_file:
                    car.image.save(f'{vin}.jpg', File(img_file), save=True)
                self.stdout.write(self.style.SUCCESS(f'Image added to Car with VIN {vin}'))
            except Car.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Car with VIN {vin} does not exist.'))
            except Exception as e:
                raise CommandError(f'An error occurred: {e}')
