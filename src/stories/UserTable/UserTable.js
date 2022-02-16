import React,{useState} from "react";
//import ModifyModal from "./ModifyModal";
//import MoreInformationModal from "./MoreInformationModal";

require("typeface-poppins");
require("typeface-rubik");
function UserTable() {
  const columns = [1, 2];
  const columns2 = [3, 4];
  const columns5 = [5, 6];
  const columns3 = [7, 8, 9, 10];
  const columns4=[1,2,3,4,5,6,7,8,9,10]
  const [showModal, setShowModal] = useState(false)

  const openModal=()=>setShowModal(true)

  const closeModal=()=>setShowModal(false)


  return (
    <div className="flex items-center justify-center ">
      <div className=" overflow-x-auto w-193.5">
        <table className=" border-2 border-collapse border-blue-850">
          <thead>
            <tr className="">
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850 w-46.75 text-base h-11.25  text-center">
                Nombre
              </td>
              <td className="border-2 font-rubik border-blue-850 w-80.25 text-base h-11.25 text-center">
                Email
              </td>
              <td className="border-2 font-rubik border-blue-850  w-48.5 text-base h-11.25  text-center">
                Rol
              </td>
            </tr>
          </thead>

          <tbody>
            {columns.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center" >
                  Administrador
                </td>
              </tr>
            ))}
             {columns2.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center" >
                  Colaborador de registros
                </td>
              </tr>
            ))}
             {columns5.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center" >
                  Colaborador de etiquetado
                </td>
              </tr>
            ))}
            {columns3.map((rowscounter) => (
              <tr className="">
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Id{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  Usuario{rowscounter}@gmail.com
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center" >
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
  );
}

export default UserTable;
