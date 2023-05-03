import React from "react";
import Head from "../components/Head";
import AdministratorNavbar from "../components/AdministratorNavbar";
import imgbanner from "../images/02.banner 1/imgBanner.jpg";
import Footer from "../components/Footer";

require("typeface-poppins");
require("typeface-rubik");

function Administrator() {
  const userRole = localStorage.getItem("rolename");

  return (
    <>
      <header className="sticky top-0 z-50  bg-white">
        <Head />
        <AdministratorNavbar />
      </header>

      <main className="w-full">
        <div className="flex justify-center items-center ">
          <div className="flex">
            <img src={imgbanner} alt="" />
          </div>
          <div className="absolute self-center justify-center ">
            <div className="space-y-3">
              <h1 className="text-center font-extrabold font-poppins text-4.5xl text-white">
                Bienvenido {userRole}
              </h1>
              <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                {
                  //******ACAAAAAAAAAAAAAAAAAAA FALTAAAAAAAAAAAAAAA COLOCAR EL NOMBRE DE LA PERSONA OTRA VEZ*****
                }
              </h1>
            </div>
          </div>
        </div>
      </main>

      <Footer />
    </>
  );
}
<script type="text/javascript">
  window.history.forward(); function noBack() {window.history.forward()}
</script>;
export default Administrator;
