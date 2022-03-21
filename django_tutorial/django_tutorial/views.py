from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .froms import CreateUserForm

class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = "registration/register.html"
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된후에
    # 이동할 URL을 지정.

    success_url = reverse_lazy("register_done")

class UserCreateDoneTV(TemplateView):
    template_name = "registration/register_done.html"

