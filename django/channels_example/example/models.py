from django.db import models


class TEST(models.Model):
    TIM = models.CharField(max_length=20)
    TEM = models.CharField(max_length=20)
    HUM = models.CharField(max_length=20)

    class Meta:
        db_table = "TEST"


class TEST1(models.Model):
    TIM = models.CharField(max_length=20)
    TEM = models.CharField(max_length=20)
    HUM = models.CharField(max_length=20)

    class Meta:
        db_table = "TEST1"


class TEST2(models.Model):
    TIM = models.CharField(max_length=20)
    TEM = models.CharField(max_length=20)
    HUM = models.CharField(max_length=20)

    class Meta:
        db_table = "TEST2"


class TEST3(models.Model):
    TIM = models.CharField(max_length=20)
    TEM = models.CharField(max_length=20)
    HUM = models.CharField(max_length=20)

    class Meta:
        db_table = "TEST3"


class TEST4(models.Model):
    TIM = models.CharField(max_length=20)
    TEM = models.CharField(max_length=20)
    HUM = models.CharField(max_length=20)

    class Meta:
        db_table = "TEST4"


# Create your models here.
# class SOURCECOWSFARM(models.Model):
#     COWSFARMID = models.CharField(max_length=20)
#     COWSFARMNAME = models.CharField(max_length=50)
#     COWSFARMLOC = models.CharField(max_length=50)
#     COWSFARMSIZE = models.CharField(max_length=20)
#     COWSFARMPHONE = models.CharField(max_length=20)
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "SOURCECOWSFARM"
#
#
# class SOURCECOWSENVIRONMENT1(models.Model):
#     GATHERTIME = models.CharField(max_length=20)
#     SENSOR = models.CharField(max_length=20)
#     ENVIRONMENTTEM = models.CharField(max_length=20)
#     ENVIRONMENTHUM = models.CharField(max_length=20)
#     ENVIRONMENTPH = models.CharField(max_length=20)
#     ENVIRONMENTPHOTO = models.BinaryField()
#     COWSFARMID = models.CharField(max_length=20)
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "SOURCECOWSENVIRONMENT1"
#
#
# class SOURCECOWSINFO(models.Model):
#     COWSRFID = models.CharField(max_length=100)
#     COWSFARMID = models.CharField(max_length=20)
#     PRODUCTTIME = models.CharField(max_length=20)
#     MILKAMOUNT = models.CharField(max_length=20)
#     COWSPHOTO = models.BinaryField()
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "SOURCECOWSINFO"
#
#
# class SOURCEMILKPROCESSINFO(models.Model):
#     FACTORYID = models.CharField(max_length=20)
#     FACTORYNAME = models.CharField(max_length=50)
#     PROCESSTIME = models.CharField(max_length=20)
#     PACKMATERIAL = models.CharField(max_length=20)
#     SUPPLEMENTNAME = models.CharField(max_length=100)
#     PROCESSPHOTO = models.BinaryField()
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "SOURCEMILKPROCESSINFO"
#
#
# class SOURCEBOTTLEINFO(models.Model):
#     PRODUCTIONTYPE = models.CharField(max_length=20)
#     HSCODE = models.CharField(max_length=30)
#     STORE = models.CharField(max_length=20)
#     PRODUCTIONDATE = models.CharField(max_length=20)
#     EXPIRATIONDATE = models.CharField(max_length=20)
#     MANUFACTURER = models.CharField(max_length=50)
#     MANUFACTURERLOC = models.CharField(max_length=50)
#     NETCONTENT = models.CharField(max_length=20)
#     COWSRFID = models.CharField(max_length=100)
#     OFFICIALWEBSITE = models.CharField(max_length=50)
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "SOURCEBOTTLEINFO"
#
#
# class INDOORDEPOTINFO(models.Model):
#     ID = models.IntegerField()
#     TAGEPC = models.CharField(max_length=32)
#     DEPOTLOC = models.CharField(max_length=50)
#     DEPOTTEM = models.CharField(max_length=20)
#     DEPOTHUM = models.CharField(max_length=20)
#     MANAGERNAME = models.CharField(max_length=20)
#     MANAGERPHONE = models.CharField(max_length=20)
#
#     class Meta:
#         db_table = "INDOORDEPOTINFO"
#
#
# class INDOORMILKPRODUCTINFO(models.Model):
#     TAGEPC = models.CharField(max_length=32)
#     PRONAME = models.CharField(max_length=20)
#     PROINOREX = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = "INDOORMILKPRODUCTINFO"
#
#
# class LOGISTICMILKPRODUCTINFO(models.Model):
#     TAGEPC = models.CharField(max_length=32)
#     PRONAME = models.CharField(max_length=20)
#     PROSELLER = models.CharField(max_length=20)
#     PROSHOPNAME = models.CharField(max_length=20)
#
#     class Meta:
#         db_table = "LOGISTICMILKPRODUCTINFO"
#
#
# class LOGISTICCARINFO(models.Model):
#     TAGEPC = models.CharField(max_length=32)
#     CARID = models.CharField(max_length=32)
#     COMPANY = models.CharField(max_length=32)
#     REGISTERTIME = models.CharField(max_length=20)
#
#     class Meta:
#         db_table = "LOGISTICCARINFO"
#
#
# class LOGISTICDRIVERSINFO(models.Model):
#     TAGEPC = models.CharField(max_length=32)
#     DRIVERID = models.CharField(max_length=32)
#     DRIVERNAME = models.CharField(max_length=32)
#     DRIVERPHONE = models.CharField(max_length=32)
#     DRILICENSE = models.CharField(max_length=32)
#     SEX = models.CharField(max_length=20)
#     NATION = models.CharField(max_length=20)
#
#     class Meta:
#         db_table = "LOGISTICDRIVERSINFO"
#
#
# class LOGISTICTERMINALINFO(models.Model):
#     TERMINALDEVICEID = models.CharField(max_length=32)
#     SIMNO = models.CharField(max_length=32)
#     TEMPERATURE = models.CharField(max_length=32)
#     HUMIDITY = models.CharField(max_length=32)
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "LOGISTICTERMINALINFO"
#
#
# class SOURCESALE(models.Model):
#     MARKETNAME = models.CharField(max_length=20)
#     MARKETLOC = models.CharField(max_length=60)
#     MARKETTEL = models.CharField(max_length=20)
#     SALEDORNOT = models.CharField(max_length=50)
#     TAGEPC = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = "SOURCESALE"