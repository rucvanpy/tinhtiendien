from django.db import models

# Create your models here.
class GiaDienEVN(models.Model):
    start_date = models.DateField('Ngày bắt đầu')
    end_date = models.DateField('Ngày kết thúc')

    def __str__(self):
        return "Giá điện từ ngày " + str(self.start_date) + " đến " + str(self.end_date)


class DinhMuc(models.Model):
    gia_dien_evn = models.ForeignKey(GiaDienEVN, on_delete=models.CASCADE)
    level_no = models.IntegerField()
    level_start = models.IntegerField()
    level_end = models.IntegerField()
    level_price = models.IntegerField()

    def __str__(self):
        desc = "Định mức {}, từ ngày {} tới ngày {}".format(self.level_no, self.gia_dien_evn.start_date,
                                                            self.gia_dien_evn.end_date)
        return desc
