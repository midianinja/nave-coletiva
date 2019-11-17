import {LISTA_ATIVIDADES} from '../constants/actionTypes';
import objectAssign from 'object-assign';
import initialState from './initialState';

export default function listaAtividadesReducer(state = initialState.atividades, action) {

  switch (action.type) {
    case LISTA_ATIVIDADES:
    const newState = objectAssign({}, state);
    newState.atividades = action.atividades;
    return newState;

    default:
    return state;
  }
}
