from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

def foto_file_path(instance, filename):

    try:
        temp = filename.split('.')
        ext = '.' +  temp[len(temp) - 1]
    except:
        ext = '.jpg'

    now = datetime.datetime.now()
    return 'Data/Foto_Koleksi/{0}/{1}'.format(instance.id_seniman, str(instance.no_urut_koleksi_seniman) + ext)

class Pegawai(models.Model):
    nama = models.CharField(max_length=200)
    userId = models.ForeignKey(User)
    jabatan = models.CharField(max_length=200)
    def __str__(self):
        return '%s | %s' % (self.nama, self.jabatan)

class Instansi(models.Model):
    kode_instansi = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.kode_instansi)

class Status_Karya(models.Model):
    deskripsi_status = models.CharField(max_length=100)
    def __str__(self):
        return '%s' % (self.deskripsi_status)

class Kondisi_Karya(models.Model):
    deskripsi_kondisi = models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.deskripsi_kondisi)

class Kategori_Karya(models.Model):
    kategori = models.CharField(max_length=100)
    def __str__(self):
        return '%s ' % (self.kategori)

class Cara_Perolehan(models.Model):
    deskripsi_perolehan = models.CharField(max_length=200)
    def __str__(self):
        return '%s ' % (self.deskripsi_perolehan)

class Lokasi_Penyimpanan(models.Model):
    nama_ruangan = models.CharField(max_length=100)
    jenis_rak = models.CharField(max_length=50)
    no_urut_rak = models.CharField(max_length=50)
    no_urut_karya_rak = models.CharField(max_length=50)
    def __str__(self):
        return '%s / %s / %s / %s' % (self.nama_ruangan,self.jenis_rak,self.no_urut_rak,self.no_urut_karya_rak)

class Seniman(models.Model):
    nama = models.CharField(max_length=100)
    biografi = models.TextField()
    tahun_lahir = models.DateField(null=True)
    tahun_meninggal = models.DateField(null=True)
    narahubung = models.CharField(max_length=500,null=True)
    alamat = models.TextField()
    def __str__(self):
        return '%s' % (self.nama)

class Koleksi(models.Model):
    no_inventaris = models.CharField(max_length=50)
    id_instansi = models.ForeignKey(Instansi, related_name='id_instansi')
    no_urut_koleksi_seniman = models.IntegerField()
    id_seniman = models.ForeignKey(Seniman)
    judul_karya = models.CharField(max_length=1000)
    deskripsi_karya = models.TextField()
    tahun_pembuatan = models.IntegerField()
    foto = models.FileField(upload_to=foto_file_path)
    nomor_slide_negatif = models.CharField(max_length=200)
    media = models.TextField()
    ukuran = models.TextField()
    harga = models.IntegerField()
    kondisi = models.ForeignKey(Kondisi_Karya)
    lokasi_penyimpanan = models.ForeignKey(Lokasi_Penyimpanan)
    status_karya = models.ForeignKey(Status_Karya)
    kategori_karya = models.ForeignKey(Kategori_Karya)
    kurator = models.ForeignKey(User,related_name='kurator')
    input_by = models.ForeignKey(User, related_name='input_by')
    waktu_edit_terakhir = models.DateTimeField()
    input_time = models.DateTimeField()
    diedit_oleh = models.ForeignKey(User, related_name='diedit_oleh')
    cara_perolehan = models.ForeignKey(Cara_Perolehan)
    tahun_perolehan = models.IntegerField()
    diperoleh_dari = models.ForeignKey(Instansi, related_name='diperoleh_dari')
    tanda_tangan_seniman = models.BooleanField(default=False)
    nomor_perolehan = models.IntegerField()
    no_urut_koleksi = models.IntegerField()
    no_registrasi = models.CharField(max_length=100)

    def __str__(self):
        return '%s | %s ' % (self.id_seniman,self.judul_karya)