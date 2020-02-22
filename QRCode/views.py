from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from utils.qr_code import gen_qrcode


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        qr_path = gen_qrcode(data)
        return HttpResponse(qr_path)
