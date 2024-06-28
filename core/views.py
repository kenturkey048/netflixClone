from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile, Movie

def home(request):
    if request.user.is_authenticated:
        return redirect('/profile-list')
    else:
        return render(request, 'core/index.html')

@login_required
def profile(request):
    profile = Profile.objects.all()
    return render(request, 'core/profile.html', {
    'profile':profile
    })


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_profile = Profile(
            name = request.POST['name'],
            age_limit = request.POST['age_limit']
            )
            new_profile.save()
            return redirect('/profile-list')
    else:
        form = ProfileForm()
    return render(request, 'core/create_profile.html', {
    'form':form
    })

@login_required
def profile_detail(request, pk):
    profiles = Profile.objects.get(uuid=pk)
    movies = Movie.objects.filter(age_limit=profiles.age_limit)
    return render(request, 'core/movie_list.html', {
    'profiles':profiles,
    'movies':movies,
    })


@login_required
def movie_detail(request, pk):
    movies = Movie.objects.get(uuid=pk)
    return render(request, 'core/movie_detail.html', {
    'movies':movies
    })


def show_movie(request, pk):
    movies = Movie.objects.get(uuid=pk)
    movie = movies.video.values()
    return render(request, 'core/show_movies.html', {
        'movies':movies
    })
