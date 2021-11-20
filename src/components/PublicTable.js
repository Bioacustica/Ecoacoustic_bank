import React from "react"


require("typeface-poppins");
require("typeface-rubik");
function PublicTable(){

const columns=[1,2,3,4,5,6,7,8,9,10];

/* 
-Id
-Nombre
-Fecha
-Habitat
-Municipio
-Ciudad
-Elevacion
-Evento
-Formato
-Tipo de microfono
-Metodo de etiquetado
-Tipo de grabadora
-Software de etiquetado
-Tipo de case
-Sampling Description *********** OJO CON ESTE ***********
*/



      return (
        <div className=" w-screen border">
            <table className=" border border-collapse">    
                <thead>
                <tr className="">
                <td className="border font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Id
                  </td>
                  <td className="border font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Nombre
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Fecha
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Habitat
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Municipio
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Ciudad
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Elevacion
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Evento
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Formato
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Tipo de microfono
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Metodo de etiquetado
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Tipo de grabadora
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Software de etiquetado
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base h-12.75 px-4 text-center">
                      Tipo de case
                  </td>
                  <td className="border-2 font-rubik font-semibold text-base text-center ">
                      Mas
                  </td>
                </tr>
                </thead>

                <tbody>

            
                {columns.map((rowscounter) =>
                <tr className="">
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola1
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola2
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola3
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola4
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola5fddddddddddddddddddddddddddddddddd
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola6
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola7
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola8
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola9
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola10
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola11
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola12
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola13
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4 text-center">
                    Hola14
                </td>
                <td className="border-2 font-rubik font-light text-base h-12.75 px-4">
                    <button className=" bg-yellow-400 rounded-lg w-18.5">
                        Mas
                    </button>
                </td>
                </tr>     
      )}
                </tbody>

            </table>
        </div>
       
      )
    }

export default PublicTable