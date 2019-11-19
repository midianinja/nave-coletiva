import { ALTURA_HORA, LARGURA_ATIVIDADE, PRIMEIRA_HORA } from './agenda';

class Atividade {
    constructor(atividade, inicio, fim) {
        this.atividade = JSON.parse(JSON.stringify(atividade));
        this.atividade.inicio = inicio.toString();
        this.atividade.fim = fim.toString();
        this.inicio = inicio;
        this.fim = fim;
        this.slots = (fim - inicio) / 3600000;
        this.data = inicio.getDate() + '/11'; // novembro
        this.atividade.slots = this.slots;
        this.espaco = atividade.espaco;
        atividade.ordem = atividade.ordem || 1;
        this.style = {
            height: this.slots * (ALTURA_HORA + 0.5),
            width: LARGURA_ATIVIDADE * this.atividade.largura - 2,
            top: (ALTURA_HORA + 1) * ((inicio.getHours() - PRIMEIRA_HORA) + inicio.getMinutes() / 60),
            left: LARGURA_ATIVIDADE * (atividade.coluna - 1),
        };
    }
}

export default Atividade;
