import React, {useState} from "react";
import Head from "../components/Head";
import AdministratorNavbar from "../components/AdministratorNavbar";
import imgbanner from "../images/02.banner 1/imgBanner.jpg";
import Footer from "../components/Footer";
import UserTable from "../components/UserTable";
import AddUser from "../components/AddUser";

require("typeface-poppins");
require("typeface-rubik");

function UserPanel() {
  const [showModal, setShowModal] = useState(false)

  const openModal=()=>setShowModal(true)

  const closeModal=()=>setShowModal(false)
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
                    Usuarios
                  </h1>
                </div>
              </div>
            </div>

            <div className="flex justify-center items-center mt-5 mb-3 ">
                <button 
                onClick={openModal}
                className="w-87.75 bg-blue-250 text-white h-10.75 font-semibold text-2xl font-poppins">
                    Agregar usuario
                </button>
            </div>

            <div className="h-full">
            <UserTable/>
            </div>
            
            {showModal && <AddUser className="z-50" close={closeModal}/>}
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
export default UserPanel;