from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.


def index(request):
    return render(request, 'post/index.html')


def nutrition(request):

    form =CommentForm()

    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            your_comment=form.cleaned_data['your_comment']
            Comment.objects.create(name=name, your_comment=your_comment)

            messages.success(request,'Your comment has been successfully submitted')
            return redirect('nutrition')
        else:
            form=CommentForm()
        
        # Fetch nutrition posts
    nutrition_posts=Post.objects.filter(title__icontains='nutrition')
    comments=Comment.objects.all()
    # Use 'icontains' for case-insensitive matching
    context ={'nutrition_posts':nutrition_posts,
              'form':form, 'comments':comments}
    return render(request, 'post/nutrition.html', 
         context
    )

def edit_comment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)

    if request.method== "POST":
        form=CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request,'Your comment has been updated successfuly')
            return redirect('nutrition')
    else:
        form =CommentForm

    return redirect(request,'post/nutrition.html',{'form':form,'comment':comment})

def delete_comment(request, pk):
    comment=get_object_or_404(Comment,pk=pk)
    if request.method=="POST":
            comment.delete()
            messages.success(request,'Your comment has been successfully deleted')
            return redirect('nutrition')
        
    return render(request,'post/nutrition.html', {'comment':comment})





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


