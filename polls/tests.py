from django.test import TestCase
from polls.models import *
import logging 
# Create your tests here.
 
 
import sys
logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))

class CosoModelTest(TestCase):
    
    def test_basic_test(self):

        # Inserisci
        c1 = Coso()
        c1.id_coso = 1
        c1.descrizione_coso = "Coso N° 1"
        c1.save()

        a=None
        a=AttributoCoso()
        a.id_coso=c1
        a.cod_attributo="A"
        a.valore_attributo="1 -- attr A"
        a.save()

        a=None
        a=AttributoCoso()
        a.id_coso=c1
        a.cod_attributo="B"
        a.valore_attributo="1 -- attr B"
        a.save()

        a=None
        a=AttributoCoso()
        a.id_coso=c1
        a.cod_attributo="C"
        a.valore_attributo="1 -- attr C"
        a.save()

        c2 = Coso()
        c2.id_coso = 2
        c2.descrizione_coso = "Coso N° 2"
        c2.save()

        a=None
        a=AttributoCoso()
        a.id_coso=c2
        a.cod_attributo="A"
        a.valore_attributo="2 -- attr A"
        a.save()

        a=None
        a=AttributoCoso()
        a.id_coso=c2
        a.cod_attributo="B"
        a.valore_attributo="2 -- attr B"
        a.save()

        a=None
        a=AttributoCoso()
        a.id_coso=c2
        a.cod_attributo="C"
        a.valore_attributo="2 -- attr C"
        a.save()

        c3 = Coso()
        c3.id_coso = 3
        c3.descrizione_coso = "Coso N° tre"
        c3.save()                

        cx = Coso.objects.get(id_coso=3)
        cx.descrizione_coso = "Coso N° 3"
        cx.save()

        for id in range(1, 4):
            print ("------------- Coso id = " + str(id))
            cx = Coso.objects.get(id_coso=id)
            print (cx)
            print ("Attributi = " + str(id))
            print (cx.attributocoso_set.all())


        print ("Elenco oggetti coso")
        clist = Coso.objects.all()
        print (clist)

 

 
