import React from "react";
import { BrowserRouter,Route,Routes} from "react-router-dom";
import PrincipalPage from '../pages/PrincipalPage'
import Login from "../pages/Login";
import RecoverPassword from "../pages/RecoverPassword";
import Administrator from "../pages/Admin";
import LabelledFilter from "../pages/LabelledFilter-Admin";
import AssigmentAdmin from "../pages/Assignment-Filter-Admin";
import DownloadFilter from "../pages/DownloadFilter";
import UserPanel from "../pages/UsersPanel";
import RecorderPanel from "../pages/RecorderPanel";

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
          <Route exact path="/admin-label-filter" element={<LabelledFilter/>}/>
          <Route exact path="/admin-assignment-filter" element={<AssigmentAdmin/>}/>
          <Route exact path="/admin-dowload-filter" element={<DownloadFilter/>}/>
          <Route exact path="/recorder-panel" element={<RecorderPanel/>}/>
          <Route exact path="/user-panel" element={<UserPanel/>}/>
        </Routes>
      </BrowserRouter>
    );
  }
  
  export default Routers;