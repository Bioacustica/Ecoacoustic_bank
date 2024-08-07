import React,{useState} from "react";
import EditModal from "./EditModal";
import MoreInformationModal from "./MoreInformationModal"

require("typeface-poppins");
require("typeface-rubik");
function PrivateLabelTable({List_Audio}) {
  const {results} = List_Audio
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
      <div className="border overflow-x-auto w-full">
        <table className=" border border-collapse ">
          <thead>
            <tr className="">
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Fingerprint
              </td>
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 text-center">
                Date
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Habitat
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Department
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Municipality
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Country
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Elevation
              </td>
              {/* <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Evento
              </td> */}
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Format
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Microphone
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Evidence
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Hardware
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Software
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Case
              </td>
              <td colSpan={1} className="sticky right-0 bg-white border-2 font-rubik border-blue-850  text-base h-11.25 px-4 text-center">
                Actions
              </td>
            </tr>
          </thead>
          <tbody>
            {(results || []).map((rowscounter) => (
              <tr className="" key={rowscounter.id_record}>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.id_record}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.fingerprint_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.date_record_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.habitat_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.departamento_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.ciudad_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.ciudad_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.elevation}
                </td>
                {/* <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.id_record}
                </td> */}
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.formato_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.microphone}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.metodo_etiquetado_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.tipo_grabadora_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.software_etiquetado_}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                {rowscounter.case_}
                </td>
                {/* <td className="sticky right-40 bg-white border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
                  <button 
                    onClick={openModal2}className=" bg-yellow-400 font-semibold text-lg text-white  w-31.25 h-7.75">
                    Más
                  </button>
                </td> */}
                <td className="sticky right-0 bg-white border-2 font-rubik border-blue-850 font-light text-base h-13.5 px-4 text-center">
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
      </div>

      <div className="ml-8">
        {showModal && <EditModal className="z-50" close={closeModal}/>}
        {showModal2 && <MoreInformationModal className="z-50" close={closeModal2}/>}
      </div>
    </div>
  );
}

export default PrivateLabelTable;
