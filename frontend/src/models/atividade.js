export class Atividade {
    constructor(atividade, inicio, fim) {
        this.atividade = atividade;
        this.inicio = inicio;
        this.fim = fim;
        this.slots = (fim - inicio) / 3600000;
        this.data = inicio.getDate() + '/11';
    }
}

export default Atividade;
