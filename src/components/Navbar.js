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
             <nav className="bg-green-450 flex text- h-11 w-341.5 justify-center items-center">
        <a
          href="/"
          className="text-white ml-26.75 mr-26.5 content-center font-poppins hover:text-green-900"
        >
          INICIO
        </a>
        <a
          href="/#sobre-nosotros"
          className="text-white mr-26.5  content-center font-poppins hover:text-green-900"
        >
          SOBRE NOSOTROS
        </a>
        <a
      
          href="/#visualizacion"
          className="text-white mr-26.5  content-center font-poppins hover:text-green-900"
        >
          VISUALIZACIÓN
        </a>
        <a
          href="/#filtros"
          className="text-white mr-26.5  content-center font-poppins hover:text-green-900"
        >
          FILTROS
        </a>
        <button
          href="#"
          className="text-white mr-26.5   content-center font-poppins hover:text-green-900"
          onClick={openModal}
        >
          CONTACTO
        </button>
        <a
          href="/login"
          className="text-white content-center mr-26.75 font-poppins hover:text-green-900"
        >
          INICIAR SESIÓN
        </a>
      </nav>

      {showModal && <ContactModal close={closeModal}/>}
        </div>
       
      )
    }

export default Navbar