import React from 'react';
import PropTypes from 'prop-types';

import AtividadeComponent from './Atividade';
import './agenda.scss';

class AgendaComponent extends React.Component {
    state = {
        data: '21/11',
    }

    render() {
        const { agenda } = this.props;
        const atividadesDoDia = agenda.atividades[this.state.data];
        return (
            <div>
              <select id="data" value={this.state.data} onChange={event => this.setState({ data: event.target.value })}>
                <option value="21/11">21/11</option>
                <option value="22/11">22/11</option>
                <option value="23/11">23/11</option>
                <option value="24/11">24/11</option>
              </select>
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
};

export default AgendaComponent;
