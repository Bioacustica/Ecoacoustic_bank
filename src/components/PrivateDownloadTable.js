import React ,{useState}from "react";
import MoreInformationModal from "./MoreInformationModal";

require("typeface-poppins");
require("typeface-rubik");
function PrivateDownloadTable() {
  const columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const [showModal, setShowModal] = useState(false)

  const openModal=()=>setShowModal(true)

  const closeModal=()=>setShowModal(false)

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
          <thead className="h-11.25">
            <tr className="h-11.25">
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Nombre
              </td>
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 text-center">
                Fecha
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Hábitat
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Departamento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Municipio
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Ciudad
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Elevación
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Evento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Formato
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Tipo de micrófono
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Método de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Tipo de grabadora
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Software de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Tipo de carcasa
              </td>
            </tr>
          </thead>

          <tbody>
            {columns.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="ml-8">
        <table>
          <thead>
            <tr className="">
              <td className=" font-rubik font-semibold text-base h-20 text-center w-28 ">
                <button className="bg-blue-250 font-semibold text-white p-1 w-full">Seleccionar todo</button>
              </td>
            </tr>
          </thead>
          <tbody>
            {columns.map((rowscounter) => (
              <tr>
                <td className=" flex font-rubik font-light text-base h-13.5 w-39.5 ">
                  <button onClick={openModal}
                  className=" bg-yellow-400 font-semibold text-white text-lg w-31.25 h-7.75">
                    Más
                  </button>
                  <input className="w-7.75 h-7.75 ml-2 text-white "  type="checkbox"/>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {showModal && <MoreInformationModal className="z-50" close={closeModal}/>}
      </div>
      
    </div>
    
  );
}

export default PrivateDownloadTable;
