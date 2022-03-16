from django.shortcuts import render
from community.forms import Form
from .models import Article

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()  #필드값 저장

    else:
        form =Form()

    return render(request,'write.html', {'form': form })


#글 작성 목록
def articlelist(request):
    article_list=Article.objects.all()
    return render(request,'list.html',{'article_list': article_list})
