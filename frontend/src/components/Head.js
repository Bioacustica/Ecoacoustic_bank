import React, { Component } from "react";
import imagesHead from "../helpers/imagesHead";



class Head extends Component {
  render() {
    return (
      <div className="flex bg-white items-center w-341.5 mt-8.75 h-16 justify-center mb-8.75">
       
        <div className="h-16 mr-17.5 w-36.75">
            <img src={imagesHead.img2} alt=""/>
        </div>
        <div className="h-16 mr-17.5 w-63.5 ">
        <img src={imagesHead.img1} alt=""/>
        </div>
        
      </div>
    );
  }
}

export default Head;
