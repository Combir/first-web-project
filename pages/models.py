from django.db import models

class Course(models.Model):
    """Курс иностранного языка в школе M School"""

    LEVEL_CHOICES = [
        ('A1', 'A1 — Beginner'),
        ('A2', 'A2 — Elementary'),
        ('B1', 'B1 — Intermediate'),
        ('B2', 'B2 — Upper Intermediate'),
        ('C1', 'C1 — Advanced'),
        ('C2', 'C2 — Proficiency'),
    ]

    title = models.CharField(
        max_length=200, 
        verbose_name="Название курса"
    )
    description = models.TextField(
        verbose_name="Описание курса"
    )
    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        verbose_name="Уровень"
    )
    duration_months = models.PositiveIntegerField(
        default=3,
        verbose_name="Длительность"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Цена (руб)"
    )

    def __str__(self):
        return f"{self.title} ({self.level}) — {self.price} ₽"