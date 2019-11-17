import { Atividade } from './atividade';

describe('Atividade', () => {
    it('tem data', () => {
        const dados = {
            id: 1,
            nome: 'vários dias',
            inicio: 'Thu Nov 21 2019 22:00:00 GMT-0300',
            fim: 'Thu Nov 21 2019 23:00:00 GMT-0300',
            espaco: 1,
        };
        const atividade = new Atividade(dados, new Date(dados.inicio), new Date(dados.fim));
        expect(atividade.data).toBe('21/11');
    });

});
