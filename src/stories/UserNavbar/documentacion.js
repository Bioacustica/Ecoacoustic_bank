// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl justify-center text-blue-500'>
      <h1 >Barra de navegacion publica</h1>
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
        Este componente hace referencia a la barra del usuario publico, contando con 5 opciones para navegar a diferentes funcionalidades propias de su pestaña y ademas, poder iniciar sesion.
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
     href="#filtros"
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
  
    `}
</code>

}</pre>
    </div>
  );
  
}

