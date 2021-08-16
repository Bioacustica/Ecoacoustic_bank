import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Login from "../pages/Login";
import PrincipalPage from "../pages/PrincipalPage";

function Routes() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/principal" component={PrincipalPage} />
      </Switch>
    </BrowserRouter>
  );
}

export default Routes;
