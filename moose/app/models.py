from django.db import models

"""
models.CharField(max_length=100) - ma'lum bir uzunlikka ega bo'lgan textlarni kiritish uchun foydalaniladi.
models.TextField() - qavsni ichi bo'sh turadi chunki istalgancha text kiritiladi.
models.DateTimeField(auto_now_add=True) - websitega joylangan vaqtini aniq ko'rsatib turishi uchun foydalaniladi
models.BoolenField(default=True) - True yoki False qaytaradi
models.ImageField(upload_to='blog') - Rasm yuklash uchun ishlatiladi (Yuklanishi kerak bo'lgan joy 'shuni ichida yoziladi')
models.IntegerField(default=0) - Necha marta ko'rilganligini sonini aniqlash uchun ishlatiladi
models.EmailField() - Email kiritish uchun ishlatiladi
models.URLField() - portfoliolariz joylashtrgan website manzillarini joylashtirish uchun ishlatiladi (faqat https malumotlarini ham kiritish kerak)
models.CharField() - portfoliolariz joylashtrgan website manzillarini joylashtirish uchun ishlatiladi (faqat https malumotlarini kiritish shart emas)
"black=True" - kiritish majburiy bo'lmagan narsalar uchun ishlatiladi masalan (subject = models.TextField(max_length=50, blank=True))

"""


# Website ni faqat Blog qismi uchun
class Blog(models.Model):
    title = models.CharField(max_length=100)  # rasmga beriladigan nom title deb kiritiladi
    created_at = models.DateTimeField(auto_now_add=True)  # qaysi vaqtda kiritilganini chiqarish uchun yoziladi
    is_published = models.BooleanField(default=False)  # website ga chiqarilgan yoki yoqligini bilish uchun yoziladi
    comment = models.TextField()  # comment qoldirish uchun ishlatiladigan code
    image = models.ImageField(upload_to='blog')  # rasm yuklash uchun ishlatiladi
    author = models.CharField(max_length=100)  # post kim tomondan qoyilganligini bildiradi
    views = models.IntegerField(default=0)  # necha marta ko'rilganligini soni


# Website ni faqat Contact qismi uchun
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    is_solved = models.BooleanField(default=False)  # Yuborilgan muammolar ko'rib chiqilganmi yoqmi bilish uchun
    created_at = models.DateTimeField(auto_now_add=True)  # qaysi vaqtda kiritilganini chiqarish uchun yoziladi


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField()
    left_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)