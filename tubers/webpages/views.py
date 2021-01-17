from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import YouTuber


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = YouTuber.objects.order_by('-created_at').filter(is_featured=True)
    all_youtubers = YouTuber.objects.order_by('-created_at')
    data = {
        "sliders": sliders,
        "teams": teams,
        "featured_youtubers": featured_youtubers,
        "all_youtubers": all_youtubers
    }
    return render(request=request, template_name='webpages/home.html', context=data)


def about(request):
    return render(request=request, template_name='webpages/about.html')


def services(request):
    return render(request=request, template_name='webpages/services.html')


def contact(request):
    return render(request=request, template_name='webpages/contact.html')


