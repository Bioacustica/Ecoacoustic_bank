import React from "react";
import Head from "../components/Head";
import AdministratorNavbar from "../components/AdministratorNavbar";
import imgbanner from "../images/02.banner 1/imgBanner.jpg";
import Footer from "../components/Footer";


require("typeface-poppins");
require("typeface-rubik");

function Administrator() {
  return (
    <>
      <div className="flex justify-center items-center">
        <div className="w-341.5 ">
          <header className="sticky top-0 z-50  bg-white">
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
                    Bienvenido Administrador
                  </h1>
                  <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                    { 
                    //******ACAAAAAAAAAAAAAAAAAAA FALTAAAAAAAAAAAAAAA COLOCAR EL NOMBRE DE LA PERSONA OTRA VEZ*****
                    }
                  </h1>
                </div>
              </div>
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
export default Administrator;
