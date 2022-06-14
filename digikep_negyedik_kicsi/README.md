# digikep_negyedik_kicsi

### A feladat leírása
Készítsen egy programot Python-ban az OpenCV és Numpy Python csomagok felhasználásával, ami egy bemeneti színes kép esetén egy megadott HSV intervallumban előforduló színeket megtartja, a kívül esőket pedig a szürkeárnyalatos megfelelőjükkel helyettesíti! A program bemenete: egy kép, amelynek a neve PalPant_800.jpg

### Fejlesztői dokumentáció
A program először betölti a feldolgozandó képet (PalPant_800.jpg), majd gauss szűrés következik:

- gauss kernel mérete: (3,3),
- a szórás Y és X irányba is 2.0.

Ezt követően BGR-ből átváltunk HSV színtérbe, ahol szegmentálunk egy bizonyos színtartományt. A szegmentált tartányt összefűzzük az eredeti képpel, így a következő eredményt kapjuk:

![image](https://user-images.githubusercontent.com/71877876/173565199-f3863aa5-0106-4869-b5a9-7b43e58b3344.png)

Ezt követően az invertált maszkot vonjuk össze az eredeti szürkeárnyalatos képpel. Melynek eredménye:

![image](https://user-images.githubusercontent.com/71877876/173565228-8af6ac07-c6a9-457c-ba10-8b020c3bc027.png)

A kettő képet mergeljük, így kapjuk a lent látható eredményt.


### Elért eredmények

- a feldolgozandó kép:

![image](https://user-images.githubusercontent.com/71877876/173565257-928975ce-9d10-4eea-b360-c14a2178079b.png)

- az eredmény:

![image](https://user-images.githubusercontent.com/71877876/173565281-edcc6204-0db0-4361-81b3-0513366c4120.png)
