# LKLCTF19
Весь CTF строится вокруг идеи виртуального ограбления банка.  
  
The plan:  
https://docs.google.com/document/d/11c03qD_jrP5roYNqIiKQLulL6gv3regPOWb6lojFBXE/edit#  

List:
1. welcome-web
2. welcome-crypto
3. welcome-admin
4. welcome-ppc
5. welcome-forensics
6. welcome-stego
7. welcome-recon
8. welcome-misc
9. web-ebanking (3 part)
10. web-fussy
11. crypto-xor
12. crypto-rsa
13. crypto-decypher 
14. admin-webcam
15. admin-vm
16. ppc-atm
16. ppc-database
17. ppc-primes
18. ppc-mining
19. ppc-dijkstra
20. for-hijacking
21. for-dump
22. for-vm
22. stego-logo
23. stego-excel
24. stego-ringtone
25. stego-spaces
26. recon-1
27. recon-2
28. recon-3
29. rev-timemachine
30. rev-infiniteloop
31. rev-python
32. rev-android
33. misc-hotline
34. misc-discord
35. misc-vk
---
  
# Categories:
welcome, web, crypto, admin, ppc, forensics, stego, recon, misc

## welcome - 8 на каждую категорию кроме misc


## web - 4
### **ebanking - web**  
Ну это короче онлайн банк у которого хуевые программисты  
Три шага:   
1) простая sql инъекция  
2) xss  
3) взломать 2fa  
  
### **Паучок Фаззи - web**  
Какая удача, на сайте ЛКЛ-Банка появилась вакансия специалиста по безопасности! Необходимо найти уязвимость в веб-странице, подумаешь! Вперед решать, аххаха. и ссылка.  
*Не совсем понял. Ну будет какой-нибудь лендинг, там внизу страницы форма отправки сообщения. нужно сломать парсер email, тогда страница крашится и выдается флаг.Ааааааа. Фаззинг, я думал что раз паучок то crawling. Это тоже можно замутить кстати. Сделать лабиринт из ссылок. И в конце концов будет страница с отправкой обратной связи*


## crypto - 3
### **Таск на криптоанализ xor-а - crypto**  
Бла-бла-бла  
  
### **Таск на rsa (очевидно) - crypto**  
Бла-бла-бла  
  
### **Расшифровка - crypto**
Каждые 30 минут между двумя точками банка начинается трансфер данных, зашифрованных, около 25 сообщений. Вы успешно провели митм. Теперь необходимо вытащить информацию из этого канала. Но данные всегда разные, и чаще там попадается ненужное говно, чем флаг.
При начале транзакции передаются какие-то параметры шифрования.  
Шифрование всегда разное (AES, ECC private, RSA private)  
Затем рецепт каждого зашифрованного сообщения:  
base64(шифрование какое-то(json.dumps(obj)))  
obj = объект перевода денег, флаг в описании к переводу  


## admin - 
### Заклей вебкамеру - admin
получить изображение с вебки сотрудника, упавшей с монитора, которая смотрит прямо на документы (там тупа будет статичное изображение, а то сложно, нам не дадут 24/7 крутить вебку)


## ppc - 4
### atm - ppc
В чем суть: nc доступ к сервису, на котором человек должен на время решить regex кроссворд (https://regexcrossword.com/) (нагло спизжено с квалов inno ctf-а)  
(ну по-моему регэкспы решать на время это смэрть) (ну так ppc же))))  
  
### какая-нибудь автоматизация - ppc
у нас же в банке криворукие программисты? пускай утечет база  
логинов-паролей сотрудников 2010 года, то есть  
пусть только одна пара логин-пароль из n штук подойдет 

### самое простое задание - ppc (фишка в названии, ок да) 
есть доход банка за 20 лет работы в сумме в фемтокопейках (ору)
сотрудник банка просит вас найти количество всех простых чисел
образующих при перемножении это число, так как он новенький и сам не умеет,
а взамен он обещает дать вам что-нибудь полезное для дальнейших хаков.
__и ответ обязательно ограничен 5 попытками.__

### 2 CSA - ppc
Старый добрый банк как никогда нуждается в вычислительных мощностях, поэтому запускает программу распределенных вычислений “Advanced Sausage Computing 2” и просит всех добровольцев помочь в тестировании. Вам нужно намайнить 1 LKLCoin, для этого решайте математические примеры. Ваш человек в банке уже знает, как передать Вам новые секретные данные с помощью этого метода. (вложенные скобки и все операции, кроме деления на ноль. Название - ASCII наоборот. прикол в том, что каждый результат примера на самом деле будет давать число из ascii. и если получившееся предложение перевернуть - получится флаг)  

