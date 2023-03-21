import React, { useState } from "react";

function LoadingModal() {
    return(

        <>
        <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
          <div className="relative w-41.5 h-41.5 my-6 mx-auto max-w-3xl">
            {/*content*/}
            <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full h-full bg-white outline-none justify-center items-center focus:outline-none">
            <div className="flex justify-center items-center space-x-1 text-sm text-gray-700">
             
             <svg fill='none' className="w-12 h-12 animate-spin" viewBox="0 0 32 32" xmlns='http://www.w3.org/2000/svg'>
                 <path clipRule='evenodd'
                     d='M15.165 8.53a.5.5 0 01-.404.58A7 7 0 1023 16a.5.5 0 011 0 8 8 0 11-9.416-7.874.5.5 0 01.58.404z'
                     fill='currentColor' fillRule='evenodd' />
             </svg>
    
      
     <div>Cargando ...</div>
    </div>
            </div>  
          </div>
        </div>

        <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
      </>

    )
}
export default LoadingModal;
