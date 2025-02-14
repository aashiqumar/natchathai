from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Menu, FoodItem, Testimonial, GalleryImage, AboutUs, BannerContent, Service, FooterContent, SocialMedia
from .forms import ReservationForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    menu_items = Menu.objects.all()
    food_items = FoodItem.objects.all()
    testimonials = Testimonial.objects.all()
    banner_content = BannerContent.objects.first()
    gallery_images = GalleryImage.objects.all()
    about_us = AboutUs.objects.first()
    services = Service.objects.all()
    footer_content = FooterContent.objects.first()
    social_media_links = SocialMedia.objects.all()

    if request.method == 'POST':
        logger.info("Form submission received")
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the reservation to the database
            logger.info("Form is valid and saved")
            messages.success(request, "Your reservation is requested. We will update you shortly.")
            return redirect('index')  # Redirect to clear the form and avoid resubmission
        else:
            logger.info("Form is invalid")
            messages.error(request, "There was an error with your reservation. Please try again.")
    else:
        form = ReservationForm()

    return render(request, 'restaurant/index.html', {
        'menu_items': menu_items,
        'food_items': food_items,
        'testimonials': testimonials,
        'form': form,
        'banner_content': banner_content,
        'gallery_images': gallery_images,
        'about_us': about_us,
        'services': services,
        'footer_content': footer_content,
        'social_media_links': social_media_links,
    })