# Hava-Araci-Uretim-Uygulamasi

Bu proje, İHA parçalarının üretimini ve montajını yönetmeyi amaçlayan bir Django tabanlı uygulamadır. Aynı zamanda Django Rest Framework (DRF) ile API desteği sunar.

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [API Belgeleri](#api-belgeleri)
- [Ekran Görüntüleri](#ekran-görüntüleri)
- [Veritabanı Şeması](#veritabanı-şeması)

## Proje Hakkında

İHA üretim sürecinde montaj, parça üretimi ve yönetimi gibi süreçlerin yürütülmesine olanak sağlayan bir sistemdir. Kullanıcılar, takımlarına göre parça üretimi gerçekleştirebilir, montaj ekibi ise üretilen parçaları birleştirerek uçak üretebilir.

## Özellikler
- Parça üretimi (takım bazlı)
- Uçak montaj işlemi
- Üretilen uçakların listesi ve detayları
- Eksik parça uyarıları
- Django Rest Framework ile API desteği
- Swagger arayüzü ile API dokümantasyonu

## API Belgeleri

Django Rest Framework ile oluşturulan API endpoint'lerine aşağıdaki linkten ulaşabilirsiniz:

- [Swagger API Belgeleri](http://127.0.0.1:8000/swagger/)

Projede aşağıdaki API'ler bulunmaktadır:
- Parçalar API'si: `http://127.0.0.1:8000/api/parcalar/`
- Uçaklar API'si: `http://127.0.0.1:8000/api/ucaklar/`
- Üretilen Uçaklar API'si: `http://127.0.0.1:8000/api/uretilen-ucaklar/`
- Personeller API'si: `http://127.0.0.1:8000/api/personeller/`
- Takımlar API'si: `http://127.0.0.1:8000/api/takimlar/`

![Swagger API](images/swagger.png)
![API Root](images/api1.png)
![API Root 2](images/api2.png)

## Ekran Görüntüleri


### Giriş Sayfası
![Giriş Sayfası](images/login.png)

![Giriş Sayfası Alternatif](images/login2.png)


### Parça Üretim Ekranı
![Parça Üretimi](images/parca_uretim.png)
![Parça Üretimi 2](images/parca_uretim2.png)


### Parçalar Listesi
![Parçalar Listesi](images/parcalar.png)


### Montaj Ekranı
![Montaj Ekranı](images/montaj_giris.png)


### Üretilen Uçakların Detayları
![Üretilen Uçak 1](images/ucak_uret1.png)

![Üretilen Uçak 2](images/ucak_uret2.png)

![Üretilen Uçak 3](images/ucak_uret3.png)

![Üretilen Uçak 4](images/ucak_uret4.png)

![Üretilen Uçak 5](images/ucak_uret5.png)


### Parça Geri Dönüşüm
![Parça Geri Dönüşüm](images/geri_donusum.png)


### Admin Paneli
![Admin Panel 1](images/admin_ucaks.png)

![Admin Panel 2](images/admin_uretilen_ucaks.png)


### Eksik Parça Uyarısı
![Eksik Parça Uyarısı](images/eksik_parca.png)


## Veritabanı Şeması

Bu projede kullanılan ilişkisel veritabanı yapısı aşağıdaki gibidir:

![Veritabanı Şeması](images/er_diagram.png)

Veritabanı ilişkileri:

- **Personel**: Takımlara bağlı olarak parçaları üretir.
- **Parça**: Her parça bir uçağa özeldir ve üreten personel bilgisi ile birlikte kaydedilir.
- **Uçak**: Montajlama işlemi tamamlandığında parçalarla ilişkilendirilir ve üretilmiş olur.
- **Takım**: Takımlar belirli parçalardan sorumludur. Her takım kendi parçasını üretir.
- **Üretilen Uçak**: Montaj işlemi tamamlandıktan sonra uçaklar bu tabloda saklanır ve hangi parçaların kullanıldığı bilgisi tutulur.
