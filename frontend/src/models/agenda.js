import Atividade from './atividade';

Date.prototype.copy = function() {
  return new Date(JSON.parse(JSON.stringify(this)));
}

export const LARGURA_ATIVIDADE = 150;
export const ALTURA_HORA = 170;
export const PRIMEIRA_HORA = 10;
export const TZ = -3;

class Agenda {
  constructor(espacos, atividades, convidades) {
    this.atividades = {
      '21/11': {},
      '22/11': {},
      '23/11': {},
      '24/11': {},
    };
    this.convidades = {};
    this.width = 1;
    this.height = 14 * (ALTURA_HORA + 1) - 1;
    this.buildEspacos(espacos);
    this.buildConvidades(convidades);
    if (espacos.length > 0 && convidades.length > 0) {
      this.buildAtividades(atividades);
    }
    this.horarios = Array.from(Array(14).keys()).map(num => ({
      horario: `${num + PRIMEIRA_HORA}:00`,
      height: ALTURA_HORA,
      top: (num) * ALTURA_HORA + num,
    }));
  }

  buildEspacos(espacos) {
    this.width = 1;
    this.columns = [];
    espacos.forEach((espaco) => {
      espaco.width = espaco.colunas * LARGURA_ATIVIDADE;
      this.width += espaco.width + 1;
      for (let i=0; i<espaco.colunas; i++) {
        this.columns.push({
          width: LARGURA_ATIVIDADE - 1.45, // 1.6 é um valor experimental pra alinhar as linhas do grid
          height: this.height,
        });
      }
    });
    this.espacos = espacos;
  }

  buildConvidades(convidades) {
    convidades.forEach((convidade) => {
      this.convidades[convidade.url] = convidade;
    });
  }

  buildAtividades(atividades) {
    atividades.forEach((regra) => {
      if (!regra.inicio || !regra.fim || !regra.espaco) {
        return;
      }
      this.agendas(regra).forEach((atividade) => {
        if (!this.atividades[atividade.data]) {
          this.atividades[atividade.data] = {};
        }
        if (!this.atividades[atividade.data][atividade.espaco]) {
          this.atividades[atividade.data][atividade.espaco] = [];
        }
        this.atividades[atividade.data][atividade.espaco].push(JSON.parse(JSON.stringify(atividade)));
      });
    });
  }

  agendas(atividade) {
    const inicio = new Date(atividade.inicio);
    const fim = new Date(atividade.fim);
    inicio.setHours(inicio.getHours() - TZ);
    fim.setHours(fim.getHours() - TZ);
    const agendas = [];
    while (inicio.getDate() <= fim.getDate()) {
      let novofim = fim.copy();
      let novoinicio = inicio.copy();
      if (inicio.getDate() <= novofim.getDate()) {
        if (novofim.getDate() > inicio.getDate()) {
          novofim.setDate(inicio.getDate()+1);
          novofim.setHours(0);
        }
      }
      if (novoinicio.getHours() < PRIMEIRA_HORA) {
        novoinicio.setHours(PRIMEIRA_HORA);
      }
      atividade.convidades = atividade.convidades.map(url => this.convidades[url]);
      agendas.push(new Atividade(atividade, novoinicio, novofim));
      inicio.setDate(inicio.getDate() + 1);
      inicio.setHours(0);
    }
    return agendas;
  }
}

export default Agenda;
