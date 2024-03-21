from django.shortcuts import render,redirect
from .models import Category, Photo

# Create your views here.
def gallery(reqeust):
    category = reqeust.GET.get('category')
    # print('category:',category)
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(cataeory__name=category)
    cataeory=Category.objects.all()
    # photos=Photo.objects.all()
    context={'categories': cataeory,'photos':photos}
    return render(reqeust,'photos/galery.html',context)

def viewphoto(reqeust,pk):
    photo=Photo.objects.get(id=pk)
    return render(reqeust,'photos/photo.html',{'photo':photo})
    
def addphoto(reqeust):
    categories=Category.objects.all()
    if reqeust.method == 'POST':
        data= reqeust.POST
        image= reqeust.FILES.get('image')
        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['create'] != '':
            category,created = Category.objects.get_or_create(name=data['create'])
        else:
            category = None
        photo=Photo.objects.create(cataeory=category,
                                   description=data['descript'],
                                   image=image,)
        return redirect('gallery')

    
    context={'categories': categories}

    return render(reqeust,'photos/add.html',context)