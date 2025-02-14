from django.contrib import admin
from .models import Menu, MasterData, FoodItem, Testimonial, Reservation, GalleryImage, AboutUs, BannerContent, Service, FooterContent, SocialMedia
from unfold.admin import ModelAdmin

@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    list_display = ('name', 'icon_class')

@admin.register(MasterData)
class MasterDataAdmin(ModelAdmin):
    list_display = ('category_code', 'value')

@admin.register(FoodItem)
class FoodItemAdmin(ModelAdmin):
    list_display = ('name', 'menu', 'price')

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = ('name', 'phone_number', 'number_of_people', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'phone_number')    

@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ('css_class', 'image')
    search_fields = ('css_class',)

@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    list_display = ('image1', 'image2', 'image3', 'image4', 'experience_years', 'master_chefs')
    search_fields = ('experience_years', 'master_chefs')

@admin.register(BannerContent)
class BannerContentAdmin(ModelAdmin):
    list_display = ('header', 'header2', 'paragraph1')
    search_fields = ('header',)    

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('icon', 'heading', 'description')
    search_fields = ('heading',)

@admin.register(FooterContent)
class FooterContentAdmin(ModelAdmin):
    list_display = ('address', 'phone_number', 'email', 'reservation_number')
    search_fields = ('address', 'phone_number', 'email')

@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin):
    list_display = ('icon', 'url')
    search_fields = ('icon', 'url')    