import { combineReducers } from 'redux';
import agendaReducer from './agendaReducer';
import { connectRouter } from 'connected-react-router'

const rootReducer = history => combineReducers({
  router: connectRouter(history),
  agenda: agendaReducer,
});

export default rootReducer;
