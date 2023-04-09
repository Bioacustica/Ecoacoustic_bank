import React from "react";
import ReactDOM from "react-dom";

import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import "./index.css";

import reportWebVitals from "./reportWebVitals";
import Routers from "./routes/Routers";

ReactDOM.render(
  <>
    <Routers />
    <ToastContainer />
  </>,

  document.getElementById("root")
);

reportWebVitals();
