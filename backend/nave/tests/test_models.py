from datetime import date, datetime
from django.test import TestCase, tag

from nave.models import Andar, Espaco

class OrdemTest(TestCase):
    def setUp(self):
        self.andar = Andar.objects.create(nivel=1, nome='primeiro andar')

    def test_espacos_sao_criados_em_ordem(self):
        espaco1 = Espaco.objects.create(andar=self.andar,
                                        nome='sala estudio',
                                        capacidade=10)
        espaco2 = Espaco.objects.create(andar=self.andar,
                                        nome='sala estudio',
                                        capacidade=10)
        espaco3 = Espaco.objects.create(andar=self.andar,
                                        nome='sala estudio',
                                        capacidade=10)

        self.assertEquals(espaco1.ordem, 1)
        self.assertEquals(espaco2.ordem, 2)
        self.assertEquals(espaco3.ordem, 3)

    def test_espacos_sao_reordenados(self):
        espaco1 = Espaco.objects.create(andar=self.andar,
                                        nome='sala estudio',
                                        capacidade=10)
        espaco2 = Espaco.objects.create(andar=self.andar,
                                        nome='sala estudio',
                                        capacidade=10)
        espaco3 = Espaco.objects.create(andar=self.andar,
                                        nome='sala estudio',
                                        capacidade=10)

        espaco2.ordem = 1
        espaco2.save()

        self.assertEquals(Espaco.objects.get(id=espaco1.id).ordem, 2) #mudou
        self.assertEquals(Espaco.objects.get(id=espaco2.id).ordem, 1)
        self.assertEquals(Espaco.objects.get(id=espaco3.id).ordem, 3)
