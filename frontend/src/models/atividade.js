import { ALTURA_HORA, LARGURA_ATIVIDADE } from './agenda';

export class Atividade {
    constructor(atividade, inicio, fim) {
        this.atividade = atividade;
        this.inicio = inicio;
        this.fim = fim;
        this.slots = (fim - inicio) / 3600000;
        this.data = inicio.getDate() + '/11';
        this.espaco = atividade.espaco;
        this.style = {
            height: this.slots * ALTURA_HORA,
            width: LARGURA_ATIVIDADE,
            top: ALTURA_HORA * inicio.getHours(),
        };
    }
}

export default Atividade;
