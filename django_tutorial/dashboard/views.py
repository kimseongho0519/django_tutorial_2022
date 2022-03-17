from django.shortcuts import render
from .models import CountryData
# Create your views here.
# 함수 안에는 request 
def dashboard(request):
    #각 나라와 인구숫자 가져오기
    data = CountryData.objects.all()
    #print(data)

    #변수처리, db데이터 가져오기
    #데이터 필터링, form처리
    #aaa="대시보드 만들기"
    return render(request, 
    'dashboard/dashboard.html',{'dataset': data} )
    # return render(request, '랜더링할 템플릿파일',{템플릿에 전달할 데이터 키: 데이터 변수} )


    # class CountryData(models.Model):
    # country = models.CharField(max_length=100)
    # population = models.IntegerField()