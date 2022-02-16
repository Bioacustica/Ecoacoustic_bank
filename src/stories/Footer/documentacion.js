// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl  justify-center text-blue-500'>
      <h1 >Footer</h1>
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
        Este componente hace referencia a la barra inferior de cada pagina (Footer) donde se muestra los logotipos de las instituciones participantes en el apoyo y creacion del proyecto.
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
        <div className=" flex bg-white w-341.5   h-25 mb-4">
        <div className="h-15 ml-3.75 bg-gray-600 mr-10.5 w-23.75 ">
            <h1>Logo Principal</h1>
        </div>
        <div className="h-10.5 justify-center mr-10.5 w-23.75">
            <img src={itm} alt=""/>
        </div>
        <div className="h-10.5 mr-10.5 w-42 justify-center ">
            <img src={udea} alt=""/>
        </div>
        <div className="h-10.5 mr-10.5 w-10.5 justify-center ">
        <img src={humboldt} alt=""/>
        </div>
        <div className="h-12 mr-10.5 w-38.75 w-27.5 justify-center">
        <img src={sistemic} alt=""/>
        </div>
        <div className="h-10.5 mr-10.5 w-20.75 justify-center">
        <img src={gha} alt=""/>
        </div>

        <label className=" ml-64 font-semibold text-xl mr-3">
          Apoya:</label>
        <div className=" h-11 mr-3.75 w-59.75">
        <img src={minciencias} alt=""/>
        </div>
        </div>
    `}
</code>

}</pre>
    </div>
  );
  
}

