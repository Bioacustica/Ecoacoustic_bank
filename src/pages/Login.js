import React, { Component } from "react";
import Footer from "../components/Footer";
import Head from "../components/Head";
import Navbar from "../components/Navbar";

require("typeface-poppins");
require("typeface-rubik");

class Login extends Component {
  render() {
    return (
      <div>
        <div className="flex justify-center items-center">
          <Head />
        </div>
        <div className="flex justify-center items-center">
          <Navbar />
        </div>
        <div className="flex justify-center">
          <div className="justify-center w-341.5 h-165.25 bg-green-450 mt-8">
            <div className="h-0.625 bg-blue-850 mx-auto mt-14 w-79 mb-3"></div>
            <div className="text-center">
              <h1 className=" font-poppins font-extrabold text-4.5xl text-blue-850 mb-3">
                Iniciar Sesión
              </h1>
            </div>
            <div className="h-0.625 bg-blue-850 mx-auto w-79 "></div>

            <div className="mt-14 mb-10 text-white text-center font-rubik font-normal text-xl">
              <h1>
                Ingrese su dirección de correo electrónico para acceder al
                sistema{" "}
              </h1>
            </div>

            <div className="flex w-341.5 justify-center items-center">
              <form className=" pt-6 ">
                <div className=" mb-6 justify-items-center">
                  <h1 className="text-left text-white  font-poppins font-semibold text-3xl">
                    Usuario
                  </h1>
                  <input
                    name="usuario"
                    type="text"
                    valor="usuario"
                    placeholder="Ingrese usuario"
                    className="placeholder-blue-850 bg-white w-166.25 h-10.75 font-rubik font-light  border-2 border-white border-opacity-100 "
                  />
                </div>
                <div className="mt-9">
                  <h1 className="text-left text-white font-poppins font-semibold text-3xl">
                    Contraseña
                  </h1>
                  <input
                    name="contraseña"
                    type="password"
                    valor="contraseña"
                    placeholder="Ingrese contraseña"
                    className="placeholder-blue-850  w-166.25 h-10.75 mb-4 font-rubik font-light bg-white border-2 border-white border-opacity-100 "
                  />
                </div>
                <div className="flex justify-end w-166.25 mb-10 ">
                  <a
                    className=" text-white text-right
                    font-rubik font-normal text-xl
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
                    href="/recoverpassword"
                  >
                    ¿Olvidaste tu contraseña?{" "}
                  </a>
                </div>
                <div className="flex justify-center w-166.25">
                  <button
                    className="w-76.25 h-13.5 bg-blue-850"
                    type="submit"
                    href="#"
                  >
                    <h1 className="text-white font-poppins font-semibold text-4xl">
                      Ingresar
                    </h1>
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div className="flex justify-center items-center mt-7.25">
          <Footer />
        </div>
      </div>
    );
  }
}

export default Login;
