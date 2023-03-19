from django.db import models


class Budget(models.Model):
    date = models.DateField(verbose_name="Дата")
    amount_spent = models.IntegerField(verbose_name="Потраченная сумма")
    description = models.CharField(max_length=200, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "family_budget"

    def __str__(self) -> str:
        return f"{self.date} --- {self.amount_spent} --- {self.description}"

    __repr__ = __str__

    # def get_absolute_url(self):
    #     return reverse(kwargs={'pk': self.pk})
