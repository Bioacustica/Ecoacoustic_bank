import React, { Component } from "react";
import Footer from "../components/Footer";
import Head from "../components/Head";
import Navbar from "../components/Navbar";
import AdministratorNavbar from "../components/AdministratorNavbar";

require("typeface-poppins");
require("typeface-rubik");
class Recuperar extends Component {
  render() {
    return (
      <div>
        <header className="sticky top-0 z-30 bg-white">
          <Head />
          <AdministratorNavbar />
        </header>

        <div className="flex justify-center">
          <div className="justify-center w-341.5 h-133.5 bg-green-450 mt-8">
            <div className="h-0.625 bg-blue-850 mx-auto mt-14 w-107 mb-3"></div>
            <div className="text-center">
              <h1 className="mb-3 text-4xl font-extrabold text-blue-850 font-poppins">
                Recuperar Contraseña
              </h1>
            </div>
            <div className="h-0.625 bg-blue-850 mx-auto w-107 "></div>

            <div className="text-xl font-normal text-center text-white mt-9 font-rubik">
              <h1>
                Ingrese su dirección de correo electrónico y te enviaremos un
                con
              </h1>
              <h1>instruciones para recuperar tu contraseña</h1>
            </div>

            <div className="flex w-341.5 justify-center items-center">
              <form className="mt-6">
                <div className="">
                  <h1 className="text-4xl font-semibold text-left text-white font-poppins">
                    Mail
                  </h1>
                  <input
                    name="mail"
                    type="email"
                    valor="mail"
                    placeholder="Ingresar tu mail"
                    className="placeholder-blue-850 w-166.25 h-10.75 mb-4 font-light font-rubik bg-white border-2 border-white border-opacity-100 "
                  />
                </div>
                <div className="flex justify-end w-166.25 mb-10 ">
                  <a
                    href="/log-in"
                    className="text-xl font-semibold text-right text-white border-b-2 font-rubik hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
                  >
                    Iniciar Sesión
                  </a>
                </div>
                <div className="flex justify-center w-166.25">
                  <button
                    className="w-120.25 h-13.25 bg-blue-850"
                    type="submit"
                    href="#"
                  >
                    <h1 className="text-4xl font-semibold text-white font-poppins">
                      Recuperar Contraseña
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

export default Recuperar;
