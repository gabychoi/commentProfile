from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    return render(request, 'filterApp/index.html')

def login(request):
    email = request.POST['email']
    pwd = request.POST['password']
    print(">>>>>>>>>>>>>>>>>>>>>>>>> ", email)
    print(">>>>>>>>>>>>>>>>>>>>>>>>> ", pwd)
    try:
        user = User.objects.get(user_email=email, user_pwd=pwd)
        print(">>>>>>>>>>> login success" , user.user_name)
    except:
        return redirect('index')

    context = {}
    if user is not None :
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        context['name']  = request.session['user_name']
        context['email'] = request.session['user_email']
        return redirect('profile')
    # else:
    #     return redirect('login')
    return render(request, 'filterApp/index.html')

def logout(request) :
    request.session['user_name'] = {}
    request.session.modified =True

    return redirect('index')

def register(request) :
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        name = request.POST['name']

        register = User(user_email=email, user_pwd=pwd, user_name=name)
        register.save()
        print('>>>>>>>>>>>>>>>>>>>>', register.user_name)
        context = {}
        if register is not None :
            request.session['flag'] = 1
            context['flag'] = request.session['flag']
    # return redirect('index')
    return render(request, 'filterApp/index.html', context)


def profile(request):
    if request.session.get('user_email'):
        user = User.objects.all()
        print('>>>>>>>>>>>>>>>>>>>>', user)
        context = {'email': request.session['user_email'],
                   'name': request.session['user_name']}
        return render(request, 'filterApp/profile.html', context)

    # if request.session.get('user_email'):
    #     posts = Post.objects.all()
    #     print('>>>>>>', posts)
    #     context = {'email': request.session['user_email'],
    #                'name': request.session['user_name'],
    #                'posts': posts}
    #     return render(request, 'filterApp/profile.html', context)


def home(request):
    return render(request, 'filterApp/home.html')

def user_detail(request):
    return render(request, 'filterApp/user_detail.html')

def edit_profile(request):
    return render(request, 'filterApp/edit_profile.html')

def profile_wall(request):
    return render(request, 'filterApp/profile_wall.html')

def view_photo(request):
    return render(request, 'filterApp/view_photo.html')

def file_manager(request):
    return render(request, 'filterApp/file_manager.html')

def friends(request):
    return render(request, 'filterApp/friends.html')

def createText(request):
    post_input_str = request.POST['postcontent']
    new_post = Text(content = post_input_str)
    new_post.save()
    return HttpResponseRedirect(reverse('profile'))
    # return HttpResponse("createText를 할거야! => " + post_input_str)


def createAvatar(request):
    img_input = request.FILES['photo']
    new_img = Avatar(image = img_input)
    new_img.save()
    print('사진 저장 성공!!')
    return HttpResponseRedirect(reverse('profile'))

# def people(request, username):
#     person = get_object_or_404(get_user_model(), username=username)
#     return render(request, 'filterApp/profile.html', {'person':person})

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView):
    medel = Photo
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DeleteView):
    model = Photo
    template_name_suffix = '_detail'