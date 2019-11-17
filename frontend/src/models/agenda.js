import Atividade from './atividade';

Date.prototype.copy = function() {
    return new Date(JSON.parse(JSON.stringify(this)));
}

export const LARGURA_ATIVIDADE = 150;
export const ALTURA_HORA = 170;

class Agenda {
    constructor(espacos, atividades) {
        this.atividades = {
            '21/11': {},
            '22/11': {},
            '23/11': {},
            '24/11': {},
        };
        this.width = 1;
        this.height = 24 * (ALTURA_HORA + 1) - 1;
        this.buildEspacos(espacos);
        if (espacos.length > 0) {
            this.buildAtividades(atividades);
        }
        this.horarios = Array.from(Array(24).keys()).map(num => ({
            horario: num < 10 ? `0${num}:00` : `${num}:00`,
            height: ALTURA_HORA,
            top: num * ALTURA_HORA + num,
        }));
    }

    buildEspacos(espacos) {
        this.width = 1;
        this.columns = [];
        espacos.forEach((espaco) => {
            espaco.width = espaco.eventos_simultaneos * LARGURA_ATIVIDADE;
            this.width += espaco.width + 1;
            this.columns.push({
                width: LARGURA_ATIVIDADE - 1,
                height: this.height,
            });
        });
        this.espacos = espacos;
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
                this.atividades[atividade.data][atividade.espaco].push(atividade);
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
            agendas.push(new Atividade(atividade, inicio.copy(), novofim.copy()));
            inicio.setDate(inicio.getDate() + 1);
            inicio.setHours(0);
        }
        return agendas;
    }
}

export default Agenda;
