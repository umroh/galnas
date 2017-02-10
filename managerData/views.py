from django.shortcuts import render
from .models import *
# Create your views here.


def beranda_data(request):
    karya = Koleksi.objects.all()
    data = {'koleksi': karya}
    return render(request, "beranda-data.html", data)

def view_koleksi(request):
    karya = Koleksi.objects.all()
    data = {'koleksi': karya}
    return render(request, "daftar_koleksi.html", data)

def view_pegawai(request):
    pegawai = Pegawai.objects.all()
    data = {'pegawai': pegawai}
    return render(request, "daftar_pegawai.html", data)

def view_instansi(request):
    instansi = Instansi.objects.all()
    data = {'instansi': instansi}
    return render(request, "daftar_instansi.html", data)

def view_status_karya(request):
    status_karya = Status_Karya.objects.all()
    data = {'status_karya': status_karya}
    return render(request, "daftar_status_karya.html", data)

def view_kondisi_karya(request):
    kondisi_karya = Kondisi_Karya.objects.all()
    data = {'kondisi_karya': kondisi_karya}
    return render(request, "daftar_kondisi_karya.html", data)

def view_kategori_karya(request):
    kategori_karya = Kategori_Karya.objects.all()
    data = {'kategori_karya': kategori_karya}
    return render(request, "daftar_kategori_karya.html", data)

def view_cara_perolehan(request):
    cara_perolehan = Cara_Perolehan.objects.all()
    data = {'cara_perolehan': cara_perolehan}
    return render(request, "daftar_cara_perolehan.html", data)

def view_lokasi_penyimpanan(request):
    lokasi_penyimpanan = Lokasi_Penyimpanan.objects.all()
    data = {'lokasi_penyimpanan': lokasi_penyimpanan}
    return render(request, "daftar_lokasi_penyimpanan.html", data)

def view_seniman(request):
    seniman = Seniman.objects.all()
    data = {'seniman': seniman}
    return render(request, "daftar_seniman.html", data)
