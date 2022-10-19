import React, { useState } from "react"

function AdministratorNavbar() {
  return (
    <div className="">
      <nav className="bg-green-450 flex  h-11 w-341.5 justify-center items-center">
        <a
          href="/"
          className="text-white ml-26.25 mr-26.25 content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
                    
        >
          INICIO
        </a>
        <a
          href="#"
          className="text-white mr-26.25  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          SUBIR AUDIOS
        </a>
        <a
          href="/admin-label-filter"
          className="text-white mr-26.25  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          FILTROS
        </a>
        <a
          href="/user-panel"
          className="text-white mr-26.25  content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          USUARIOS
        </a>
        <a
          href="#"
          className="text-white mr-26.25 content-center hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          MAPA
        </a>
        <a
          href="#"
          className="text-white content-center mr-26.25 hover:text-white
          hover:text-whithe border-b-2 border-green-450
          hover:border-b-2 hover:border-white"
        >
          VISUALIZACIÓN DE METADATOS
        </a>
        
      </nav>


    </div>

  )
}

export default AdministratorNavbar