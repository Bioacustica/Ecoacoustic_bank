import React, { useEffect } from "react";
import Head from "../components/Head";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import PublicFilter from "../components/PublicFilter";

import imgBanner from "../images/02.banner 1/imgBanner.jpg";
import aboutUs from "../images/03.Sobre nosotros/aboutUs.jpg";
import map from "../images/04.Visualización/mapas.jpg";
import metadata from "../images/04.Visualización/metadatos.jpg";
import AdministratorNavbar from "../components/AdministratorNavbar";

require("typeface-poppins");
require("typeface-rubik");

function PrincipalPage() {
  return (
    <div>
      <header className="sticky top-0 z-30 bg-white">
        <Head />
        <AdministratorNavbar />
      </header>

      <main>
        <div className="flex justify-center items-center mb-15.75">
          <div className="flex w-341.5 ">
            <img src={imgBanner} alt="" />
          </div>
          <div className="absolute self-center justify-center w-341.5 ">
            <div className="space-y-3">
              <h1 className="text-center font-extrabold font-poppins text-4.5xl text-white">
                CONSERVACIÓN BIOLÓGICA
              </h1>
              <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                USANDO INTELIGENCIA ARTIFICIAL
              </h1>
            </div>
          </div>
        </div>

        <div
          className="h-0.625 bg-blue-850 mx-auto w-83 mb-3"
          id="sobre-nosotros"
        ></div>
        <div>
          <h1 className="text-center font-extrabold font-poppins text-4.5xl text-blue-850 mb-3">
            Sobre nosotros
          </h1>
        </div>
        <div className="h-0.625 bg-blue-850 mx-auto mb-11.5 w-83"></div>

        <div className="flex items-center justify-center mb-7 ">
          <div className="flex  w-341.5 ">
            <div className="w-118.5 h-159  ml-37 mr-18.5 ">
              <img src={aboutUs} alt="" />
            </div>
            <div className="w-128.25 h-159  ">
              <p className="text-justify font-normal font-rubik text-1.5xl text-blue-850">
                Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed
                diam nonummy nibh euismod tincidunt ut laoreet dolore magna
                aliquam erat volutpat. Ut wisi enim ad minim veniam, quis
                nostrud exerci tation ullamcorper suscipit lobortis nisl ut
                aliquip.Lorem ipsum dolor sit amet, consectetuer adipiscing
                elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore
                magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis
                nostrud exerci tation ullamcorper suscipit lobortis nisl ut
                aliquip.
              </p>
              <p className="text-justify font-normal font-rubik text-1.5xl text-blue-850 mt-8.75">
                Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed
                diam nonummy nibh euismod tincidunt ut laoreet dolore magna
                aliquam erat volutpat. Ut wisi enim ad minim veniam, quis
                nostrud exerci tation ullamcorper suscipit lobortis nisl ut
                aliquip.Lorem ipsum dolor sit amet, consectetuer adipiscing
                elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore
                magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis
                nostrud exerci tation ullamcorper suscipit lobortis nisl ut
                aliquip.
              </p>
            </div>
          </div>
        </div>

        <div className="flex items-center justify-center " id="visualizacion">
          <div className="bg-blue-250 w-341.5 ">
            <div className="h-0.625 bg-blue-850 mx-auto w-76  mt-7 mb-3"></div>
            <div>
              <h1 className="text-center font-extrabold font-poppins text-4.5xl text-blue-850 mb-3">
                Visualización
              </h1>
            </div>
            <div className="h-0.625 bg-blue-850 mx-auto mb-11.5 w-76"></div>

            <div className="flex justify-center items-center mb-11.25 ">
              <div>
                <button className=" bg-white mr-7.5 border-solid border-2 w-128.75 h-147.25 border-black hover:bg-gray-300">
                  <div className="imagen bg-pink-100 w-128.5 h-73">
                    <img src={metadata} alt="" />
                  </div>
                  <div className="texto m-6.25">
                    <h1 className="mb-3 text-5xl font-semibold text-left font-poppins text-blue-850">
                      Metadatos
                    </h1>
                    <p className="text-xl font-normal text-justify font-rubik text-blue-850">
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit,
                      sed diam nonummy nibh euismod tincidunt ut laoreet dolore
                      magna Lorem ipsum dolor sit amet, consectetuer adipiscing
                      elit, sed diam nonummy nibh euismod tincidunt ut laoreet
                      dolore magnaLorem ipsum dolor sit amet, consectetuer
                      adipiscing elit, sed diam
                    </p>
                  </div>
                </button>
              </div>

              <div>
                <button className=" bg-white  border-solid border-2 w-128.75 h-147.25 border-black hover:bg-gray-300">
                  <div className="imagen bg-pink-100 w-128.5 h-73">
                    <img src={map} alt="" />
                  </div>
                  <div className="texto m-6.25">
                    <h1 className="mb-3 text-5xl font-semibold text-left font-poppins text-blue-850">
                      Mapas
                    </h1>
                    <p className="text-xl font-normal text-justify font-rubik text-blue-850">
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit,
                      sed diam nonummy nibh euismod tincidunt ut laoreet dolore
                      magna Lorem ipsum dolor sit amet, consectetuer adipiscing
                      elit, sed diam nonummy nibh euismod tincidunt ut laoreet
                      dolore magnaLorem ipsum dolor sit amet, consectetuer
                      adipiscing elit, sed diam
                    </p>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* <div
          className=" h-0.625 bg-blue-850 mx-auto w-37 mt-11.25  mb-3"
          id="filtros"
        ></div>
        <div>
          <h1 className="text-center font-extrabold font-poppins text-4.5xl text-blue-850 mb-3">
            Filtros
          </h1>
        </div>
        <div className="h-0.625 bg-blue-850 mx-auto mb-11.25 w-37 "></div> */}
      </main>

      {/* <PublicFilter /> */}

      <footer>
        <div className="flex justify-center items-center mt-11.25 ">
          <Footer />
        </div>
      </footer>
    </div>
  );
}

export default PrincipalPage;