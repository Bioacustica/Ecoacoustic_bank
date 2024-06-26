import React from "react";
import closeimg from "../images/06.Contacto/x.png";

require("typeface-poppins");
require("typeface-rubik");

function EditModal({ close }) {
  return (
    <>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-auto my-6 mx-auto max-w-3xl">
          <div className="flex justify-center items-center">
            <div className="bg-white justify-center w-263.75 h-91">
              <div className="justify-center items-center">
                <div className="flex w-263.75 justify-end items-end ">
                  <button
                    onClick={close}
                    className=" rounded-md p-4 inline-flex justify-end items-end hover:text-gray-500 hover:bg-blue-100 focus:outline-none focus:shadow-lg"
                  >
                    <img className="" src={closeimg} alt="" />
                  </button>
                </div>

                <div className="justify-center text-center  z-30 mt-1 mb-11.75">
                  <h1 className="font-extrabold text-4xl text-blue-850">
                    Editar
                  </h1>
                </div>
                <div className="flex ml-34.75 mr-34.75 w-194.25 border overflow-x-auto">
                  <table className="text-center">
                    <tr className="h-4">
                      <td className="border-solid border-2 border-black px-4 py-2">
                        <h1>ID</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Nombre</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Fecha</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Habitat</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Municipio</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Ciudad</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Elevación</h1>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <h1>Evento</h1>
                      </td>
                      <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                        Formato
                      </td>
                      <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                        Tipo de microfono
                      </td>
                      <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                        Metodo de etiquetado
                      </td>
                      <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                        Tipo de grabadora
                      </td>
                      <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                        Software de etiquetado
                      </td>
                      <td className="border-2 font-rubik border-blue-850 text-base h-12.75 px-4 text-center">
                        Tipo de case
                      </td>
                    </tr>
                    <tr className="h-10">
                      <td className="border-solid border-2 border-black px-4"></td>
                      <td className="border-solid border-2 border-black ">
                        <input
                          className="w-20 "
                          value="Nombre1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Fecha1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Habitat1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Municipio1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Ciudad1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Elevacion1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Evento1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Formato1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Tipo de microfono1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Metodo de etiquetado1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Tipo de grabadora1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Software de etiquetado1"
                          type="text"
                        ></input>
                      </td>
                      <td className="border-solid border-2 border-black px-4">
                        <input
                          className="w-20"
                          value="Tipo de case"
                          type="text"
                        ></input>
                      </td>
                    </tr>
                  </table>
                </div>
                <div className="flex justify-center items-center mt-6 mb-10.5">
                  <div className="mr-3">
                    <button className="bg-blue-850 text-white font-semibold px-4 text-xl h-8">
                      Cancelar
                    </button>
                  </div>
                  <div>
                    <button className="bg-gray-250 h-8 text-white font-semibold px-4 text-xl">
                      Guardar
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
    </>
  );
}
export default EditModal;
