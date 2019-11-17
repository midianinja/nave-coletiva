import { LISTA_ATIVIDADES, LISTA_ESPACOS } from '../constants/actionTypes';
import objectAssign from 'object-assign';
import initialState from './initialState';
import Agenda from '../models/agenda';

function agendaReducer(state = initialState.agenda, action) {
  const newState = objectAssign({}, state);

  switch (action.type) {
  case LISTA_ATIVIDADES:
      newState.atividades = action.atividades;
      newState.agenda = new Agenda(state.espacos, action.atividades);
      return newState;

  case LISTA_ESPACOS:
      newState.espacos = action.espacos;
      newState.agenda = new Agenda(action.espacos, state.atividades);
      return newState;

  default:
    return state;
  }
}


export default agendaReducer;
