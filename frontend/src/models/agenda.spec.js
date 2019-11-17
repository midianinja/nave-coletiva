import Agenda from './agenda';

describe('Agenda', () => {
    const espacos = [
        { id: 1, nome: 'sala' },
        { id: 2, nome: 'estudio' },
    ];

    beforeAll(() => {
    });

    it('atividade que termina no dia seguinte é quebrada em duas', () => {
        const atividade = {
            id: 1,
            nome: 'vários dias',
            inicio: 'Thu Nov 21 2019 22:00:00 GMT-0300',
            fim: 'Thu Nov 22 2019 2:00:00 GMT-0300',
            espaco: 1,
        };

        const agenda = new Agenda(espacos, [ atividade ]);
        const agendas = agenda.agendas(atividade);
        expect(agendas.length).toBe(2);
        expect(agendas[0].inicio.getDate()).toBe(21);
        expect(agendas[0].fim.getDate()).toBe(22);
        expect(agendas[0].fim.getHours()).toBe(0);
        expect(agendas[0].fim.getMinutes()).toBe(0);
        expect(agendas[1].inicio).toStrictEqual(agendas[0].fim);
        expect(agendas[1].fim.getDate()).toBe(22);
        expect(agendas[1].fim.getHours()).toBe(2);
    });

    it('atividade que termina dois dias depois é quebrada em tres', () => {
        const atividade = {
            id: 1,
            nome: 'vários dias',
            inicio: 'Thu Nov 21 2019 22:00:00 GMT-0300',
            fim: 'Thu Nov 23 2019 2:00:00 GMT-0300',
            espaco: 1,
        };

        const agenda = new Agenda(espacos, [ atividade ]);
        const agendas = agenda.agendas(atividade);
        expect(agendas.length).toBe(3);
        expect(agendas[0].inicio.getDate()).toBe(21);
        expect(agendas[0].fim.getDate()).toBe(22);
        expect(agendas[0].fim.getHours()).toBe(0);
        expect(agendas[0].fim.getMinutes()).toBe(0);
        expect(agendas[1].inicio).toStrictEqual(agendas[0].fim);
        expect(agendas[1].fim.getDate()).toBe(23);
        expect(agendas[1].fim.getHours()).toBe(0);
        expect(agendas[2].inicio).toStrictEqual(agendas[1].fim);
        expect(agendas[2].fim.getDate()).toBe(23);
        expect(agendas[2].fim.getHours()).toBe(2);
    });

});
