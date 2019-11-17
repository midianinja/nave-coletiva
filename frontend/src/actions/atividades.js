import * as types from '../constants/actionTypes';

export function listaAtividades() {
  return function (dispatch) {
    fetch('http://admin.festivalninja.org/api/atividades/').then((response) => {
      response.json().then((atividades) => {
        dispatch({
          type: types.LISTA_ATIVIDADES,
          atividades,
        });
      });
    });
  };
}

export function listaEspacos() {
  return function (dispatch) {
    fetch('http://admin.festivalninja.org/api/espacos/').then((response) => {
      return response.json().then((espacos) => {
        return dispatch({
          type: types.LISTA_ESPACOS,
          espacos,
        });
      });
    });
  };
}

export function listaConvidades() {
  return function(dispatch) {
    fetch('http://admin.festivalninja.org/api/pessoas/').then((response) => {
      return response.json().then((convidades) => {
        return dispatch({
          type: types.LISTA_CONVIDADES,
          convidades,
        });
      });
    });
  };
}
