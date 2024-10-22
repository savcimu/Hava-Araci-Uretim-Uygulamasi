from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .models import Parca, Ucak, UretilenUcak, Personel, Takim
from .api.serializers import ParcaSerializer, UcakSerializer, UretilenUcakSerializer, PersonelSerializer, TakimSerializer

class ParcaViewSet(viewsets.ModelViewSet):
    queryset = Parca.objects.all()
    serializer_class = ParcaSerializer

class UcakViewSet(viewsets.ModelViewSet):
    queryset = Ucak.objects.all()
    serializer_class = UcakSerializer

class UretilenUcakViewSet(viewsets.ModelViewSet):
    queryset = UretilenUcak.objects.all()
    serializer_class = UretilenUcakSerializer

class PersonelViewSet(viewsets.ModelViewSet):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer

class TakimViewSet(viewsets.ModelViewSet):
    queryset = Takim.objects.all()
    serializer_class = TakimSerializer
    
def personel_giris(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            personel = Personel.objects.get(user=username, sifre=password)
            request.session['personel_id'] = personel.id
            request.session['personel_name'] = personel.user
            request.session['personel_takim_id'] = personel.takim.id
            request.session['personel_takim'] = personel.takim.takim_tipi
            request.session['personel_giris'] = True
            return redirect('index')
        except Personel.DoesNotExist:
            messages.error(request, "Kullanıcı adı veya şifre hatalı")
    
    return render(request, 'login.html')

@login_required
def personel_cikis(request):
    try:
        del request.session['personel_id']
        del request.session['personel_name']
        del request.session['personel_takim_id']
        del request.session['personel_takim']
        del request.session['personel_giris']
    except KeyError:
        pass
    return redirect('login') 

def personel_liste(request):
    personeller = Personel.objects.all()
    return render(request, 'personel_liste.html', {'personeller': personeller})

def parca_uret(request):
    personel_id = request.session.get('personel_id')
    if not personel_id:
        return redirect('login')

    takim_id = request.session.get('personel_takim_id')
    personel_takim = Takim.objects.get(id=takim_id)

    if request.method == 'POST':
        parca_tipi = request.POST['parca_tipi']
        ucak_id = request.POST['ucak']
        ucak = Ucak.objects.get(id=ucak_id)

        yeni_parca = Parca.objects.create(
            ucak=ucak,
            parca_tipi=parca_tipi,
            ureten_personel=Personel.objects.get(id=personel_id)
        )

        messages.success(request, f"{parca_tipi} parçası başarıyla üretildi.")
        return redirect('index')

    ucaklar = Ucak.objects.all()
    return render(request, 'parca_uret.html', {
        'ucaklar': ucaklar,
        'uygun_parca_tipi': personel_takim.takim_tipi
    })

def parca_sil(request, parca_id):
    parca = get_object_or_404(Parca, id=parca_id)
    
    if request.method == 'POST':
        parca.delete()
        messages.success(request, f"{parca.parca_tipi} parçası başarıyla geri dönüşüme gönderildi.")
        return redirect('index')

    return render(request, 'parca_sil.html', {'parca': parca})

def index(request):
    personel_id = request.session.get('personel_id')
    if not personel_id:
        return redirect('login')

    takim_id = request.session.get('personel_takim_id')
    personel_takim = Takim.objects.get(id=takim_id)

    ucaklar = Ucak.objects.all()

    parcalar = Parca.objects.filter(parca_tipi=personel_takim.takim_tipi, kullanilan_ucak__isnull=True)

    uretilen_ucaklar = UretilenUcak.objects.all() if personel_takim.takim_tipi == 'MONTAJ' else None

    return render(request, 'index.html', {
        'ucaklar': ucaklar,
        'parcalar': parcalar,
        'uretilen_ucaklar': uretilen_ucaklar,
        'personel': Personel.objects.get(id=personel_id)
    })

def ucak_montaj(request):
    if request.method == 'POST':
        ucak_id = request.POST['ucak']
        ucak = Ucak.objects.get(id=ucak_id)

        gerekli_parcalar = ['KANAT', 'GOVDE', 'KUYRUK', 'AVIYONIK']
        eksik_parcalar = []

        for parca_tipi in gerekli_parcalar:
            parca = Parca.objects.filter(ucak=ucak, parca_tipi=parca_tipi, kullanilan_ucak__isnull=True).first()
            if not parca:
                eksik_parcalar.append(parca_tipi)

        if eksik_parcalar:
            eksik_parcalar_str = ', '.join(eksik_parcalar)
            messages.error(request, f"{ucak.ad} için eksik parçalar var: {eksik_parcalar_str}")
            return redirect('ucak_montaj')

        uretilen_ucak = UretilenUcak.objects.create(ucak_tipi=ucak)
        for parca_tipi in gerekli_parcalar:
            parca = Parca.objects.filter(ucak=ucak, parca_tipi=parca_tipi, kullanilan_ucak__isnull=True).first()
            parca.kullanilan_ucak = ucak
            parca.save()
            uretilen_ucak.kullanilan_parcalar.add(parca)

        uretilen_ucak.save()
        messages.success(request, f"{ucak.ad} başarıyla üretildi ve montaj tamamlandı.")
        return redirect('ucak_liste')

    ucaklar = Ucak.objects.all()
    return render(request, 'ucak_montaj.html', {'ucaklar': ucaklar})

def uretilen_ucaklar_liste(request):
    uretilen_ucaklar = UretilenUcak.objects.all()
    return render(request, 'uretilen_ucaklar_liste.html', {'uretilen_ucaklar': uretilen_ucaklar})

def ucak_montaj(request):
    if request.method == 'POST':
        ucak_id = request.POST['ucak']
        ucak = Ucak.objects.get(id=ucak_id)
        personel_id = request.session.get('personel_id')
        personel = Personel.objects.get(id=personel_id)

        gerekli_parcalar = ['KANAT', 'GOVDE', 'KUYRUK', 'AVIYONIK']
        eksik_parcalar = []

        for parca_tipi in gerekli_parcalar:
            parca = Parca.objects.filter(ucak=ucak, parca_tipi=parca_tipi, kullanilan_ucak__isnull=True).first()
            if not parca:
                eksik_parcalar.append(parca_tipi)

        if eksik_parcalar:
            eksik_parcalar_str = ', '.join(eksik_parcalar)
            messages.error(request, f"{ucak.ad} için eksik parçalar var: {eksik_parcalar_str}")
            return redirect('ucak_montaj')

        uretilen_ucak = UretilenUcak.objects.create(ucak_tipi=ucak, ureten_personel=personel)
        for parca_tipi in gerekli_parcalar:
            parca = Parca.objects.filter(ucak=ucak, parca_tipi=parca_tipi, kullanilan_ucak__isnull=True).first()
            parca.kullanilan_ucak = ucak
            parca.save()
            uretilen_ucak.kullanilan_parcalar.add(parca)

        uretilen_ucak.save()
        messages.success(request, f"{ucak.ad} başarıyla üretildi ve montaj tamamlandı.")
        return redirect('index')

    ucaklar = Ucak.objects.all()
    return render(request, 'ucak_montaj.html', {'ucaklar': ucaklar})
