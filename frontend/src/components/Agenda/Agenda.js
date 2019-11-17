import React from 'react';

import Agenda from '../../models/agenda';
import style from './agenda.scss';

const AgendaComponent = ({ espacos, atividades }) => {
    const agenda = new Agenda(espacos, atividades);
    return (
        <div  className='agenda'>
          <div className='espacos-header' style={{ width: agenda.width }}>
            {agenda.espacos.map((espaco, index) => {
                return (
                    <div className='espaco-header' style={{ width: espaco.width }} key={index}>{espaco.nome}</div>
                );})}
          </div>
          <div className='horarios-header'>
            {agenda.horarios.map((horario, index) => {
                return (
                    <div className='horario-header' style={{ height: horario.height }} key={index}><div className="horario">{horario.horario}</div></div>
                );})}
          </div>
          <div className="canvas" style={{ width: agenda.width, height: agenda.height }}>
            <div className="container">
              {agenda.horarios.map((horario, index) => {
                  return (
                      <div className='grid-row' style={{ width: agenda.width, height: horario.height, top: horario.top }} key={index} />
                  );})}
              {agenda.espacos.map((espaco, index) => {
                  return (
                      <div className='column' style={{ width: espaco.width, height: agenda.height, left: espaco.left }} key={index} ></div>
                  );})}
            </div>
          </div>
        </div>
  );
}

export default AgendaComponent;
