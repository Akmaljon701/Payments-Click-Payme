
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apteka(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    nomi = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255)
    moljal = models.CharField(max_length=255)
    tel = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    ish_vaqti_cheksiz = models.CharField(max_length=20)
    hudud_id = models.IntegerField()
    bosh_cat_id = models.IntegerField(blank=True, null=True)
    reyting = models.FloatField()
    comment = models.IntegerField()
    ish_vaqti = models.TimeField()
    tugash_vaqt = models.TimeField()

    class Meta:
        managed = False
        db_table = 'apteka'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BemorChek(models.Model):
    bemor_id = models.CharField(max_length=255)
    chek_rasm = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bemor_chek'


class BemorHamshiraBuyurtma(models.Model):
    bemor_id = models.CharField(max_length=255)
    shifokor_id = models.CharField(max_length=255, blank=True, null=True)
    bolalar_yoshi_id = models.IntegerField()
    ism = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    muddati = models.IntegerField()
    status = models.CharField(max_length=100)
    operator_id = models.IntegerField(blank=True, null=True)
    jinsi = models.CharField(max_length=100)
    manzil = models.CharField(max_length=255)
    mamlakat = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    viloyat_id = models.IntegerField()
    tuman_id = models.IntegerField()
    tel = models.CharField(max_length=30)
    buyurtma_sana = models.DateTimeField()
    boshlanish_sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bemor_hamshira_buyurtma'


class BemorHamshiraMuolajaFk(models.Model):
    buyurtma_id = models.IntegerField()
    muolaja_id = models.IntegerField()
    hamshira_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bemor_hamshira_muolaja_fk'


class BemorHaqida(models.Model):
    bemor_id = models.CharField(max_length=255)
    kasallik_matni = models.CharField(max_length=255)
    allergiya = models.CharField(max_length=255)
    surunkali = models.CharField(max_length=255)
    sana = models.DateField()

    class Meta:
        managed = False
        db_table = 'bemor_haqida'


