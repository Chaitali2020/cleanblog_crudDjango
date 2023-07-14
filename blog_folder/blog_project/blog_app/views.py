from django.shortcuts import render,HttpResponse,redirect
from .models import blog_model


# Create your views here.
def index(request):
    d=blog_model.objects.all()
    
    return render(request,'index.html',{'data':d})

def create_blog(request):
    if request.method=='POST':
        h=request.POST['bhead']
        c=request.POST['bcat']
        d=request.POST['bdesc']
        n=request.POST['bname']
        dat=request.POST['bdate']
        b1=blog_model.objects.create(bhead=h,bcat=c,bdesc=d,bname=n,bdate=dat)
        b1.save()
        # return HttpResponse(h)
        return redirect('/')
    else:
        return render(request,'create_blog.html')

def edit(request,rid):
    if request.method=='POST':
        h=request.POST['bhead']
        c=request.POST['bcat']
        d=request.POST['bdesc']
        n=request.POST['bname']
        dat=request.POST['bdate']
        b=blog_model.objects.filter(id=rid)
        b.update(bhead=h,bcat=c,bdesc=d,bname=n,bdate=dat)
        return redirect('/')
    else:
        content={}
        content['data']=blog_model.objects.get(id=rid)
        return render(request,'edit_blog.html',content)

    # return HttpResponse("id is edit" + rid)

def delete(request,rid):
    x=blog_model.objects.get(id=rid)
    x.delete()
    return redirect('/')
    # return HttpResponse("id is delete" + rid)