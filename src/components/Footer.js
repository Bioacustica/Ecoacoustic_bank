
import React, { Component } from "react";

import itm from "../images/05.Footer/logo-itm.png"
import udea from "../images/05.Footer/logo-udea.png"
import humboldt from "../images/05.Footer/logo-humboldt.png"
import sistemic from "../images/05.Footer/logo-sistemic.png"
import gha from "../images/05.Footer/logo-gha.png"
import minciencias from "../images/05.Footer/min-ciencias.png"
class Footer extends Component {
    render() {
      return (
        <div className=" flex bg-white w-341.5   h-25 mb-4">
        <div className="h-15 ml-3.75 bg-gray-600 mr-10.5 w-23.75 ">
            <h1>Hola</h1>
        </div>
        <div className="h-10.5 justify-center mr-10.5 w-23.75">
            <img src={itm} alt=""/>
        </div>
        <div className="h-10.5 mr-10.5 w-42 justify-center ">
            <img src={udea} alt=""/>
        </div>
        <div className="h-10.5 mr-10.5 w-10.5 justify-center ">
        <img src={humboldt} alt=""/>
        </div>
        <div className="h-12 mr-10.5 w-38.75 w-27.5 justify-center">
        <img src={sistemic} alt=""/>
        </div>
        <div className="h-10.5 mr-10.5 w-20.75 justify-center">
        <img src={gha} alt=""/>
        </div>

        <label className=" ml-64 font-semibold text-xl mr-1">
          Apoya:</label>
        <div className=" h-11 mr-3.75 w-59.75">
        <img src={minciencias} alt=""/>
        </div>
        </div>
      );
    }
  }
  
  export default Footer;
  
