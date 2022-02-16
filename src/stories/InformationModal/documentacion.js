// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 
  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl justify-center text-blue-500'>
      <h1 >Modal de mas informacion</h1>
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
        Este componente hace referencia al modal mostrado en cada filtro de audios, el cual contendra informacion adicional a la presentada en cada tabla de audios.
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
        <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto 
        fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-auto my-6 mx-auto max-w-3xl">
        
        <div className="flex justify-center items-center"> 

          <div className="bg-white justify-center w-263.75 h-150">

            <div className="justify-center items-center">
              <div className="flex w-263.75 justify-end items-end ">
                <button 
                onClick={close} className=" rounded-md p-1 inline-flex justify-end items-end 
                hover:text-gray-500 hover:bg-blue-100 focus:outline-none focus:shadow-lg">
                <img className="" src={closeimg} alt="" />
                </button>
              </div>

              <div className="justify-center text-center font-poppins font-extrabold text-5xl  mb-7 ">
                <h1>Más</h1>
              </div>

              <div className="ml-10.5 mr-10.5 w-241.75 justify-center items-center">
              <div className="flex h-36 ">
                <div className=" flex w-75.5 border border-black justify-center items-center">
                  <h1 className="text-center font-rubik font-bold text-3xl ">Lorem ipsum</h1>
                </div>
              <div className="w-166.25 border p-2 border-black">Lorem ipsum dolor sit amet,
               consectetur 
              adipiscing elit. Fusce eget lectus tempor nisl luctus facilisis ut vel leo. 
              Vivamus nisi arcu,
               molestie non suscipit nec, mattis vitae justo. Nullam luctus odio ac velit 
               cursus, 
               at hendrerit justo faucibus. Suspendisse quis eros lobortis lacus congue 
               vulputate. 
               Curabitur varius augue quis ex lacinia, sit amet fringilla quam varius. 
               Curabitur imperdiet 
               enim ut tortor tristique, vitae congue sapien imperdiet. </div>
              </div>

              <div className="flex h-36 mt-2">
                <div className=" flex w-75.5 border border-black justify-center items-center">
                  <h1 className="text-center font-rubik font-bold text-3xl ">Lorem ipsum</h1>
                </div>
              <div className="w-166.25 border p-2 border-black">Lorem ipsum dolor sit amet, 
              consectetur 
              adipiscing elit. Fusce eget lectus tempor nisl luctus facilisis ut vel leo. 
              Vivamus nisi arcu, 
              molestie non suscipit nec, mattis vitae justo. Nullam luctus odio ac velit c
              ursus, at hendrerit 
              justo faucibus. Suspendisse quis eros lobortis lacus congue vulputate. 
              Curabitur varius augue 
              quis ex lacinia, sit amet fringilla quam varius. Curabitur imperdiet 
              enim ut tortor tristique, 
              vitae congue sapien imperdiet. </div>
              </div>

              <div className="flex h-36 mt-2 ">
                <div className=" flex w-75.5 border border-black justify-center items-center">
                  <h1 className="text-center font-rubik font-bold text-3xl ">Lorem ipsum</h1>
                </div>
              <div className="w-166.25 border p-2 border-black">Lorem ipsum dolor sit amet, 
              consectetur 
              adipiscing elit. Fusce eget lectus tempor nisl luctus facilisis ut vel leo. 
              Vivamus nisi arcu, 
              molestie non suscipit nec, mattis vitae justo. Nullam luctus odio ac velit
               cursus, at hendrerit 
              justo faucibus. Suspendisse quis eros lobortis lacus congue vulputate. 
              Curabitur varius augue 
              quis ex lacinia, sit amet fringilla quam varius. Curabitur imperdiet enim 
              ut tortor tristique, 
              vitae congue sapien imperdiet. </div>
              </div>
             
              </div>
              
            </div>
          </div>
          </div>
        </div>
      </div>
      <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
    `}
</code>

}</pre>
    </div>
  );
  
}

