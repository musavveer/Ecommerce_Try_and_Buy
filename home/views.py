from django.shortcuts import render, redirect,HttpResponse

from home.models import Contact, Photo
from datetime import datetime
from django.contrib import messages


from home import meshroom_CLI
from home import RunBlender
from home import ExtractImages

import threading
modelDone = False
# Create your views here.
def index(request):
    #context - set of variable sent to template
    #usually data from model is fetchedand sent to template
    
    
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    #return HttpResponse("This is about")
    return render(request, 'about.html')

def profile(request):
    if modelDone == True:
        messages.success(request, "Your models have been created")
    return render(request, 'profile.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, desc=desc, date = datetime.today())

        contact.save()
        
        messages.success(request, "Your message has been sent")


    return render(request, 'contact.html')



def addPhoto(request):

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist('images')
        
        for image in images:
            photo = Photo.objects.create(
                image=image,
            )

        print("the images are sent to meshroom and processed")

        
        def thread_(request):
            #ExtractImages.extract()
            global modelDone
            #meshroom_CLI.main()
            RunBlender.runBlender()
            modelDone = True
            return redirect('profile')

        threadObj = threading.Thread(target=thread_ , args=[request])
        threadObj.start()
        return redirect('profile')
    
    return render(request, 'photos/add.html')


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


def product1(request):
    return render(request, 'product1.html')


def product2(request):
    return render(request, 'product2.html')


def product3(request):
    return render(request, 'product3.html')


def product4(request):
    return render(request, 'product4.html')


def product5(request):
    return render(request, 'product5.html')


def product6(request):
    return render(request, 'product6.html')


    