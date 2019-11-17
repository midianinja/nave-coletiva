import Atividade from './atividade';

Date.prototype.copy = function() {
    return new Date(JSON.parse(JSON.stringify(this)));
}

const LARGURA_ATIVIDADE = 100;
const ALTURA_HORA = 100;

class Agenda {
    constructor(espacos, atividades) {
        this.datas = [];
        this.index = {
            datas: {},
        };
        this.width = 0;
        this.height = 24 * ALTURA_HORA;
        this.buildEspacos(espacos);
        if (espacos.length > 0) {
            this.buildAtividades(atividades);
        }
        this.horarios = Array.from(Array(24).keys()).map(num => ({
            horario: num < 10 ? `0${num}:00` : `${num}:00`,
            height: ALTURA_HORA,
        }));
    }

    buildEspacos(espacos) {
        espacos.forEach((espaco) => {
            espaco.width = espaco.eventos_simultaneos * LARGURA_ATIVIDADE;
            this.width += espaco.width;
        });
        this.espacos = espacos;
    }

    buildAtividades(atividades) {
        atividades.forEach((regra) => {
            if (!regra.inicio || !regra.fim || !regra.espaco) {
                return;
            }
            this.agendas(regra).forEach((atividade) => {
                if (!this.datas[atividade.data]) {
                    this.datas[atividade.data] = {};
                }
                if (!this.datas[atividade.data][atividade.espaco]) {
                    this.datas[atividade.data][atividade.espaco] = [];
                }
                this.datas[atividade.data][atividade.espaco].push(atividade);
            });
        });
    }

    agendas(atividade) {
        const inicio = new Date(atividade.inicio);
        const fim = new Date(atividade.fim);
        const agendas = [];
        while (inicio.getDate() <= fim.getDate()) {
            let novofim = fim.copy();
            if (inicio.getDate() <= novofim.getDate()) {
                if (novofim.getDate() > inicio.getDate()) {
                    novofim.setDate(inicio.getDate()+1);
                    novofim.setHours(0);
                }
            }
            agendas.push(new Atividade(atividade, inicio.copy(), novofim));
            inicio.setDate(inicio.getDate() + 1);
            inicio.setHours(0);
        }
        return agendas;
    }
}

export default Agenda;
