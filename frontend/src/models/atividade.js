import { ALTURA_HORA, LARGURA_ATIVIDADE } from './agenda';

class Atividade {
    constructor(atividade, inicio, fim) {
        this.atividade = atividade;
        this.inicio = inicio;
        this.fim = fim;
        this.slots = (fim - inicio) / 3600000;
        this.data = inicio.getDate() + '/11'; // novembro
        this.atividade.slots = this.slots;
        this.espaco = atividade.espaco;
        atividade.ordem = atividade.ordem || 1;
        this.style = {
            height: this.slots * (ALTURA_HORA + 1),
            width: LARGURA_ATIVIDADE,
            top: (ALTURA_HORA + 1) * inicio.getHours(),
            left: LARGURA_ATIVIDADE * (atividade.coluna - 1),
        };
    }
}

export default Atividade;
