from django.db import models


class Budget(models.Model):

    date = models.DateField()
    amount_spent = models.IntegerField()
    description = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "family_budget"

    def __str__(self) -> str:
        return f"{self.date} --- {self.amount_spent} --- {self.description}"

    __repr__ = __str__
