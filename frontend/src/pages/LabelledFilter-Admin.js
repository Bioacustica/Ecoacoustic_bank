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
  const userRole = localStorage.getItem("rolename");

  return (
    <>
      <header className="sticky top-0 z-30 bg-white">
        <Head />
        <AdministratorNavbar />
      </header>

      <main>
        <div className="flex justify-center items-center ">
          <div>
            <img src={imgbanner} alt="" />
          </div>
          <div className="absolute self-center justify-center ">
            <div className="space-y-3">
              <h1 className="text-center font-extrabold font-poppins text-4.5xl text-white">
                {userRole},
              </h1>
              <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                Queries
              </h1>
            </div>
          </div>
        </div>

        <div className="flex justify-center divide-x divide-black divide-x-12.25 h-20.25 bg-blue-250 items-center">
          <div className="">
            {/* <Link to="/admin-label-filter"> */}
              <div className="text-center text-blue-850 text-xl w-full">
                <label> AUDIO QUERY </label>
                  <br />
                <label> TO DOWNLOAD </label>
              </div>
            {/* </Link> */}
          </div>
          {/* <div className="hover:bg-blue-200 w-4/12">
            <Link to="/admin-assignment-filter">
              <button className="text-white text-xl w-full">
                <label> FILTRO ASIGNACIÓN </label>
                <br />
                <label> DE AUDIOS PÚBLICOS </label>
              </button>
            </Link>
          </div>

          <div className="hover:bg-blue-200 w-4/12 ">
            <Link to="/admin-dowload-filter">
              <button className="text-white text-xl w-full">
                <label> FILTRO DESCARGA </label>
                <br />
                <label> DE AUDIOS </label>
              </button>
            </Link>
          </div> */}
        </div>
        <div className="mt-16">
          <PrivateLabel />
        </div>
      </main>

      <Footer />
    </>
  );
}

export default LabelledFilter;
