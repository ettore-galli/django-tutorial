from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class Coso(models.Model):
    id_coso = models.BigIntegerField(db_column="IDCOSO", primary_key=True)
    descrizione_coso = models.CharField(max_length=255, db_column="DECOSO")

    def __str__(self):
        return str(self.id_coso) + ": " + self.descrizione_coso


class AttributoCoso(models.Model):
    id_coso = models.ForeignKey(Coso, on_delete=models.PROTECT, db_column="IDCOSO")
    cod_attributo = models.CharField(db_column="CODATTR", max_length=20)
    valore_attributo = models.CharField(max_length=255, db_column="VALATTR")

    def __str__(self):
        return self.cod_attributo + " : " + self.valore_attributo