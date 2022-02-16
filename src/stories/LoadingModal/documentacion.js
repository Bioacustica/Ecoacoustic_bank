// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl  justify-center text-blue-500'>
      <h1 >Modal de carga</h1>
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
        Este componente hace referencia al modal de carga utilziado mientras se hace la solicitud de login a la API del proyecto.
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
        <>
        <div className="justify-center items-center flex overflow-x-hidden 
        overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
          <div className="relative w-41.5 h-41.5 my-6 mx-auto max-w-3xl">
            {/*content*/}
            <div className="border-0 rounded-lg shadow-lg relative flex flex-col
             w-full h-full bg-white outline-none justify-center items-center 
             focus:outline-none">
            <div className="flex justify-center items-center space-x-1 text-sm 
            text-gray-700">
             
             <svg fill='none' className="w-12 h-12 animate-spin" viewBox="0 0 32 32" 
             xmlns='http://www.w3.org/2000/svg'>
                 <path clipRule='evenodd'
                     d='M15.165 8.53a.5.5 0 01-.404.58A7 7 0 1023 16a.5.5 0 011 0 8 8 
                     0 11-9.416-7.874.5.5 0 01.58.404z'
                     fill='currentColor' fillRule='evenodd' />
             </svg>
    
      
     <div>Cargando ...</div>
    </div>
            </div>  
          </div>
        </div>

        <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
      </>

    `}
</code>

}</pre>
    </div>
  );
  
}

