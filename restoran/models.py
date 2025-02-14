from django.db import models
from django.contrib.auth.models import User

class MasterData(models.Model):
    category_code = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category_code} - {self.value}"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.ForeignKey(MasterData, on_delete=models.CASCADE, limit_choices_to={'category_code': 'icon'})

    def __str__(self):
        return self.name
    

class FoodItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Optional price
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)  # Optional image
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Optional image URL

    def __str__(self):
        return self.name # Optional image
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name    
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    number_of_people = models.IntegerField()
    date = models.CharField(max_length=10)  # Changed to CharField
    time = models.CharField(max_length=8)   # Changed to CharField
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending')

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
    

class GalleryImage(models.Model):
    CSS_CLASS_CHOICES = [
        ('gallery-image-one', 'Gallery Image One'),
        ('gallery-image-two', 'Gallery Image Two'),
        ('gallery-image-three', 'Gallery Image Three'),
        ('gallery-image-four', 'Gallery Image Four'),
        ('gallery-image-five', 'Gallery Image Five'),
        ('gallery-image-six', 'Gallery Image Six'),
    ]

    image = models.URLField(max_length=200)
    css_class = models.CharField(max_length=50, choices=CSS_CLASS_CHOICES)

    def __str__(self):
        return self.css_class
    

class AboutUs(models.Model):
    image1 = models.URLField(max_length=200)
    image2 = models.URLField(max_length=200)
    image3 = models.URLField(max_length=200)
    image4 = models.URLField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    experience_years = models.IntegerField()
    master_chefs = models.IntegerField()

    def __str__(self):
        return "About Us Section"    
    

class BannerContent(models.Model):
    header = models.CharField(max_length=200)
    header2 = models.TextField(blank=True, null=True)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.header


class Service(models.Model):
    icon = models.ForeignKey(MasterData, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.heading
    
class SocialMedia(models.Model):
    icon = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.icon

class FooterContent(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    open_hours = models.TextField()
    reservation_number = models.CharField(max_length=20)

    def __str__(self):
        return "Footer Content"    