from django.shortcuts import render, get_object_or_404
from .models import YouTuber


def youtubers(request):
    youtubers = YouTuber.objects.order_by('-created_at')
    data = {
        "youtubers": youtubers
    }
    return render(request=request, template_name="youtubers/youtubers.html", context=data)


def youtubers_detail(request, id):
    tuber = get_object_or_404(YouTuber, pk=id)
    data = {
        "tuber": tuber
    }
    return render(request=request, template_name="youtubers/youtuber_detail.html", context=data)


def search(request):
    youtubers = YouTuber.objects.order_by('-created_at')
    city_search = YouTuber.objects.values_list('city', flat=True).distinct()
    category_search = YouTuber.objects.values_list('category', flat=True).distinct()
    camera_search = YouTuber.objects.values_list('camera', flat=True).distinct()

    if "keyword" in request.GET:
        keyword = request.GET['keyword']
        youtubers = youtubers.filter(description__contains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            youtubers = youtubers.filter(city__iexact=city)

    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            youtubers = youtubers.filter(camera__iexact=camera)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            youtubers = youtubers.filter(category__iexact=category)

    data = {
        "youtubers": youtubers,
        "city_search": city_search,
        "category_search": category_search,
        "camera_search": camera_search
    }
    return render(request=request, template_name="youtubers/search.html", context=data)

