import * as types from '../constants/actionTypes';

const ENDPOINT = 'http://admin.festivalninja.org/api';

export function listaAtividades() {
  return function (dispatch) {
    fetch(`${ENDPOINT}/atividades/`).then((response) => {
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
    fetch(`${ENDPOINT}/espacos/`).then((response) => {
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
    fetch(`${ENDPOINT}/pessoas/`).then((response) => {
      return response.json().then((convidades) => {
        return dispatch({
          type: types.LISTA_CONVIDADES,
          convidades,
        });
      });
    });
  };
}
