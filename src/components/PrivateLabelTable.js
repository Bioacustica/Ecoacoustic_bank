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
                Habitat
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
                Elevacion
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Evento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Formato
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Tipo de microfono
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Metodo de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Tipo de grabadora
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Software de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Tipo de case
              </td>
            </tr>
          </thead>

          <tbody>
            {columns.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato1
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato2
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato3
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato4
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato5
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato6
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato7
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato8
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato9
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato10
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato11
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato12
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato13
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato14
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  Dato15
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
              <tr>
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
