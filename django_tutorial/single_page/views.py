from django.shortcuts import render
from community.models import Article

# Create your views here.
def index(request):
    lastest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'single_page/index.html',{'lastest_article_list':lastest_article_list})
    #return render(request, '/index.html', {'latest_article_list': latest_article_list})

def aboutMe(request):
    # return rander(request,'템플릿파일',{'키':데이터_변수} )
    return render(request,'single_page/aboutme.html',)