class BolalarYoshi(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bolalar_yoshi'


class Calculator(models.Model):
    height = models.IntegerField()
    weight = models.IntegerField()
    normal = models.IntegerField()
    bemor_id = models.CharField(max_length=111)
    sana = models.DateField()
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calculator'


class CatXizmatlar(models.Model):
    idd = models.CharField(max_length=255)
    xizmat_cat_id = models.IntegerField()
    bosh_cat_id = models.IntegerField()
    qurilma = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cat_xizmatlar'


class ChatTugallangan(models.Model):
    bemor_id = models.CharField(max_length=255)
    shifokor_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'chat_tugallangan'


class ClickTransaction(models.Model):
    click_paydoc_id = models.IntegerField()
    amount = models.IntegerField()
    action = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField()
    modified = models.IntegerField()
    extra_data = models.IntegerField()
    message = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'click_transaction'


class ClickuzTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    click_trans_id = models.CharField(max_length=255)
    merchant_trans_id = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    sign_string = models.CharField(max_length=255)
    sign_datetime = models.DateTimeField()
    status = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'clickuz_transaction'


class Comment(models.Model):
    izoh = models.CharField(max_length=255)
    reyting = models.FloatField(blank=True, null=True)
    bosh_cat_id = models.IntegerField()
    reyting_bosh_cat = models.CharField(max_length=255)
    foydalanuvchi_id = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'


class ConsultationNavbat(models.Model):
    bemor_id = models.CharField(max_length=111, db_collation='utf8mb4_unicode_ci')
    doctor_id = models.CharField(max_length=111, db_collation='utf8mb4_unicode_ci')
    sana = models.DateTimeField()
    status_yakunlash = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    oldin_koringan = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    izoh = models.CharField(max_length=500, db_collation='utf8mb4_unicode_ci')
    aloqa = models.CharField(max_length=111, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    reyting = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultation_navbat'


class Dezinfeksiya(models.Model):
    nom = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dezinfeksiya'


class DezinfeksiyaBuyurtma(models.Model):
    bemor_id = models.CharField(max_length=255)
    ism = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    operator_id = models.CharField(max_length=255, blank=True, null=True)
    jinsi = models.CharField(max_length=50)
    manzil = models.CharField(max_length=255)
    mamlakat = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    viloyat_id = models.IntegerField()
    tuman_id = models.IntegerField()
    tel = models.CharField(max_length=20)
    sana = models.DateTimeField()
    chaqiruv_vaqti = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dezinfeksiya_buyurtma'


class DezinfeksiyaBuyurtmaFk(models.Model):
    dezinfeksiya_id = models.IntegerField()
    dezinfeksiya_buyurtma_id = models.IntegerField()
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dezinfeksiya_buyurtma_fk'


class Diagnostika(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    nomi = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)
    moljal = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255)
    tel = models.IntegerField()
    viloyat_id = models.IntegerField()
    tuman_id = models.IntegerField()
    longtude = models.FloatField()
    latude = models.FloatField()
    karta_raqami = models.BigIntegerField()
    narx = models.IntegerField()
    sana = models.DateTimeField()
    reyting = models.FloatField()
    comment = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'diagnostika'


class DiagnostikaKatService(models.Model):
    kat_id = models.IntegerField()
    service_name = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'diagnostika_kat_service'


class DiagnostikaKategoriya(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'diagnostika_kategoriya'


class DiagnostikaNavbat(models.Model):
    diagnostika_id = models.CharField(max_length=111)
    bemor_id = models.CharField(max_length=111)
    sana = models.DateTimeField()
    status = models.CharField(max_length=111)
    status2 = models.CharField(max_length=111)
    ism = models.CharField(max_length=111)
    fam = models.CharField(max_length=111)
    jins = models.CharField(max_length=111)
    yosh = models.IntegerField()
    tel = models.CharField(max_length=111)
    viloyat_id = models.IntegerField()
    tuman_id = models.IntegerField()
    manzil = models.CharField(max_length=111)
    longtude = models.CharField(max_length=111)
    latude = models.CharField(max_length=111)

    class Meta:
        managed = False
        db_table = 'diagnostika_navbat'


class DiagnostikaNavbatService(models.Model):
    navbat_id = models.IntegerField()
    servis_id = models.IntegerField()
    bemor_sana = models.DateField()
    bemor_vaqt = models.TimeField()
    diagostika_sana = models.DateField(blank=True, null=True)
    diagostika_vaqt = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnostika_navbat_service'


class DiagnostikaOnOff(models.Model):
    diagnostika_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'diagnostika_on_off'


class DiagnostikaService(models.Model):
    diagnostic_id = models.CharField(max_length=255)
    kat_id = models.IntegerField()
    kat_service_id = models.IntegerField()
    sana = models.DateField()
    status = models.CharField(max_length=111)
    ishga_kelish_vaqti = models.TimeField()
    ortacha_vaqt = models.TimeField()
    ketish_vaqti = models.TimeField()
    summa = models.IntegerField()
    skidka_narx = models.IntegerField()
    xona = models.CharField(max_length=111)
    uyga_chaqiruv = models.CharField(max_length=255)
    obed_vaqti = models.TimeField()
    obed_tugash_vaqti = models.TimeField()
    dam_olish_kuni = models.CharField(max_length=255)
    masul = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'diagnostika_service'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocUserToken(models.Model):
    ip = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    text = models.CharField(max_length=50)
    sana = models.DateField()
    vaqt = models.TimeField()

    class Meta:
        managed = False
        db_table = 'doc_user_token'


class DoctorPassword(models.Model):
    doctor_id = models.CharField(max_length=255)
    username_tel = models.CharField(max_length=255)
    hash_password = models.CharField(max_length=255)
    tizimda = models.IntegerField()
    online = models.DateTimeField()
    block = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doctor_password'


class Donor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    ism = models.CharField(max_length=255)
    yoshi = models.IntegerField()
    gurux = models.CharField(max_length=255)
    manzili = models.CharField(max_length=255)
    moljal = models.CharField(max_length=255)
    tel = models.IntegerField()
    hudud_id = models.IntegerField()
    bosh_cat_id = models.IntegerField()
    narx = models.IntegerField()
    sana = models.DateField()
    longtude = models.FloatField()
    latude = models.FloatField()
    reyting = models.FloatField()
    comment = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donor'


class DonorOrgan(models.Model):
    donor_id = models.CharField(max_length=255)
    organ = models.CharField(max_length=255)
    xizmat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donor_organ'


class Dorilar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    nomi = models.CharField(max_length=255)
    narx = models.IntegerField()
    ishlab_chiqarish = models.CharField(max_length=255)
    sana = models.DateTimeField()
    apteka_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dorilar'


class Foydalanuvchi(models.Model):
    id = models.CharField(primary_key=True, max_length=111)
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


class FoydalanuvchiRasm(models.Model):
    patient_id = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    filename_id = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'foydalanuvchi_rasm'


class HamshiraMuolaja(models.Model):
    nom = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hamshira_muolaja'


class HamshiraMuolajalarFk(models.Model):
    shifokor_id = models.CharField(max_length=255)
    muolaja_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hamshira_muolajalar_fk'


class Hudud(models.Model):
    nomi = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hudud'


class HududTuman(models.Model):
    nomi = models.CharField(max_length=255)
    viloyat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hudud_tuman'


class Images(models.Model):
    rasm = models.CharField(max_length=255)
    idd = models.CharField(max_length=255)
    bosh_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'images'


class KasallikTurlari(models.Model):
    matn = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kasallik_turlari'


class LandingMalumot(models.Model):
    ism = models.CharField(max_length=255)
    tel = models.IntegerField()
    categoriya = models.CharField(max_length=255)
    sana = models.DateField()

    class Meta:
        managed = False
        db_table = 'landing_malumot'


class Marks(models.Model):
    patient_id = models.CharField(max_length=255)
    doctor_id = models.CharField(max_length=255, blank=True, null=True)
    diagnostic_id = models.CharField(max_length=255, blank=True, null=True)
    sana = models.DateField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'marks'


class Maslaxatlar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    content = models.CharField(max_length=255)
    post = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maslaxatlar'


class MostSeen(models.Model):
    foydalanuvchi_id = models.CharField(max_length=255)
    most_seen_id = models.CharField(max_length=255)
    bosh_cat_id = models.IntegerField()
    soni = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'most_seen'


class Muloqot(models.Model):
    user_doctor = models.IntegerField()
    shifokor_id = models.CharField(max_length=255)
    foydalanuvchi_id = models.CharField(max_length=255)
    chat = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'muloqot'


class Notification(models.Model):
    text = models.CharField(max_length=255)
    sana = models.DateTimeField()
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notification'


class Oferta(models.Model):
    oferta = models.TextField()

    class Meta:
        managed = False
        db_table = 'oferta'


class OperatorChat(models.Model):
    sms = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_doctor_status = models.CharField(max_length=50)
    operator_id = models.IntegerField()
    status = models.CharField(max_length=50)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'operator_chat'


class Parxez(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    retsept_id = models.CharField(max_length=255)
    nomi = models.CharField(max_length=255)
    status = models.IntegerField()
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parxez'


class ParxezUsers(models.Model):
    content = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    izoh = models.TextField()

    class Meta:
        managed = False
        db_table = 'parxez_users'


class PaycomuzTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    field_id = models.CharField(db_column='_id', max_length=255)  # Field renamed because it started with '_'.
    request_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=55)
    cancel_datetime = models.CharField(max_length=255, blank=True, null=True)
    created_datetime = models.CharField(max_length=255, blank=True, null=True)
    order_key = models.CharField(max_length=255, blank=True, null=True)
    perform_datetime = models.CharField(max_length=255, blank=True, null=True)
    reason = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paycomuz_transaction'


class PaymentsPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.IntegerField()
    date = models.DateTimeField()
    completed = models.IntegerField()
    type = models.CharField(max_length=10)
    doctor_patient_id = models.CharField(max_length=9, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments_payment'


class PromoCode(models.Model):
    bloger_name = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    bloger_username = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    bloger_odam_soni = models.CharField(max_length=255)
    promo_code = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    boshlash_vaqti = models.DateField()
    tugash_vaqti = models.DateField()
    active = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')

    class Meta:
        managed = False
        db_table = 'promo_code'


class PromoCodeBemor(models.Model):
    promo_code_id = models.IntegerField()
    bemor_id = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')

    class Meta:
        managed = False
        db_table = 'promo_code_bemor'


class QueueForTheDoctor(models.Model):
    doctor_id = models.CharField(max_length=255)
    patient_id = models.CharField(max_length=255)
    operator_id = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'queue_for_the_doctor'


class Retsept(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    nomi = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    doctor_id = models.CharField(max_length=255)
    sana = models.DateTimeField()
    times = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'retsept'


class RetseptDori(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    retsept_id = models.CharField(max_length=255)
    dori_nomi = models.CharField(max_length=255)
    kun = models.IntegerField()
    maxal = models.IntegerField()
    comment = models.CharField(max_length=255)
    ichildi = models.IntegerField()
    vaqt = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'retsept_dori'


class RetseptLanding(models.Model):
    ismi = models.CharField(max_length=255)
    tel = models.IntegerField()
    retsept_nomi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'retsept_landing'


class ShifokorCarta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    idd = models.CharField(max_length=255)
    uzcart = models.BigIntegerField()
    bosh_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shifokor_carta'


class ShifokorHaqida(models.Model):
    nomi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shifokor_haqida'


class ShifokorKasallikFk(models.Model):
    shifokor_id = models.CharField(max_length=255)
    kasallik_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shifokor_kasallik_fk'


class ShifokorKonsultatsiya(models.Model):
    shifokor_id = models.CharField(max_length=255)
    k_soni = models.IntegerField()
    sana = models.DateField()

    class Meta:
        managed = False
        db_table = 'shifokor_konsultatsiya'


class ShifokorOqiganJoyi(models.Model):
    rasm = models.CharField(max_length=255)
    idd = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255)
    chiqish_yili = models.IntegerField()
    bosh_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shifokor_oqigan_joyi'


class ShifokorSavollar(models.Model):
    shifokor_id = models.CharField(max_length=255)
    savol = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shifokor_savollar'


class Shifokorlar(models.Model):
    id = models.CharField(max_length=255)
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


class Shifoxona(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    nomi = models.CharField(max_length=255)
    hudud_id = models.IntegerField()
    manzili = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    karta_raqami = models.BigIntegerField()
    tel_nomer = models.IntegerField()
    xona_qiymati = models.IntegerField()
    malumotlari = models.CharField(max_length=255)
    long = models.FloatField()
    lat = models.FloatField()
    bosh_cat_id = models.IntegerField()
    reyting = models.FloatField()
    comment = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shifoxona'


class ShifoxonaSixatgoxNavbat(models.Model):
    idd = models.CharField(max_length=255)
    sh_s_xizmat_id = models.IntegerField()
    bemor_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    vaqt_belgilash = models.TimeField()
    sana = models.DateField()

    class Meta:
        managed = False
        db_table = 'shifoxona_sixatgox_navbat'


class ShifoxonaSixatgoxXizmat(models.Model):
    idd = models.CharField(max_length=255)
    xizmat_id = models.IntegerField()
    narx = models.CharField(max_length=255)
    skidka_narx = models.FloatField()
    bosh_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shifoxona_sixatgox_xizmat'


class Sixatgoh(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    nomi = models.CharField(max_length=255, blank=True, null=True)
    izoh = models.CharField(max_length=255, blank=True, null=True)
    manzili = models.CharField(max_length=255, blank=True, null=True)
    moljal = models.CharField(max_length=255, blank=True, null=True)
    longtude = models.FloatField(blank=True, null=True)
    latude = models.FloatField(blank=True, null=True)
    narxi = models.IntegerField(blank=True, null=True)
    bosh_cat_id = models.IntegerField(blank=True, null=True)
    hudud_id = models.IntegerField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    reyting = models.FloatField()
    comment = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sixatgoh'


class Skidka(models.Model):
    diagnostika_id = models.CharField(max_length=255)
    skidka_narx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skidka'


class SmsStatus(models.Model):
    sms_count = models.IntegerField()
    phone = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_status'


class Sorov(models.Model):
    nomi = models.CharField(max_length=255)
    darajasi = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sorov'


class Supply(models.Model):
    large_category_id = models.IntegerField()
    sub_cat_id = models.IntegerField()
    product_id = models.IntegerField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    currency_id = models.IntegerField()
    branch_id = models.IntegerField()
    supplier_id = models.IntegerField()
    datetimes = models.DateTimeField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'supply'


class TaklifHamshira(models.Model):
    bemor_hamshira_buyurtma_id = models.IntegerField()
    price = models.IntegerField()
    hamshira_id = models.CharField(max_length=255)
    bemor_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'taklif_hamshira'


class TaklifHamshiraService(models.Model):
    taklif_hamshira_id = models.IntegerField()
    muolaja_id = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'taklif_hamshira_service'


class TaklifShikoyat(models.Model):
    izoh = models.TextField()
    idd = models.CharField(max_length=255)
    cat = models.CharField(max_length=255)
    c_id = models.IntegerField()
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'taklif_shikoyat'


class Test(models.Model):
    nomi = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'test'


class TestWebsocket(models.Model):
    matn = models.CharField(max_length=255)
    viloyat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test_websocket'


class TexnikJihoz(models.Model):
    idd = models.CharField(max_length=255)
    nomi = models.CharField(max_length=255)
    narxi = models.IntegerField()
    uzunligi = models.IntegerField()
    izoh = models.CharField(max_length=255)
    apteka_id = models.CharField(max_length=255)
    cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'texnik_jihoz'


class TezYordam(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    content = models.CharField(max_length=255)
    post = models.TextField()
    tez_yordam_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tez_yordam'


class TezkorHolat(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tezkor_holat'


class TezkorSorov(models.Model):
    shifokor_id = models.CharField(max_length=255, blank=True, null=True)
    bemor_id = models.CharField(max_length=255)
    holat_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    call_status = models.CharField(max_length=100)
    batafsil = models.CharField(max_length=255, blank=True, null=True)
    manzil = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=20)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tezkor_sorov'


class User(models.Model):
    idd = models.CharField(max_length=255)
    ism = models.CharField(max_length=111)
    phone = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserAvatar(models.Model):
    filename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_avatar'


class Xizmatlar(models.Model):
    nomi = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    bosh_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xizmatlar'


class Yangiliklar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    content = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    rasm = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    sana = models.DateTimeField()
    korildi_soni = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yangiliklar'


class YangiliklarKorilmadi(models.Model):
    yangilik_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    sana = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'yangiliklar_korilmadi'

