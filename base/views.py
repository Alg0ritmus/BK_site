from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import *

from .uploadFileAndSave import *

import json

from django.http import JsonResponse


from django.core.paginator import Paginator


from django.contrib.auth.decorators import permission_required,login_required


# Create your views here.


def index(request):
    context = {
        "Posts": TopPosts.objects.all(),
        "Oznamy": Oznamy.objects.all()
    }
    return render(request, 'base/index.html', context)


def galeria(request):
    galeryObjs = Galeria.objects.all()
    context = {
        "galeries": galeryObjs
    }
    return render(request, 'base/galeria.html', context)


def galeria_get(request, pk):
    galery = get_object_or_404(Galeria, pk=pk)
    galeryObj = galery.images.all()
    context = {
        "images": galeryObj,
        "galery": galery
    }
    return render(request, 'base/galeria_article.html', context)

@permission_required('base.change_galeria')
def galeria_create(request):
    if request.method == 'POST':
        newGalery = Galeria.objects.create(title=request.POST['title'])
        img_urls = uploadImg(request)
        for url in img_urls:
            newImg = Obrazok.objects.create(title=url[0], url=url[1])
            saveNeeded = newGalery.images.add(newImg)
            if saveNeeded is not None:
                saveNeeded.save()
    return render(request, 'base/galeria_create.html')


@permission_required('base.change_galeria')
def galeria_delete(request, pk):
    if request.method == 'POST':
        galeryObj = get_object_or_404(Galeria, pk=pk)
        galeryObj.delete()
    return redirect('base:galeria')

@permission_required('base.change_galeria')
def galeria_add_img_to_galeria(request, pk):
    print("##", pk)
    if request.method == 'POST':
        galeryObj = get_object_or_404(Galeria, pk=pk)
        print(galeryObj)
        img_urls = uploadImg(request)
        print(">>>>IMGURLS", img_urls)
        for url in img_urls:
            newImg = Obrazok.objects.create(title=url[0], url=url[1])
            saveNeeded = galeryObj.images.add(newImg)
            if saveNeeded is not None:
                saveNeeded.save()

    return redirect('base:galeria_get', pk)

@permission_required('base.change_galeria')
def galeria_del_img_to_galeria(request, page, pk):
    if request.method == 'POST':
        img = get_object_or_404(Obrazok, pk=pk)
        img.delete()
    return redirect('base:galeria_get', page)



def archiv(request):
    archive = Clanok.objects.all()
    paginator = Paginator(archive, 5)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'archive': page_obj,
        'Posts': [post.clanok for post in TopPosts.objects.all()],
        'page_obj': page_obj
    }

    return render(request, 'base/archiv.html', context)

@permission_required('base.change_clanok')
def clanok_create_empty(request):
    newClanok = Clanok()
    newClanok.save()
    return redirect('base:clanok_create', newClanok.id)


def clanok(request, pk):
    myClanok = get_object_or_404(Clanok, pk=pk)
    context = {
        'clanok': myClanok,
        'komentare': myClanok.postcomment_set.all()
    }
    return render(request, 'base/clanok.html', context)


def clanok_body_RO(request, pk):
    myClanok = get_object_or_404(Clanok, pk=pk)
    context = {
        'clanok': myClanok.body,
    }
    return JsonResponse(context)

@permission_required('base.change_clanok')
def clanok_add_img(request, pk):
    print("##", pk)
    if request.method == 'POST':
        galeryObj = get_object_or_404(Clanok, pk=pk)
        print(galeryObj)
        img_urls = uploadImg(request)
        print(">>>>IMGURLS", img_urls)
        for url in img_urls:
            newImg = Obrazok.objects.create(title=url[0], url=url[1])
            saveNeeded = galeryObj.images.add(newImg)
            if saveNeeded is not None:
                saveNeeded.save()

    return redirect('base:clanok_create', pk)

@permission_required('base.change_clanok')
def clanok_create(request, pk):
    newClanok = get_object_or_404(Clanok, pk=pk)
    return render(request, 'base/clanok_create.html', {'clanok': newClanok})

@permission_required('base.change_clanok')
def clanok_update(request):
    if request.method == 'POST':
        # decode request body and parse
        serialized_data = json.loads(request.body.decode())
        newClanok = get_object_or_404(Clanok, pk=serialized_data['pk'])

        title = serialized_data['title']
        body = serialized_data['body']

        newClanok.title = title
        newClanok.body = body
        newClanok.save()
        print(">!!>", newClanok.title)

    return redirect('base:archiv')


def add_comment(request, pk):
    if request.method == 'POST':
        myCLanok = get_object_or_404(Clanok, pk=pk)
        PostComment.objects.create(
            author_name=request.POST['autor'], body=request.POST['text'], clanok=myCLanok)
        return redirect('base:clanok', pk)

@permission_required('base.change_clanok')
def clanok_delete(request, pk):
    get_object_or_404(Clanok, pk=pk).delete()
    return redirect('base:archiv')


def log_page(request):
    return render(request, 'base/log_page.html')

def log_out(request):
    logout(request)
    return redirect('base:home')

def login_bk(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('logged in sucessfully')
            return redirect('base:home')
        else:
            print('smthing goes wrong')

    return redirect('base:home')


def reg_bk(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            User.objects.create_user(
                username=username, email=email, password=password)
        except Exception as e:
            print(e)

    return redirect('base:home')

@permission_required('base.change_clanok')
def setTopPost(request, pk, pk_post):

    getPost = get_object_or_404(TopPosts, pk=pk_post)
    getClanok = get_object_or_404(Clanok, pk=pk)
    getPost.clanok = getClanok
    getPost.save()
    print(getPost.clanok)

    return redirect('base:archiv')

@permission_required('base.change_clanok')
def delTopPost(request, pk):

    getClanok = get_object_or_404(Clanok, pk=pk)
    post_id = getClanok.topposts.id

    getPost = get_object_or_404(TopPosts, pk=post_id)
    getPost.clanok = None

    getPost.save()

    return redirect('base:archiv')

@permission_required('base.change_clanok')
def oznam_add(request):
    print("adding >>")
    if request.method == 'POST':
        
        serialized_data = json.loads(request.body.decode())
        myClanok = get_object_or_404(Clanok,pk=serialized_data['clanok_id']) 
        try: 
            Oznamy.objects.create(clanok=myClanok)
        except:
            print("already created")

    return JsonResponse({"status":"Good"})
@permission_required('base.change_clanok')
def oznam_del(request):
    print("deleting >>")
    if request.method == 'POST':
       serialized_data = json.loads(request.body.decode())

       myClanok = get_object_or_404(Clanok,pk=serialized_data['clanok_id']) 
       myOznam=Oznamy.objects.get(pk=myClanok.oznamy.pk)
       myOznam.delete()

    return JsonResponse({"status":"Good"})

@login_required(login_url='../login/')
def dashboard(request):
    
    context = {
        "permissions":list(request.user.get_group_permissions())
        }
    return render(request, 'base/dashboard.html',context)

