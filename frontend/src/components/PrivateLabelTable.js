import React,{useState} from "react";
import EditModal from "./EditModal";
import MoreInformationModal from "./MoreInformationModal"

require("typeface-poppins");
require("typeface-rubik");
function PrivateLabelTable() {
  const columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  const [showModal, setShowModal] = useState(false)
  const [showModal2, setShowModal2] = useState(false)

  const openModal=()=>setShowModal(true)
  const openModal2=()=>setShowModal2(true)

  const closeModal=()=>setShowModal(false)
  const closeModal2=()=>setShowModal2(false)

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
      <div className="border overflow-x-auto w-193.5">
        <table className=" border border-collapse ">
          <thead>
            <tr className="">
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
              <tr className="" key={rowscounter}>
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
              <td className=" font-rubik font-semibold text-base h-20 px-4 text-center"></td>
            </tr>
          </thead>
          <tbody>
            {columns.map((rowscounter) => (
              <tr key={rowscounter}>
                <td className="font-rubik font-light text-base h-13.5 ">
                  <button 
                  onClick={openModal2}className=" bg-yellow-400 font-semibold text-lg text-white  w-31.25 h-7.75">
                  Más
                  </button>
                </td>
                <td className="font-rubik font-light text-base h-13.5 ">
                  <button
                  onClick={openModal}
                  className=" bg-blue-250 ml-2 font-semibold text-white text-lg w-31.25 h-7.75">
                    Editar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {showModal && <EditModal className="z-50" close={closeModal}/>}
        {showModal2 && <MoreInformationModal className="z-50" close={closeModal2}/>}
      </div>
    </div>
  );
}

export default PrivateLabelTable;
