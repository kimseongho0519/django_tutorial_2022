from multiprocessing import reduction
from django.shortcuts import redirect, render
from .models import CountryData
from .forms import CountryDataForm
# Create your views here.
# 함수 안에는 request 
def dashboard(request):
    #각 나라와 인구숫자 가져오기
    data = CountryData.objects.all()
    # add 버튼 클릭 , 값 입력 요청 처리
    if request.method =='POST':
    # DB입력
        form = CountryDataForm(request.POST)
        #폼에 입력한 나라
        input_country = form.data.get('country', None)
        #폼에 입력한 인구수
        input_num = form.data.get('population', None)
        if form.is_valid():
            # DB 나라이름이 중복된 경우 업데이트
            # 아닌경우, 추가
            #CRUD : create , Read , Update , Delate
            CountryData.objects.update_or_create(
                #filter
                country = input_country,
                #new value
                defaults = {
                    'country': input_country,
                    'population': input_num
                }
            )

            #form.save()
            return redirect('.')
    #form 출력 
    else:
        #form 객체 생성
        form = CountryDataForm()
    

    #변수처리, db데이터 가져오기
    #데이터 필터링, form처리
    #aaa="대시보드 만들기"
    #form = CountryDataForm()
    context = {'dataset': data, 'form': form }
    return render(request, 
    'dashboard/dashboard.html', context)
    # return render(request, '랜더링할 템플릿파일',{템플릿에 전달할 데이터 키: 데이터 변수} )


    # class CountryData(models.Model):
    # country = models.CharField(max_length=100)
    # population = models.IntegerField()