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

![Swagger API](swagger.png)
![API Root](api1.png)
![API Root 2](api2.png)

## Ekran Görüntüleri

### Giriş Sayfası
![Giriş Sayfası](login.png)
![Giriş Sayfası Alternatif](login2.png)

### Parça Üretim Ekranı
![Parça Üretimi](parca_uretim.png)
![Parça Üretimi 2](parca_uretim2.png)

### Parçalar Listesi
![Parçalar Listesi](parcalar.png)

### Montaj Ekranı
![Montaj Ekranı](montaj_giris.png)

### Üretilen Uçakların Detayları
![Üretilen Uçak 1](ucak_uret1.png)
![Üretilen Uçak 2](ucak_uret2.png)
![Üretilen Uçak 3](ucak_uret3.png)
![Üretilen Uçak 4](ucak_uret4.png)
![Üretilen Uçak 5](ucak_uret5.png)

### Parça Geri Dönüşüm
![Parça Geri Dönüşüm](geri_donusum.png)

### Admin Panel - Uçaklar
![Admin Panel - Uçaklar](admin_ucaks.png)

### Admin Panel - Üretilen Uçaklar
![Admin Panel - Üretilen Uçaklar](admin_uretilen_ucaks.png)

### Eksik Parça Uyarısı
![Eksik Parça Uyarısı](eksik_parca.png)

## Veritabanı Şeması

Bu projede kullanılan ilişkisel veritabanı yapısı aşağıdaki gibidir:

![Veritabanı Şeması](er_diagram.png)

Veritabanı ilişkileri:

- **Personel**: Takımlara bağlı olarak parçaları üretir.
- **Parça**: Her parça bir uçağa özeldir ve üreten personel bilgisi ile birlikte kaydedilir.
- **Uçak**: Montajlama işlemi tamamlandığında parçalarla ilişkilendirilir ve üretilmiş olur.
- **Takım**: Takımlar belirli parçalardan sorumludur. Her takım kendi parçasını üretir.
- **Üretilen Uçak**: Montaj işlemi tamamlandıktan sonra uçaklar bu tabloda saklanır ve hangi parçaların kullanıldığı bilgisi tutulur.
