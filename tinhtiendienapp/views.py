from decimal import *

from django.shortcuts import render
from django.utils import timezone

from .models import DinhMuc
from . import functionapp

from .forms import TinhTienDienForm


def index(request):
    # get data from database to transfer to template.
    dinh_muc = DinhMuc.objects.filter(gia_dien_evn__start_date__lte=timezone.now(),
                                      gia_dien_evn__end_date__gte=timezone.now()).order_by('level_no')

    # building context variable to send to template.
    cong_suat = 0.0
    gia_dien = 0.0
    thoi_gian = 0.0

    if 'cong_suat' in request.GET and request.GET['cong_suat'] != '':
        cong_suat = Decimal(request.GET['cong_suat'])

    if 'gia_dien' in request.GET and request.GET['gia_dien'] != '':
        gia_dien = Decimal(request.GET['gia_dien'])

    if 'thoi_gian' in request.GET and request.GET['thoi_gian'] != '':
        thoi_gian = Decimal(request.GET['thoi_gian'])

    number_of_kwh_ngay = cong_suat / 1000 * thoi_gian
    number_of_kwh_tuan = number_of_kwh_ngay * 7
    number_of_kwh_thang = number_of_kwh_ngay * 30

    ket_qua_ngay = functionapp.tinh_tien(dinh_muc,number_of_kwh_ngay, gia_dien)
    ket_qua_tuan = functionapp.tinh_tien(dinh_muc,number_of_kwh_tuan, gia_dien)
    ket_qua_thang = functionapp.tinh_tien(dinh_muc, number_of_kwh_thang, gia_dien)

    # generate the image
    img_name= functionapp.generate_image(cong_suat, gia_dien, thoi_gian, [number_of_kwh_ngay,ket_qua_ngay['thanh_tien']], [number_of_kwh_tuan,ket_qua_tuan['thanh_tien']], [number_of_kwh_thang,ket_qua_thang['thanh_tien']])

    if gia_dien == 0.0:
        ini_gia_dien = ''
    else:
        ini_gia_dien = gia_dien

    if cong_suat != 0.0 or gia_dien != 0 or thoi_gian != 0:
        tinh_tien_dien_form = TinhTienDienForm(initial={'cong_suat': cong_suat, 'gia_dien': ini_gia_dien, 'thoi_gian': thoi_gian})
    else:
        tinh_tien_dien_form = TinhTienDienForm()

    return render(request, 'tinhtiendienapp/index.html', {
        'bang_gia_dien': dinh_muc,
        'ket_qua_ngay': ket_qua_ngay,
        'ket_qua_tuan': ket_qua_tuan,
        'ket_qua_thang': ket_qua_thang,
        'cong_suat': cong_suat,
        'gia_dien': gia_dien,
        'thoi_gian': thoi_gian,
        'img_name': img_name,
        'form' : tinh_tien_dien_form,
    })
