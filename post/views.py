from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    return render(request, 'post/index.html')


def nutrition(request):
    nutrition_posts=Post.objects.filter(title__icontains='nutrition')
    # Use 'icontains' for case-insensitive matching
    context ={'nutrition_posts':nutrition_posts}
    return render(request, 'post/nutrition.html', 
         context
    )

def sports_tips(request):
    tips=Post.objects.filter(title__icontains='tips')
    context={'tips':tips}
    return render(request,'post/sports_tips.html',context)

def insights(request):
    insights=Post.objects.filter(title__icontains='insights')
    context={'insights':insights}
    return render(request, 'post/insights.html', context)

def health(request):
    health_tips=Post.objects.filter(title__icontains='health')
    context={'health_tips': health_tips}
    return render(request,'post/health.html', context)


