# digikep_nagybeadando

### A feladat leírása
A feladat a crosswalk.jpg képen található zebra csíkjainak szegmentálása illetve kiszínezése. A program jelenítsen meg egy vagy több részeredmény képet. Egy lehetséges eredményt mutat a crosswalk_marked.jpg kép.
- elvárt eredmény:

![image](https://user-images.githubusercontent.com/71877876/173533877-b25724a0-4905-4900-a792-c944f6b33a25.png)
![image](https://user-images.githubusercontent.com/71877876/173533893-1d4c2e2c-cb7c-4225-9bc7-b95daf5348c5.png)

### Felhasználói dokumentáció
A felhasználót a program indításakor a crosswalk.jpg fogadja. A továbbiakban lehetősége van az 1-5 tartományba eső billentyűk lenyomásával a megjelenő képet módosítani. Ekkor már nem csak az eredeti kép, hanem az eredmény is megjelenik. Amennyiben a program használója a terminált is nézi, láthatja, hogy milyen intervallumon történt a szegmentálás, valamint mekkora az kontúrterület alsó küszöbértéke. A programból kilépni az ESC vagy a q billentyők lenyomásával lehetséges.

### Fejlesztői dokumentáció

A program kezdetben beégetett értékek alapján indul, ezen változók az
- src: feldolgozandó kép
- num: kontúrterület alsó küszöbértéke
- interval_H, interval_S, interval_V: HSV színtérben történő szegmentáláshoz a színterek intervallumai

Ezen változók minden esetben felülírodnak, amikor a feldolgozandó képet lecseréljük. Ezt a numerikus billentyűzeten, illetve a finkcionális billentyűzeten is megtehetjük az 1-5 intervallumon szereplő számok segítségével. Amikor egy ilyen billentyűt lenyomunk a változók inicializálása után a main függvényt hívjuk meg

A main függvény fontosabb lépései:
- bilaterális zajszűrés,
- egy külső függvény (hsv_segment) segítségével megtörténik HSV színtéren a szegmentálás,
- kontúrkesesés,
- kontúrokból konvex alakzatok képzése,
- színezés, ahol a kontúrterület nagyobb az alsó küszöbnél,
- az eredmény vizualizálása.

Az ESC és a q billentyűkkel megszakítható a program futása.

### Elért eredmények
- crosswalk.jpg

![image](https://user-images.githubusercontent.com/71877876/173539257-7adaa2e4-3d53-44da-a0eb-e09812ba1d07.png)
![image](https://user-images.githubusercontent.com/71877876/173539347-bcb3e7dc-66db-46b7-bb07-8b7205aab642.png)

- 2.jpg
- 
![image](https://user-images.githubusercontent.com/71877876/173540302-493e48b2-a6fd-4341-a5c6-d41bbb9fa90f.png)
![image](https://user-images.githubusercontent.com/71877876/173539726-2cd62cb4-4cec-4d1a-94e6-ea0f36e50cbf.png)

- 3.jpg

![image](https://user-images.githubusercontent.com/71877876/173540164-ffa84e1b-f4be-40cd-aeca-61de45392796.png)
![image](https://user-images.githubusercontent.com/71877876/173540180-d87d1308-f68f-447a-951f-c005e09f6dd0.png)


- 4.jpg

![image](https://user-images.githubusercontent.com/71877876/173540121-20d6567a-6721-4c74-a260-c5a982cc3acd.png)
![image](https://user-images.githubusercontent.com/71877876/173540134-d48be45a-e88f-4ed8-a55d-ea4147c7437f.png)


- 5.jpg

![image](https://user-images.githubusercontent.com/71877876/173540034-0d2e7470-7044-449a-af17-3a77c784875b.png)
![image](https://user-images.githubusercontent.com/71877876/173540077-b4933623-962f-4790-afa0-54ff38ec9f03.png)

