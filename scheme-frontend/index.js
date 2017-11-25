import React from 'react';
import SchemeForm from './modules/containers/SchemeForm';
import UserProfile from './modules/containers/UserProfile';
import App from './modules/App';
import { Router, Route, hashHistory } from 'react-router';
import { render } from 'react-dom';

render((
  <Router history={hashHistory}>
    <Route path="/" component={App}/>
    <Route path="/profile" component={UserProfile}/>
    <Route path="/scheme" component={SchemeForm}/>
  </Router>
), document.getElementById('app'))
