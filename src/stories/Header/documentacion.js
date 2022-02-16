// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl  justify-center text-blue-500'>
      <h1 >Header</h1>
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
        Este componente hace referencia a la barra superior de cada pagina, donde se mostrara el logotipo de cada institucion participante en el proyecto.
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
        <div className="flex bg-white items-center w-341.5 mt-8.75 h-16 justify-center mb-8.75">
        <div className="ml-68.25 mr-17.5 h-16 w-36.75 bg-gray-500">    
          <h1>Logo principal</h1>
        </div>
        <div className="h-16 mr-17.5 w-36.75">
            <img src={imagesHead.img2} alt=""/>
        </div>
        <div className="h-16 mr-17.5 w-63.5 ">
        <img src={imagesHead.img1} alt=""/>
        </div>
        <div className="h-16 mr-68.25 w-15 ">
        <img src={imagesHead.img3} alt=""/>
        </div>
      </div>
    `}
</code>

}</pre>
    </div>
  );
  
}

