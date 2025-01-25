from celery import shared_task

from .models import Car, Moto


@shared_task
def chek_milage(pk, model):

    if model == Car:
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == m.milage:
                prev_milage = m.milage
            else:
                if prev_milage < m.milage:
                    print("Неверный пробег")
                    break