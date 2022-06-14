# digikep_masodik_kicsi

### A feladat leírása
Detektálja a fehér virágszirmokat a hk_flower.jpg bemeneti képen. Hasonlítsa össze az előzetesen készült képpel.

### Fejlesztői dokumentáció
A program először betölti a feldolgozandó képet, valamint az elvárt eredmény képet (hk_flower_szirom.png). Ezt követően a feldolgozandó képet csatornokra bontjuk, majd a vörös, kék, zöld csatornákon egyenként küszöbölünk. A küszöböléssel előállított csatornákból egy maszkot hozunk létre. Az előállított maszk és az elvárt eredmény abszolút különbség képet megjelenítjük, valamint az L1 norma értékét meghatározzuk. Végül maszkoljuk az eredeti csatornákat, így előáll a végeredmény, amit res_segm.png néven mentünk.

### Elért eredmények

- a feldolgozandó kép:

![image](https://user-images.githubusercontent.com/71877876/173564016-2dd4912f-1c8d-4f24-9386-6892e1d4f7de.png)

- az elvárt maszk:

![image](https://user-images.githubusercontent.com/71877876/173564440-4cc5efeb-c2f1-462e-9171-8314dc57ebec.png)


- az általam létrehozott maszk:

![image](https://user-images.githubusercontent.com/71877876/173564405-d627dff3-4b6c-4d1e-9e29-7b3ccf450906.png)


- a kettő különbsége:

![image](https://user-images.githubusercontent.com/71877876/173564173-2abf0f61-b140-421b-a99c-1453eeccd184.png)

- az eredmény:

![image](https://user-images.githubusercontent.com/71877876/173564040-9b9f14b3-0dec-409e-9d08-18fabf9869a9.png)
