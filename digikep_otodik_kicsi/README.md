# digikep_otodik_kicsi

### A feladat leírása
Készítsen egy programot Python-ban az OpenCV és Numpy Python csomagok felhasználásával, amely az alábbi lépéseket hajtja végre: A car_numberplate_rs.jpg képen hajtson végre olyan szegmentálást, amely kék színű objektumokat adja eredményül (lásd a Küszöbölés és vágás színes képeken részben vagy végezhető színhasonlóságon alapuló szegmentálás is). Ha szükséges, morfológiai műveletekkel javítson a komponensek összefüggőségén! Az eredmény képen szűrje a komponenseket méret és körszerűség alapján, hogy csak a matrica maradjon! Az eredményt jelenítse meg a képernyőn és mentse el külső fájlba output.jpg néven az eredmény képet! 

### Fejlesztői dokumentáció
A program először a feldolgozandó képet beolvassa (car_numberplate_rs.jpg), ezt követően BGR-ből HSV színtérbe váltunk. Ezután szegmentáljuk a kék objektumokat. Ebben a hsv_segment lesz a segítségünkre. A szegmentált és az eredeti képet összefűzzük, majd szürkeárnyalatos színtérre váltunk. Ekkor medián szűrés következik. A körök detektálása után, kört rajzolunk a metrica köré.


### Elért eredmények

- az eredeti kép:

![image](https://user-images.githubusercontent.com/71877876/173562822-22a277d3-ba41-4f91-a5cb-eb3768814539.png)

- az eredmény:

![image](https://user-images.githubusercontent.com/71877876/173562799-0555b4ec-e97b-47eb-9f11-f8a4ca0afacd.png)
