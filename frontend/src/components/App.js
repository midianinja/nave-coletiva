/* eslint-disable import/no-named-as-default */
import { NavLink, Route, Switch } from "react-router-dom";

//import 'bootstrap/dist/css/bootstrap.min.css';

import Agenda from "./Agenda/Agenda";
import PropTypes from "prop-types";
import React from "react";
import { hot } from "react-hot-loader";

// This is a class-based component because the current
// version of hot reloading won't hot reload a stateless
// component at the top-level.

class App extends React.Component {
  render() {
    const activeStyle = { color: 'blue' };
    return (
        <Switch>
          <Route exact path="/" component={Agenda} />
        </Switch>
    );
  }
}

App.propTypes = {
  children: PropTypes.element
};

export default hot(module)(App);
