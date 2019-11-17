import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import EscolheDia from './Agenda/EscolheDia';
import Agenda from './Agenda/Agenda';
import * as actions from '../actions/atividades';

class HomePage extends React.Component {
  componentDidMount() {
    this.props.actions.listaAtividades();
    this.props.actions.listaEspacos();
  }

  render() {
      const { atividades, espacos } = this.props;
      return (
          <div>
            <h1>Festival Ninja</h1>
            <h2>Programação</h2>
            <h3>Confira abaixo a programação completa</h3>
            <EscolheDia/>
            <Agenda atividades={atividades} espacos={espacos} />
          </div>
    );
  }
};

HomePage.propTypes = {
  actions: PropTypes.object.isRequired,
  atividades: PropTypes.array,
  espacos: PropTypes.array,
};

function mapStateToProps(state) {
  return {
    atividades: state.agenda.atividades,
    espacos: state.agenda.espacos,
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
)(HomePage);
