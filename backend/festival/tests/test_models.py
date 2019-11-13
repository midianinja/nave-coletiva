from datetime import date, datetime
from django.test import TestCase, tag
from django.core.exceptions import ValidationError

from festival.models import Festival, Encontro, Categoria, Atividade
from nave.models import Andar, Espaco
from rede.models import Pessoa

class BaseTest(TestCase):
    def setUp(self):
        self.festival = Festival.objects.create(nome='Festival Ninja',
                                                inicio=date(2019, 11, 21),
                                                fim=date(2019, 11, 24))
        self.responsavel = Pessoa.objects.create(nome='Responsavel')
        andar = Andar.objects.create(nivel=1, nome='primeiro andar')
        self.estudio = Espaco.objects.create(andar=andar,
                                             nome='sala estudio',
                                             capacidade=10)
        self.hackerspace = Espaco.objects.create(andar=andar,
                                                 nome='hackerspace',
                                                 capacidade=10)
        self.kwargs = dict(
            pendente=False,
            festival=self.festival,
            espaco=self.estudio,
            responsavel=self.responsavel,
            )

class AtividadeNaoPodeConflitarHorario(BaseTest):
    def setUp(self):
        super().setUp()
        Atividade.objects.create(**self.kwargs,
                                 inicio=datetime(2019, 11, 21, 8),
                                 fim=datetime(2019, 11, 21, 10),
                                 titulo='encontro',
                                 descricao='...')

    def test_pode_haver_conflito_de_horario_em_espacos_diferentes(self):
        self.kwargs['espaco'] = self.hackerspace
        Atividade.objects.create(**self.kwargs,
                                 inicio=datetime(2019, 11, 21, 8),
                                 fim=datetime(2019, 11, 21, 10),
                                 titulo='encontro',
                                 descricao='...')

    def test_horario_exato(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 8),
                              fim=datetime(2019, 11, 21, 10),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_inicio_antes_fim_depois(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 7),
                              fim=datetime(2019, 11, 21, 11),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_inicio_antes_fim_durante(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 7),
                              fim=datetime(2019, 11, 21, 9),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_inicio_durante_fim_depois(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 9),
                              fim=datetime(2019, 11, 21, 11),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_inicio_exato_fim_durante(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 8),
                              fim=datetime(2019, 11, 21, 9),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_inicio_durante_fim_exato(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 9),
                              fim=datetime(2019, 11, 21, 10),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_inicio_durante_fim_durante(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 9, 0),
                              fim=datetime(2019, 11, 21, 9, 30),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir colisão de horários na mesma sala")

    def test_regressao_atividade_pode_conflitar_horario_se_nao_tiver_espaco(self):
        del self.kwargs['espaco']
        self.kwargs['pendente'] = True
        atividade = Atividade.objects.create(**self.kwargs,
                                             inicio=datetime(2019, 11, 21, 9, 0),
                                             fim=datetime(2019, 11, 21, 9, 30),
                                             titulo='encontro',
                                             descricao='...')
        atividade2 = Atividade.objects.create(**self.kwargs,
                                              inicio=datetime(2019, 11, 21, 9, 0),
                                              fim=datetime(2019, 11, 21, 9, 30),
                                              titulo='encontro',
                                              descricao='...')
        try:
            atividade.clean()
            atividade2.clean()
        except ValidationError:
            self.fail("Deveria permitir colisão de horários quando nao tem espaco")


class AtividadeTest(BaseTest):
    def setUp(self):
        super().setUp()

    def test_inicio_nao_pode_ser_igual_ao_fim(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 9, 0),
                              fim=datetime(2019, 11, 21, 9, 0),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir horário início igual ao fim")

    def test_inicio_nao_pode_ser_depois_do_fim(self):
        atividade = Atividade(**self.kwargs,
                              inicio=datetime(2019, 11, 21, 10, 0),
                              fim=datetime(2019, 11, 21, 9, 0),
                              titulo='encontro',
                              descricao='...')
        try:
            atividade.clean()
        except ValidationError:
            pass
        else:
            self.fail("Não deveria permitir horário início depois do fim")
