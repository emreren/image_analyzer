## Görüntü Analiz Uygulaması
Image Analyzer, yüklenen görüntü dosyalarındaki hassas verileri (örneğin telefon numaraları, kredi kartı numaraları, tarihler vb.) tespit eden bir FastAPI uygulamasıdır.

### Başlangıç

Bu talimatlar, projenin yerel makinenizde nasıl çalıştırılacağı veya dağıtılacağı hakkında size rehberlik edecektir. Geliştirme ve test amacıyla bu adımları takip edebilirsiniz.

### Önkoşullar

Projenin çalışması için aşağıdaki yazılımların yüklü olması gerekmektedir:

- Docker
- Docker Compose
- Python 3.11

### Kurulum

1. Proje klasörüne gidin:

```bash
cd image_analyzer
```

2. Docker Compose ile projeyi başlatın:

```bash
docker-compose up -d
```
Bu komut, iki farklı container'ı uyandıracaktır.

### Analyze Endpointi Kullanımı

Image Analyzer uygulaması, `POST /analyze/` endpointi aracılığıyla görüntü dosyalarının analizini yapmanıza olanak tanır. İşte adım adım nasıl kullanılacağına dair talimatlar:

1. Tarayıcınızı açın ve `http://localhost:8000/docs` adresine gidin. Bu adres, Swagger arayüzünü sağlar.

2. Swagger arayüzünde, "Analyze an Image" bölümünde yer alan `POST /analyze/` endpointini bulun.

3. Endpointin altında yer alan "Try it out!" düğmesine tıklayın.

4. **file** parametresini seçerek bir görüntü dosyası yükleyin. Dosya türü olarak desteklenen görüntü formatlarından birini seçtiğinizden emin olun.

5. "Execute" düğmesine tıklayarak analiz işlemini başlatın.

6. Uygulama, yüklenen görüntü dosyasını analiz edecek ve içerisinde bulunan hassas verileri tespit edecektir.

7. Sonuçlar, "Response body" bölümünde gösterilecektir. İçerikte, analiz edilen veri, analiz durumu ("status") ve bulunan hassas verilerin listesi ("findings") yer alır.

8. Eğer yüklenen dosyanın içeriği Redis önbelleğinde zaten bulunuyorsa, uygulama sonuçları önbellekten getirir ve "Image analysis completed. Returning cached result." şeklinde bir mesajla bildirir.

Böylece, Image Analyzer uygulamasının analyze endpointini kullanarak görüntü dosyalarının içerisindeki hassas verileri tespit edebilirsiniz.


### Katkıda Bulunma

Katkıda bulunmak için bu depoyu forklayın, değişikliklerinizi yapın ve bir pull isteği gönderin.
