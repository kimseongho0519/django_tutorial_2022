from django.shortcuts import get_object_or_404, redirect, render
from community.forms import Form
from .models import Article

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()  #필드값 저장
            return redirect('.') #입력하고 나서, 정보가 남지않게됨. 

    else:
        form =Form()

    return render(request,'write.html', {'form': form })


#글 작성 목록
def articlelist(request):
    article_list=Article.objects.all()
    return render(request,'list.html',{'article_list': article_list})

def viewdetail(request, num=1):
    #article_detail = Article.objects.get(pk=num)
    article_detail = get_object_or_404(Article,pk=num)
    #pass #나중에 구현하려면 이렇게
    return render(request, 'view_detail.html',{'article_detail':article_detail})