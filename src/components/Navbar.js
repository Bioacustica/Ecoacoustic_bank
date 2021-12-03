import React, {useState}from "react"
import ContactModal from "./ContactModal";

require("typeface-poppins");
require("typeface-rubik");
function Navbar(){
    
  const [showModal, setShowModal] = useState(false)

  const openModal=()=>setShowModal(true)

  const closeModal=()=>setShowModal(false)

  
      return (
        <div className="">
             <nav className="bg-green-450 flex  h-11 w-341.5 justify-center items-center">
        <a
          href="/"
          className="text-white ml-26.75 mr-26.5 content-center font-poppins   hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          INICIO
        </a>
        <a
          href="/#sobre-nosotros"
          className=" mr-26.5   font-poppins text-white  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white "
        >
          SOBRE NOSOTROS
        </a>
        <a
      
          href="/#visualizacion"
          className=" mr-26.5  font-poppins text-white  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          VISUALIZACIÓN
        </a>
        <a
          href="/#filtros"
          className=" mr-26.5  font-poppins text-white  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          FILTROS
        </a>
        <button
          href="#"
          className=" mr-26.5 font-poppins text-white  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
          onClick={openModal}
        >
          CONTACTO
        </button>
        <a
          href="/log-in"
          className=" mr-26.75 font-poppins text-white   content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white "
        >
          INICIAR SESIÓN
        </a>
      </nav>

      {showModal && <ContactModal close={closeModal}/>}
        </div>
       
      )
    }

export default Navbar