from django.db import models


class Payment(models.Model):
    TYPES = (
        ("Click", "Click"),
        ("Payme", "Payme")
    )
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    type = models.CharField(
        max_length=10,
        choices=TYPES
    )
    role = models.CharField(max_length=30, null=True, blank=True)
    doctor_patient_id = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return f"{self.amount}, {self.type} ({self.date})"


#medland
class Foydalanuvchi(models.Model):
    id = models.CharField(primary_key=True, max_length=111)
    payment_id = models.CharField(max_length=8)
    ism = models.CharField(max_length=255)
    tugilgan_sana = models.CharField(max_length=255)
    jinsi = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255)
    mamlakat = models.CharField(max_length=255)
    viloyat_id = models.IntegerField()
    tuman_id = models.IntegerField()
    tel = models.BigIntegerField()
    letter = models.CharField(max_length=50)
    gmail = models.CharField(max_length=255)
    karta_raqami = models.CharField(max_length=255)
    balance = models.FloatField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    disabled = models.IntegerField()
    tizimda = models.IntegerField()
    online = models.DateTimeField()
    block = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'foydalanuvchi'


class Shifokorlar(models.Model):
    id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=8)
    bosh_cat_id = models.IntegerField()
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    ish_joyi = models.CharField(max_length=255)
    murojat_vaqti_dan = models.TimeField()
    murojat_vaqti_gacha = models.TimeField()
    mamlakat = models.CharField(max_length=255)
    hudud_id = models.IntegerField()
    tuman_id = models.IntegerField()
    ish_boshlagan_sana = models.DateField()
    sana = models.DateField()
    toifasi = models.CharField(max_length=255)
    vrach_haqida = models.IntegerField()
    bolalar_yoshi_id = models.IntegerField()
    tel = models.CharField(max_length=255)
    til = models.CharField(max_length=255, blank=True, null=True)
    narx = models.IntegerField()
    xamshira_limit = models.DateField()
    status = models.CharField(max_length=255)
    online = models.DateTimeField()
    reyting = models.FloatField(blank=True, null=True)
    comment = models.IntegerField(blank=True, null=True)
    idd = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'shifokorlar'


class Balance_History(models.Model):
    payment_id = models.CharField(max_length=8)
    balance = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    tranzaksiya_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'balance_history'