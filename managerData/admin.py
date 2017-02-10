from django.contrib import admin
from models import *

# Register your models here.

admin.site.register(Pegawai)
admin.site.register(Instansi)
admin.site.register(Status_Karya)
admin.site.register(Kondisi_Karya)
admin.site.register(Kategori_Karya)
admin.site.register(Cara_Perolehan)
admin.site.register(Lokasi_Penyimpanan)

class KoleksiAdmin(admin.ModelAdmin):
    search_fields = ('id_seniman__nama', 'judul_karya')
admin.site.register(Koleksi, KoleksiAdmin)


class SenimanAdmin(admin.ModelAdmin):
    search_fields = ('nama', 'alamat')

admin.site.register(Seniman, SenimanAdmin)
