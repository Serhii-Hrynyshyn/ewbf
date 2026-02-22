from django.db import models


class Person(models.Model):
    name = models.CharField("Ім'я'", max_length=100)
    last_name = models.CharField("Прізвище", max_length=100)
    phone_number = models.CharField("Тел.номер", max_length=100)
    email = models.CharField("Е-мейл", max_length=100)
    address = models.CharField("Поточна адреса", max_length=250)
    registration_date = models.DateTimeField('Дата реєстрації')
    login = models.CharField(max_length=50, blank=True, null=True)
    parol = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персони'

    def __str__(self):
        return f"""
                    ПРОФАЙЛ КОРИСТУВАЧА
        -----------------------------------------
        Ім'я: {self.name}
        Прізвище: {self.last_name}
        Телефонний номер: {self.phone_number}
        Електронна адресв: {self.email}
        Поточне місце проживання: 
        {self.address}
        Дата реєстрації: {self.registration_date}
        """
