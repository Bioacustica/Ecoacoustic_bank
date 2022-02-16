// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl justify-center text-blue-500'>
      <h1 >Tabla de usuarios</h1>
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
        Este componente hace referencia a la tabla de usuarios mostrada en el panel de usuarios que tiene el rol de administrador.
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
        <div className="flex items-center justify-center ">
      <div className=" overflow-x-auto w-193.5">
        <table className=" border-2 border-collapse border-blue-850">
          <thead>
            <tr className="">
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 
              text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850 w-46.75 text-base h-11.25  
              text-center">
                Nombre
              </td>
              <td className="border-2 font-rubik border-blue-850 w-80.25 text-base h-11.25 
              text-center">
                Email
              </td>
              <td className="border-2 font-rubik border-blue-850  w-48.5 text-base h-11.25 
               text-center">
                Rol
              </td>
            </tr>
          </thead>

          <tbody>
            {columns.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5
                 px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5
                 px-4 text-center" >
                  Administrador
                </td>
              </tr>
            ))}
             {columns2.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5
                 px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center" >
                  Colaborador de registros
                </td>
              </tr>
            ))}
             {columns5.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5
                px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center" >
                  Colaborador de etiquetado
                </td>
              </tr>
            ))}
            {columns3.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 
                px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5
                 px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5
                 px-4 text-center" >
                  Usuario
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="ml-8 items-center justify-center">
        <table>
          <thead>
            <tr className="">
              <td className=" font-rubik font-semibold text-base h-16 px-4 text-center"></td>
            </tr>
          </thead>
          <tbody>
            {columns4.map((rowscounter) => (
              <tr>
                <td className="font-rubik font-light text-base h-13.5 ">
                  <button
                  onClick={openModal} 
                  className=" bg-yellow-400 font-semibold text-white  w-31.25 h-7.75">
                  Modificar
                  </button>
                </td>
                <td className="font-rubik font-light text-base h-13.5 ">
                  <button className=" bg-blue-850 ml-2 font-semibold text-white  w-31.25 h-7.75">
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {showModal && <ModifyModal className="z-50" close={closeModal}/>}
      </div>
    </div>
    `}
</code>

}</pre>
    </div>
  );
  
}

