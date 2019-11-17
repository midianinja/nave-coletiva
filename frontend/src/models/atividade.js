import { ALTURA_HORA, LARGURA_ATIVIDADE, PRIMEIRA_HORA } from './agenda';

const TZ = -3;

class Atividade {
    constructor(atividade, inicio, fim) {
        this.atividade = JSON.parse(JSON.stringify(atividade));
        inicio.setHours(inicio.getHours() - TZ);
        fim.setHours(fim.getHours() - TZ);
        this.atividade.inicio = inicio.toString();
        this.atividade.fim = fim.toString();
        this.inicio = inicio;
        this.fim = fim;
        debugger;
        this.slots = (fim - inicio) / 3600000 - PRIMEIRA_HORA;
        this.data = inicio.getDate() + '/11'; // novembro
        this.atividade.slots = this.slots;
        this.espaco = atividade.espaco;
        atividade.ordem = atividade.ordem || 1;
        this.style = {
            height: this.slots * (ALTURA_HORA + 1),
            width: LARGURA_ATIVIDADE,
            top: (ALTURA_HORA - 1) * (inicio.getHours() - PRIMEIRA_HORA),
            left: LARGURA_ATIVIDADE * (atividade.coluna - 1),
        };
    }
}

export default Atividade;
