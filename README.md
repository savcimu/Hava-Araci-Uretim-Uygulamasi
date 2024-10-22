# Hava-Araci-Uretim-Uygulamasi

Bu proje, İHA parçalarının üretimini ve montajını yönetmeyi amaçlayan bir Django tabanlı uygulamadır. Aynı zamanda Django Rest Framework (DRF) ile API desteği sunar.

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [API Belgeleri](#api-belgeleri)
- [Ekran Görüntüleri](#ekran-görüntüleri)
- [Veritabanı Şeması](#veritabanı-şeması)

## Proje Hakkında

Bu proje, İnsansız Hava Aracı (İHA) üretim sürecinin etkin ve düzenli bir şekilde yönetilmesini sağlayan bir sistemdir. Proje, İHA parçalarının üretiminden montaj aşamasına kadar olan tüm süreçlerin dijital olarak izlenebilmesini ve yönetilebilmesini hedefler. Django tabanlı geliştirilen bu uygulama, farklı takımların sorumlu olduğu parça üretim sürecini yönetir ve üretilen parçaların uçak montajında kullanılmasını sağlar.

Sistem, üretim ve montaj aşamalarında eksik parça uyarıları vererek sürecin hatasız ilerlemesine yardımcı olur. Her parça, hangi takım tarafından üretildiği, hangi uçak için üretildiği ve hangi personel tarafından üretildiği gibi bilgilerle kaydedilir. Bu sayede her aşamada şeffaf bir izlenebilirlik sağlanır.

Montaj ekibi, gerekli tüm parçalar tamamlandığında bu parçaları bir araya getirerek uçakları oluşturur. Üretilen uçaklar, kullanılan parçalar, montajda görev alan personel ve üretim tarihleri gibi bilgilerle kaydedilir. Böylece hem parça hem de montaj süreçleri detaylı bir şekilde takip edilebilir.

Projede Django Rest Framework (DRF) kullanılarak, API desteği sunulmuş ve tüm bu süreçlerin dış sistemlerle de entegre edilebilmesi sağlanmıştır. Swagger arayüzü sayesinde bu API'lar kolayca test edilebilir ve belgelenebilir.

- Bu projedeki ana işlevler:
    - Farklı takımların üretim sürecini yönetme
    - Parça bazlı eksik parça takip ve uyarı sistemi
    - Montaj ekibinin uçak üretimini yönetmesi
    - Üretilen uçakların detaylı listesi ve üretim sürecine dair bilgiler
    - Geri dönüşüm ve parça yönetimi
    - API desteği ve dış sistemlerle entegrasyon

## Özellikler
- Parça üretimi (takım bazlı)
  - Farklı takımların (örneğin, kanat, gövde, kuyruk, aviyonik vb.) sorumlu olduğu parçaların üretimi ve yönetimi.
  - Parçaların uçak tipine göre üretimi ve takip edilmesi.
  - Parçaların stokta olması veya eksik olup olmadığına dair uyarı sistemi.

- Uçak montaj işlemi
 - Montaj ekibi, üretilen parçaları kullanarak yeni uçaklar oluşturabilir.
 - Montaj sırasında eksik parçalar için uyarı mesajları.
 - Üretilen uçaklar hakkında detaylı bilgi (kullanılan parçalar, üreten personel, üretim tarihi).

- Üretilen uçakların listesi ve detayları
 - Montaj işlemi tamamlanan uçakların listesi ve her uçak için kullanılan parçaların detaylı listesi.
 - Her uçak için montajda kullanılan parçaların üreten personel ve üretim tarihine göre takibi.
 - Üretilen uçaklar için geri dönük analiz yapabilme ve uçakların hangi takımlar tarafından tamamlandığını görüntüleyebilme.

- Eksik parça uyarıları
 - Montaj işlemi sırasında eksik olan parçaların sistemde gösterilmesi ve uyarı mesajları.
 - Eksik parçaların hangi takımlardan üretileceğinin gösterilmesi.
 - Admin paneli ve montaj ekibi için ayrı ayrı eksik parça uyarı sistemi.

- Django Rest Framework ile API desteği
 - Sistem, API aracılığıyla parçaların, uçakların, personellerin ve takımların yönetilmesine olanak tanır.
 - API üzerinden parça üretimi, montaj işlemleri ve uçakların listelenmesi gibi operasyonlar gerçekleştirilebilir.
 - API çağrıları ile uçak montajı sırasında eksik parça bilgisine erişilebilir.

- Swagger arayüzü ile API dokümantasyonu
 - API'ların Swagger arayüzü üzerinde kolayca test edilmesi ve dokümantasyona erişim imkanı.
 - API endpoint'leri, istek ve yanıt formatları gibi detayların Swagger arayüzü üzerinden incelenmesi.
 - Hangi endpoint'lerin kullanılabileceği ve her endpoint'in döndüğü verilerin detaylı gösterimi.

- Geri Dönüşüm İşlemleri
 - Üretilen ve montajda kullanılmayan parçaların geri dönüşüme gönderilmesi işlemleri.
 - Geri dönüşüm işlemi sonrası stok durumunun güncellenmesi ve ilgili parça bilgisine erişim.

- Kullanıcı Yetkilendirme ve Doğrulama
 - Kullanıcılar yetkilerine göre farklı işlemler yapabilir (admin, montaj ekibi, parça üretim ekibi vb.).
 - Adminler, sistemdeki tüm kullanıcıları yönetebilir, yetkilerini belirleyebilir ve hangi takıma ait olduklarını düzenleyebilir.
 - Kullanıcı giriş ve doğrulama işlemleri, personel bazlı olarak yapılır.


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
- **Uçak**: Admin uçak ekler
- **Takım**: Admin takım ekler
- **Üretilen Uçak**: Montaj işlemi tamamlandıktan sonra uçaklar bu tabloda saklanır ve hangi parçaların kullanıldığı bilgisi tutulur.
