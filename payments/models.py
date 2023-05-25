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
    def __str__(self):
        return f"{self.amount}, {self.type} ({self.date})"

