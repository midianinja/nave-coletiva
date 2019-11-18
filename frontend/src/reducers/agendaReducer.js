import * as types from '../constants/actionTypes';
import objectAssign from 'object-assign';
import initialState from './initialState';
import Agenda from '../models/agenda';

function agendaReducer(state = initialState, action) {
  const newState = objectAssign({}, state);

  switch (action.type) {
  case types.LISTA_ATIVIDADES:
    newState.atividades = action.atividades;
    newState.agenda = new Agenda(newState.espacos, newState.atividades, newState.convidades);
    return newState;

  case types.LISTA_ESPACOS:
    newState.espacos = action.espacos;
    newState.agenda = new Agenda(newState.espacos, newState.atividades, newState.convidades);
    return newState;

  case types.LISTA_CONVIDADES:
    newState.convidades = action.convidades;
    newState.agenda = new Agenda(newState.espacos, newState.atividades, newState.convidades);
    return newState;

  default:
    return state;
  }
}


export default agendaReducer;
