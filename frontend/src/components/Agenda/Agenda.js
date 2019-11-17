import React from 'react';

import Agenda from '../../models/agenda';
import style from './agenda.scss';

const AgendaComponent = ({ espacos, atividades }) => {
    const agenda = new Agenda(espacos, atividades);
    return (
        <div  className='agenda' style={{ width: agenda.width }}>
          <div className='espacos' style={{ width: agenda.width }}>
            {agenda.espacos.map((espaco, index) => {
                return (
                    <div className='espaco' style={{ width: espaco.width }} key={index}>{espaco.nome}</div>
                );})}
          </div>
        </div>
  );
}

export default AgendaComponent;
