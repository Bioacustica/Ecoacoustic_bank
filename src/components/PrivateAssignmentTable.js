import React from "react";

require("typeface-poppins");
require("typeface-rubik");
function PrivateAssignmentTable() {
  const columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

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
    <div className="flex items-center justify-center ">
      <div className="border overflow-x-auto w-212.5">
        <table className=" border border-collapse ">
          <thead>
            <tr className="">
              <td className="border font-rubik text-base h-11.25 px-4 text-center">
                Id
              </td>
              <td className="border font-rubik  text-base h-11.25 px-4 text-center">
                Nombre
              </td>
              <td className="border-2 font-rubik text-base h-11.25 px-4 text-center">
                Fecha
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Habitat
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Departamento
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Municipio
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Ciudad
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Elevacion
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Evento
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Formato
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Tipo de microfono
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Metodo de etiquetado
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Tipo de grabadora
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Software de etiquetado
              </td>
              <td className="border-2 font-rubik  text-base h-11.25 px-4 text-center">
                Tipo de case
              </td>
            </tr>
          </thead>

          <tbody>
            {columns.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato1
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato2
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato3
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato4
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato5
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato6
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato7
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato8
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato9
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato10
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato11
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato12
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato13
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato14
                </td>
                <td className="border-2 font-rubik font-light text-base h-13.5 px-4 text-center">
                  Dato15
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="ml-3">
        <table>
          <thead>
            <tr className="">
              <td className=" font-rubik font-semibold text-base h-20 px-4 text-center"></td>
            </tr>
          </thead>
          <tbody>
            {columns.map((rowscounter) => (
              <tr>
                <td className="font-rubik font-light text-base h-13.5 ml-1 px-3">
                  <button className=" bg-yellow-400  w-31.25 h-7.75">
                    Mas
                  </button>
                </td>
                <td className="font-rubik font-light text-base h-13.5 ">
                <input className="w-7.75 h-7.75 mt-2 text-blue-850 " type="checkbox"/>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default PrivateAssignmentTable;
