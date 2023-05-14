# FRAYDEY - Savdogar va mijozlarning hamkori

Demo - https://fraydey.uz

**Maqsad** - _Savdogarlarni hisob-kitob ishlarini yengillashtirish, savdodagi tovarlarni bir vaqtni o'zida sonlarini, narxlarini kuzatib borish uchun web dastur yaratish._

- [Fraydey](#fraydey---savdogar-va-mijozlarning-hamkori)
   - [Qanday foyda olib keladi?](#fraydey-qanday-foyda-olib-keladi)
   - [Amalga oshirilgan ishlar](#amalga-oshirilgan-ishlar)
   - [Kamchiliklar va qilinishi zarur bo'lgan ishlar](#kamchiliklar-va-qilinishi-zarur-bolgan-ishlar)
   - [Dasturni lokal kompyuter serverga o'rnatish uchun qo'llanma](#dasturni-lokal-kompyuter-serverga-ornatish-uchun-qollanma)
   - [Hissa qo'shish](#contributions-hissa-qoshish)
   - [Aloqa](#aloqa)

## Fraydey QANDAY foyda olib keladi?
- Savdogarlar kunlik savdolarni **yozib borish**lariga ehtiyojni yo'q qiladi, barcha savdolar dasturda saqlanib boradi
- Hisob kitoblarni kamaytiradi, _kunlik_, _oylik_ va _yillik_ savdo hisobotlarini tartib bilan, **grafikda** tasvirlab beradi, bu orqali do'kon yoki biznes qay darajada rivojlanayotganini ko'rish mumkin
- Savdogarlarni mijozlar bilan bog'laydi, albatta barcha do'kon yoki biznes uchun onlayn mavjudlik muhim, va buni bir do'kon boshqaruvi bilan bir joyda yig'ilishi savdoni yengillashtiradi va ko'proq mijozlarga erishishni taminlaydi
- Ochiq-kodli dastur, demo versiyani xavfsizligiga ishonmagan foydalanuvchilar uchun dasturni o'z kompyuterlariga o'rnatish uchun [**qo'llanma**](#dasturni-lokal-kompyuter-serverga-ornatish-uchun-qollanma) mavjud



## Amalga oshirilgan ishlar
- [X] Registratsiya sahifasi
    - [X] Savdogarni ro'yxatdan o'tkazish
    - [X] Mijozlarni ro'yxatdan o'tkazish
    - [X] Sodda dizayn
- [X] Login sahifasi
    - [X] Savdogarlar uchun login 
- [X] Logout sahifasi
    - [X] Savdogarlar uchun logout
- [X] Dashboard sahifasi
    - [X] Mahsulotlar
    - [X] Qarzlar
    - [X] Chegirmalar
    - [X] Do'kon byudjeti
    - [X] Eng ko'p sotilgan mahsulotlar
    - [X] Kunlik savdo foydasi grafiklari


## Kamchiliklar va qilinishi zarur bo'lgan ishlar
- [ ] Sayt dizaynini optimallashtirish, keraksiz kodlarni tozalash
- [ ] Rasmlarni yuklaganda serverni to'ldirib yubormaydigan variantini topish
- [ ] Mijozlar uchun ijtimoiy tarmoqni tashkillashtirish
- [ ] Kiberxavfsizlik tomonidan kodni tahlil qilish
- [ ] Savdogarlar uchun BarCode|QR Code tizimini ishlab chiqish

## Dasturni lokal kompyuter serverga o'rnatish uchun Qo'llanma
### 1) Githubdan dasturni yuklash va djangoni o'rnatish
```cmd
git clone https://github.com/cyberspyde/fraydey
```

```cmd
cd fraydey
```

```cmd
pip install django django_resized django_multiselectfield pillow
```

### 2) Serverni ishga tushirish
```cmd
python manage.py runserver
```

### 3) Kompyuter browserdan dasturni ochish

Browser : http://localhost:8000

---
## Contributions (Hissa qo'shish)
Proyektga o'z hissasini qo'shishni xohlaganlar, proyektdan fork yaratgan holatda kamchiliklar va qilinishi zarur bo'lgan ishlar bo'limidagi kamchiliklarni tuzatish bilan yordam berishingiz mumkin, proyektdan boshqa kamchiliklar topsangiz, issues bo'limidan request qiling. 

## Aloqa
 [![Mailing list : test](http://img.shields.io/badge/Email-gray.svg?style=for-the-badge&logo=gmail)](mailto:cyberspyde@gmail.com) [![Mailing list : test](http://img.shields.io/badge/Telegram-blue.svg?style=for-the-badge&logo=telegram)](https://t.me/cyberspyde_admin)