### Навигатор - ppc
Дана карта московского метро. Нужно ответить на запрос: сколько времени займет поездка от v-той станции до всех остальных.


## forensics - 2 (надо 3)
### hijacking of session - forensics
найти сессию в утекающих логах?...   

### Надо было пихать в микроволновку - forensics
Проходя мимо здания главного офиса ЛКЛБанка перед одним анонимом упала оперативка. Он попытался окликнуть того, кто это сделал, но окно закрылось прямо на его глазах. Будучи смышленным парнем аноним умудрился сделать дамп памяти с помощью атаки cool boot. Он выложил его в сеть. Там вы этот дамп и нашли. Посмотрите, что можно из него вытянуть.

## stego - 
### изи стеганография - stego
Один сотрудник банка (ваш человек)  
пытается передать вам секретные данные через логотип банка (неизвестно как)  
(xor картинки с оригиналом) цель - вытащить данные  

### Секретики - stego
С помощью фишинга вам удалось получить секретный документ банка, где перечислена информация о транзакциях за месяц. Найдите то, что может представлять для Вас интерес. (это excel таблица на 5000 строк, где будет куча мусора сбивающего поиск по шаблону, а флаг спрятан в ее недрах в xml файле, если открыть архиватором)  

### Рингтон - stego
во время посещения пресс-конференции директору банка позвонила его жена. услышав его рингтон по новостям ваши уши сразу же почуяли что-то интересное. осталось только понять что…. (добавить шумов из зала - заставить человека убрать шум а потом получить рисунок с гистограммы) я не знаю даже как рисунок добавить, с математической точки зрения очень просто. Если тебе нужно добавить точку на частоте x, то ты в t-тый момент времени накладываешь волну частотой x. внатуре.

### Таск с классическими невидимыми пробелами - stego
Бла-бла-бла


## recon - (надо 3. сделаю)
### Таск про главного менеджера банка в трех частях.

## reserse - 
### Машина времени - reverse
Ваш человек в банке сказал, что эта программа была создана, как послание для родителей директора ЛКЛ-Банка и привела собственно к открытию банка и его процветанию. программа открывалась только в определенное время - ровно 12:00:00 1 января 1970 года. если дата верна, дает флаг. (не спизжено, а позаимствовано, мне очень понравилось это задание). 

### Профессор Лууп Инфинят - reverse
Основоположником всех крипто алгоритмов является известный математик Лууп Инфинят. ЛКЛБанк использует его алгоритмы в своих продуктах. Вот один из таких продуктов..   
Таск от Тео, у меня есть код. 

### Python-reversing - reverse
Таск на реверс питона

### Have I Got Paid? - reverse
Прошлый сотрудник банка не хотел работать перед самым отпуском, оставив это приложение перед увольнением (добровольным). Сможете разгадать загадку?  
https://mega.nz/#!ykJFHAgI!bt0Dg0buC0mzyjy-FIJJXauWRgNuyfvAmr9DyszcOmA  
(флаг не палится через блокнот, нужно именно декомпилировать)  
LKLCTF{M7_F1757_4PK_3XP3713NC3} (99/100)  

## misc - 
### Телефонный робот - misc
написать бота на webrtc который будет произносить говно и каждый третий символ - символ флага. Типа: спасибо что позвонили в sicamp-bank, ваш звонок очень важен для нас, оператор ответит вам как только сможет. И на мелодию ожидания наложить флаг + мусор. И вставки типа: Добро пожаловать в ЛКЛБанк. Вы позвонили в индивидуальную службу поддержки для компаний. Для улучшения качества обслуживания этот разговор будет записан. К сожалению все операторы сейчас заняты. Вами займется первый освободившийся. Пожалуйста, оставайтесь на линии. Вы [error жестким мужским голосом] в очереди. Примерное время до ответа: NaN минут NaN секунд. а как клиент будет с ботом соединяться? ему же клиент нужен да. либо voip либо webrtc. окей, прикольно.

### Шарорд (пародия на дискорд) - misc
Работники нашего банка заядлые геймеры и поэтому решили сделать себе дискорд. Сможете ли вы найти там конфиденциальную информацию? Ну короче сервер в дискорде. Где музыкальный бот играет never gonna give you up (ложная наводка) а другой бот общается с третьим в чате про рабочие вещи. Нужно настроить чат таким образом чтоб нельзя было просматривать историю сообщений. То есть чтобы видеть новые сообщения нужно быть в чате. Или спрятать флаг кому-то в описание. (я понял, крута). Сам флаг внезапно появляется в разговоре второго и третьего. 

### Таск на ВКонтакте - misc.
Заставить эксплоитить какой-то баг в Вконтакте известный :shrug:  
(а такие есть? да (шок))
