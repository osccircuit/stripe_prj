from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return str(self.name).capitalize()


class Order(models.Model):
    items = models.ManyToManyField(Item, through="OrderItem")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()

    def create_description(self):
        lines = [
            f'{oi.item.name} -- {oi.item.price} * {oi.quantity}'
            for oi in self.orderitem_set.all()
        ]
        self.description = '<br>'.join(lines)
        self.save()
        
    def calc_total(self):
        total = sum([
            oi.item.price * oi.quantity
            for oi in self.orderitem_set.all()
        ])
        self.total_amount = total
        self.save()
        
    def __str__(self):
        return f'№ {str(self.pk)}'
    

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} * {self.item.name}"