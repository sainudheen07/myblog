from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BlogData
from . forms import Blogform
# Create your views here.
def BlogAdd(request):
    if request.method=='POST':
        hedding=request.POST.get('hedding')
        content=request.POST.get('content')
        date=request.POST.get('date')
        auther=request.POST.get('auther')
        img=request.POST.get('image')
        obj=BlogData(hedding=hedding,content=content,date=date,auther=auther,img=img)
        obj.save()
    obj1=BlogData.objects.all()
    return render(request, 'about.html', {'obj1': obj1})
    # return HttpResponse("hello")

def home(request):
    return render(request, 'index.html')


def delete(request,id):

    task=BlogData.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect ('blog:BlogAdd')
    return render(request,'delete.html',{'task':task})
def update(request,id):
    task=BlogData.objects.get(id=id)
    form=Blogform(request.POST or None,instance=task )
    if form.is_valid():
        form.save()
        return redirect('blog:BlogAdd')
    return render(request,'edit.html',{'task':task,'form':form})


