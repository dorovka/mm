from django.db import models

# Create your models here.
class Advertisement(models.Model):
    
    class Meta:
        db_table = 'advertisements'
    
    title = models.CharField('название', max_length=120)
    descriptions = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=9, decimal_places=2)
    trades = models.BooleanField('Торг', help_text='Если хотим торговаться')
    date_now = models.DateField('Создание дата', auto_now_add= True)
    date_update = models.DateField("Обновление дата", auto_now= True) 
    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    '''
    def __str__(self): 
        return f'<Advertisement: Advertisement(id=1, title= "Заголовок №1", price=100.00)>'
    '''
    pass

