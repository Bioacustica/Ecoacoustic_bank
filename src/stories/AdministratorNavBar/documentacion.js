// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl  justify-center text-blue-500'>
      <h1 >Barra de navegacion del administrador</h1>
      </div>
      <br/>
      <code>
        Autor: Alejandro Piedrahita Carvajal
      </code>
      <br/>
      <hr/>
      <br/>
      <h3 className='font-bold'>Descripcion</h3>
      <div className='flex items-center justify-start'>
      <p>
        Este componente hace referencia a la barra del administrador, contando con 5 opciones para navegar a diferentes funcionalidades propias de su panel.
      </p>
      </div>
      
      <br/>
      <h3 className='font-bold'>Funciones</h3>
      <p>
       No cuenta con ninguna funcion
      </p>
      <br/>
      <h3 className='font-bold'>Variables</h3>
      <p>
       No cuenta con ninguna variable de entrada o salida
      </p>
      <br/>
      <h3 className='font-bold'>Codigo</h3>
      <br/>

      
      <pre  className='border-2'>{
        <code className='w-139 h- justify-center'>{
        `
        <div className="">
      <nav className="bg-green-450 flex h-11 w-341.5 justify-center items-center">
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
    `}
</code>

}</pre>
    </div>
  );
  
}

