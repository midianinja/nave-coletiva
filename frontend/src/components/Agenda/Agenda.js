import React from 'react';
import PropTypes from 'prop-types';

import AtividadeComponent from './Atividade';
import './agenda.scss';

class AgendaComponent extends React.Component {

  render() {
    const { agenda, data } = this.props;
    const atividadesDoDia = agenda.atividades[data];
    return (
      <div>
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
              <div className="colunas">
                {agenda.columns.map((style, index) => (
                    <div className="coluna" style={style} key={index} />
                ))}
              </div>
              {agenda.horarios.map((horario, index) => {
                return (
                  <div className='grid-row' style={{ width: agenda.width, height: horario.height, top: horario.top }} key={index} />
                );})}
              {agenda.espacos.map((espaco, index) => {
                return (
                  <div className='column' style={{ width: espaco.width, height: agenda.height, left: espaco.left }} key={index} >
                    {(atividadesDoDia[espaco.url] || []).map((atividade, idx) => {
                      return (
                        <div className="atividade-container" style={atividade.style} key={idx}>
                          <AtividadeComponent atividade={atividade.atividade} />
                        </div>
                      );})}
                  </div>
                );})}
            </div>
          </div>
        </div>
      </div>);
  }
}

AgendaComponent.propTypes = {
  agenda: PropTypes.object.isRequired,
  data: PropTypes.string.isRequired,
};

export default AgendaComponent;
