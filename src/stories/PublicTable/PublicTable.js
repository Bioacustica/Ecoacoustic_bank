import React, {useState}  from "react";
//import MoreInformationModal from "./MoreInformationModal";

require("typeface-poppins");
require("typeface-rubik");
function PublicTable() {
  const columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const [showModal, setShowModal] = useState(false)

  const openModal=()=>setShowModal(true)

  const closeModal=()=>setShowModal(false)


  return (
    <div className="flex">
      <div className="  border overflow-x-auto">
        <table className=" border border-collapse">
          <thead>
            <tr className="">
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Nombre
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Fecha
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Hábitat
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Departamento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Municipio
              </td>
              <td className="border-2 font-rubik border-blue-850 text-base h-12.75 px-4 text-center">
                Ciudad
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Elevación
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Evento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Formato
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Tipo de micrófono
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Método de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Tipo de grabadora
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Software de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850 text-base h-12.75 px-4 text-center">
                Tipo de carcasa
              </td>
            </tr>
          </thead>

          <tbody>
            {columns.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  Dato_Audio{rowscounter}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
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
              <td className=" font-rubik font-semibold text-base h-14 px-4 text-center"></td>
            </tr>
          </thead>
          <tbody>
            {columns.map((rowscounter) => (
              <tr>
                <td className="font-rubik font-light text-base h-12.75 ml-4">
                  <button 
                  onClick={openModal}
                  className=" bg-yellow-400 font-semibold text-xl text-white  w-31.25">
                    Más
                  </button>
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

export default PublicTable;