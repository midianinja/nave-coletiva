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
                    <div className='horario-header' style={{ height: horario.height }} key={index}>{horario.horario}</div>
                );})}
          </div>
          <div className="canvas" style={{ width: agenda.width, height: agenda.height }}>
            {agenda.horarios.map((horario, index) => {
                return (
                    <div className='grid-row' style={{ width: agenda.width, height: horario.height }} key={index} />
                );})}
            {agenda.espacos.map((espaco, index) => {
                return (
                    <div className='column' style={{ width: espaco.width, height: agenda.height }} key={index} />
                );})}
          </div>
        </div>
  );
}

export default AgendaComponent;
