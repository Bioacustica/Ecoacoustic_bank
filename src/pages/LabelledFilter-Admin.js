import React from "react";
import Head from "../components/Head";
import AdministratorNavbar from "../components/AdministratorNavbar";
import imgbanner from "../images/02.banner 1/imgBanner.jpg";
import Footer from "../components/Footer";
import PrivateLabel from "../components/PriveLabelFilter";
import { Link } from "react-router-dom";

require("typeface-poppins");
require("typeface-rubik");



require("typeface-poppins");
require("typeface-rubik");

function LabelledFilter() {
  return (
    <>
      <div className="flex justify-center items-center">
        <div className="w-341.5 ">
          <header className="sticky top-0 z-30  bg-white">
            <div className="flex justify-center items-center">
              <Head />
            </div>
            <div className="flex justify-center items-center">
              <AdministratorNavbar />
            </div>
          </header>

          <body>
            <div className="flex justify-center items-center ">
              <div className="flex w-341.5 ">
                <img src={imgbanner} alt="" />
              </div>
              <div className="absolute self-center justify-center w-341.5 ">
                <div className="space-y-3">
                  <h1 className="text-center font-extrabold font-poppins text-4.5xl text-white">
                    Administrador,
                  </h1>
                  <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                    Filtros
                  </h1>
                </div>
              </div>
            </div>

            <div className="flex justify-center divide-x divide-black divide-x-12.25 h-20.25 w-341.5 bg-blue-250 items-center">
              <div className="hover:bg-blue-200 ">
              <Link to="/admin-label-filter">
                <button className="text-blue-850 w-113.8333 text-xl">
                <label> FILTRO DE </label>
                  <br />
                  <label> ETIQUETADO </label>
                </button>
                </Link>
              </div>
              <div className="hover:bg-blue-200  ">
              <Link to="/admin-assignment-filter">
                <button className="text-white w-113.8333 text-xl">
                  <label> FILTRO ASIGNACIÓN </label>
                  <br />
                  <label> DE AUDIOS PÚBLICOS </label>
                </button>
                </Link>
              </div>

              <div className="hover:bg-blue-200  ">
              <Link to="/admin-dowload-filter">
                <button className="text-white w-113.8333 text-xl">
                  <label> FILTRO DESCARGA </label>
                  <br />
                  <label> DE AUDIOS </label>
                </button>
                </Link>
              </div>
            </div>
            <div className="mt-16">
            <PrivateLabel/>
            </div>
            
          </body>

          <footer>
            <div className="flex justify-center items-center mt-5">
              <Footer />
            </div>
          </footer>
        </div>
      </div>
    </>
  );
}
<script type="text/javascript">
  window.history.forward(); function noBack() {window.history.forward()}
</script>;
export default LabelledFilter;