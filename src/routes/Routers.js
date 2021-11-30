import React from "react";
import { BrowserRouter,Route,Routes} from "react-router-dom";
import PrincipalPage from '../pages/PrincipalPage'
import Login from "../pages/Login";
import RecoverPassword from "../pages/RecoverPassword";
import Administrator from "../pages/Admin";

function Routers() {
    return (
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<PrincipalPage/>}/>
          <Route exact path="/#sobre-nosotros" element={<PrincipalPage/>}/>
          <Route exact path="/#visualizacion" element={<PrincipalPage/>}/>
          <Route exact path="/#filtros" element={<PrincipalPage/>}/>
          <Route exact path="/admin" element={<Administrator/>}/>
          <Route exact path="/log-in" element={<Login/>}/>
          <Route exact path="/recoverpassword" element={<RecoverPassword/>}/>
        </Routes>
      </BrowserRouter>
    );
  }
  
  export default Routers;