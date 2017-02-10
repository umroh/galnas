from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.beranda_data, name='beranda-data'),

    #------------------View Only -----------------------------------#
    url(r'^daftar-lokasi-penyimpanan/$', views.view_lokasi_penyimpanan, name='daftar-lokasi-penyimpanan'),
    url(r'^daftar-cara-perolehan/$', views.view_cara_perolehan, name='daftar-cara-perolehan'),
    url(r'^daftar-instansi/$', views.view_instansi, name='daftar-instansi'),
    url(r'^daftar-kategori-karya/$', views.view_kategori_karya, name='daftar-kategori-karya'),
    url(r'daftar-koleksi/$', views.view_koleksi, name='daftar-koleksi'),
    url(r'^daftar-kondisi-karya/$', views.view_kondisi_karya, name='daftar-kondisi-karya'),
    url(r'^daftar-pegawai/$', views.view_pegawai, name='daftar-pegawai'),
    url(r'^daftar-seniman/$', views.view_seniman, name='daftar-seniman'),
    url(r'^daftar-status-karya/$', views.view_status_karya, name='daftar-status-karya'),


]