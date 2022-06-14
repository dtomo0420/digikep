# digikep_harmadik_kicsi

### A feladat leírása
Készítsen egy, a zajszűrésen és éldetektáláson alapuló „rajzfilmesítő” programot Python-ban az OpenCV és Numpy Python csomagok felhasználásával. A program bemenete: egy kép, amelynek a neve input.jpg (tetszőleges kép lehet, amelynek a mérete nem nagyobb, mint 1MB).

### Fejlesztői dokumentáció
A program három különböző paraméterezéssel hívja meg a feladat függvényt.

A feladat függvény paraméterei:
- img: a feldolgozandó kép,
- ca, cb: az mártix méretét határozza meg,
- candy: nyílásméret a Sobel operátor számára,
- also: also küszöb a hiszterézis küszöböléshez,
- felso: felső küszöb a hiszterézis küszöböléshez.

A feladat függvény:
- medián szűrés,
- canny éldetektor,
- élek vastagítása,
- morfológiai dilatáció,
- rgb csatornákra bontás,
- rgb élkép invertálása,
- a medián szűrt kép és a negatív élkép összefűzése.

### Elért eredmények

- első lehetőség

![image](https://user-images.githubusercontent.com/71877876/173564848-5f1d332b-cb66-4521-a0fb-ff624b966baa.png)

- második lehetőség

![image](https://user-images.githubusercontent.com/71877876/173564908-9a89d46f-2985-4a3a-a546-bc5bbe614bab.png)

- harmadik lehetőség

![image](https://user-images.githubusercontent.com/71877876/173564943-3afc87ce-8aff-4731-9f6d-3d064e843ec3.png)
