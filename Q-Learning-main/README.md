# Q-LEARNING İLE YOL PLANLAMASI 

## Giriş
Çalışmada belirlenen amaç,bir uygulama gerçekleştirimi ile beraber Q-Learning kullanılarak engellerden ve ödüllerden oluşan karesel bir alanda bir robotun giriş yaptığı ve makine öğrenmesi ile optimal yolu belirleyip çıkışa ulaşmasını sağlayan uygulama gerçeklenmesidir.Python yazılım dili kullanılmıştır.Kodun yazılacağı platform da belirlendikten sonra da gerekli algoritmalar oluşturularak robotun Q-Learning mantığı kullanarak öncelikle engellerden kaçması sağlanıp reward değerleri ve olası aksiyonlara göre bir optimal yolu belirlenmiştir. Son olarak bir arayüzle birlikte robotun giriş yaptığı ve çıkışa ulaştığı bir uygulama gerçeklenmiştir.

## Yöntem
Kodun yazılacağı platform belirlendikten sonra gerekli algoritmalar oluşturularak robotun Q-Learning mantığını kullanarak öncelikle engellerden geçmesi sağlanıp optimal yolu 
belirlenmiştir.

![image](https://user-images.githubusercontent.com/73740709/125152233-e9718c00-e153-11eb-9fcc-d04c5a676130.png)

Örneğin yukarıda verilen environment yapısına bakacak olursak elde edilecek birden çok yol bulunmaktadır.Robotun başlangıç ve bitiş durumları L1 ve L4 olsun. Robotun engellere 
değmeden bulacağı optimal yollar kümesi: {L1,L2,L5,L7,L4},{L1,L2,L5,8,L4}, ... {L1,L5,L7,L4} şeklindedir. Fakat gidilecek random yollardan çok reward tablosuna göre en verimli olan yol başka bir deyimle optimal yol bulunur.

Q-Learning algoritması için birden çok formül yapısı bulunmaktadır. Fakat projede kullanılan formül yapısı da şu şekildedir:

![image](https://user-images.githubusercontent.com/73740709/125152257-1b82ee00-e154-11eb-94f0-44f8d011ea17.png)

Geliştirilen arayüzle birlikte de 50x50 karesel alan içinde farklı renkler kullanılarak başlangıç ve bitiş oluşturulan ekrandan seçilerek engeller ise random olarak belirlenip optimal yolu bulan uygulama oluşturulmuştur. Bir dosya da bulunan engelleri txt dosyasına bastırmaktadır.

## Yalancı Kod ve Kodun Çalışma Prensibi
- Program IDE içinde çalıştırıldı.
- Başlangıç ve Çıkış noktalarını girmek için arayüz ekrana geldi.

![Giriş](https://user-images.githubusercontent.com/73740709/125152349-afed5080-e154-11eb-96cc-594911c6c01a.png)

- Robotun hareket etmesi istenen başlangıç noktası, sayı olarak girildi.
- Robotun hareket etmesi istenen çıkış noktası, sayı olarak girildi.
- ENTER tuşuna basıldı.
- Robot yolları rastgele şekilde öğrenip dolaşarak öğrenmeye başladı.
- Robot yolları öğrendikten sonra oluşturulan pygame arayüzü ekrana çıktı.
- Çıkan pygame arayüzünde robotun her adımı yani robotun optimal yolu beyaz renkle sırasıyla gösterilerek çıkışa ulaşıldı.

![Adsız](https://user-images.githubusercontent.com/73740709/125152401-fe9aea80-e154-11eb-92d6-c1a4451f7cc8.png)

- Çevre baz alınarak bir reward table oluşturulur.

![Figure](https://user-images.githubusercontent.com/73740709/125152556-e081ba00-e155-11eb-8265-1e37e1d69dc7.png)

- Bir dosya da bulunan engelleri txt dosyasına bastırmaktadır.


