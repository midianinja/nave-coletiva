import React from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import AtividadeComponent from './Atividade';
import Agenda from '../../models/agenda';
import style from './agenda.scss';

import * as actions from '../../actions/atividades';

class AgendaComponent extends React.Component {
    state = {
        data: '21/11',
    }

    componentDidMount() {
        this.props.actions.listaAtividades();
        this.props.actions.listaEspacos();
    }

    render() {
        const { agenda } = this.props;
        const atividadesDoDia = agenda.atividades[this.state.data];
        return (
            <div>
              <h1>Festival Ninja</h1>
              <h2>Programação</h2>
              <h3>Confira abaixo a programação completa</h3>
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
    actions: PropTypes.object.isRequired,
    agenda: PropTypes.object,
};

AgendaComponent.defaultProps = {
    agenda: new Agenda([], []),
};

function mapStateToProps(state) {
  return {
      agenda: state.agenda.agenda,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(actions, dispatch)
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AgendaComponent);
