import React from "react";
import closeimg from "../images/06.Contacto/x.png";

function AddUser({ close }) {
  return (
    <>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-auto my-6 mx-auto max-w-3xl">
          <div className="flex justify-center items-center">
            <div className="bg-yellow-550 justify-center w-263.75 h-119.5">
              <div className="justify-center items-center">
                <div className="flex w-263.75 justify-end items-end ">
                  <button
                    onClick={close}
                    className=" rounded-md px-4 py-2 inline-flex justify-end items-end hover:text-gray-500 hover:shadow-2xl focus:outline-none focus:shadow-lg"
                  >
                    <img className="" src={closeimg} alt="" />
                  </button>
                </div>
                <div className="justify-center text-center font-poppins font-extrabold text-4xl text-blue-850 mb-11">
                  <h1>Agregar usuario</h1>
                </div>

                <form>
                  <div className="flex justify-center items-end ">
                    <div className="">
                      <div>
                        <div className="items-center inline-flex justify-end w-full ">
                        <label className="font-poppins font-bold text-blue-850 text-2xl mr-2">
                          Nombre:{" "}
                        </label>
                        <input
                          name="subject"
                          type="text"
                        
                    
                          required
                          className="placeholder-blue-850 bg-white text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-white border-opacity-100 "
                        />
                        </div>
                        
                      </div>

                      <div className="items-center inline-flex justify-end w-full ">
                      <label className="font-poppins text-center font-bold text-blue-850 mt-2 text-2xl mr-2">
                        Mail:{" "}
                      </label>
                      <input
                        type="email"
                        required
                      
                     
                        className="mt-4 w-171.25 text-xl  h-12.5 placeholder-blue-850 text-center bg-white font-rubik"
                      ></input>
                      </div>

                      <div className="items-center justify-end flex">
                      <label className="font-poppins font-bold text-blue-850 text-2xl mr-2">
                          Rol:{" "}
                        </label>
                      <select className="block w-171.25 h-12.25 font-rubik text-xl text-center mt-4 bg-white border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                      <option className="font-rubik text-xl text-center">Seleccionar</option>
                        <option className="font-rubik text-xl text-center">Administrador</option>
                        <option className="font-rubik text-xl text-center">Colaborador de registros</option>
                        <option className="font-rubik text-xl text-center">Colaborador de etiquetado</option>
                        <option className="font-rubik text-xl text-center">Usuario</option>
                      </select>
                      </div>
                     
                     <div className="items-center inline-flex justify-end w-full ">
                     <label className="font-poppins text-center font-bold text-blue-850 text-2xl mr-2">
                          Contraseña:{" "}
                        </label>
                     <input
                        type="password"
                      
                        required
                        className="mt-4 w-171.25 text-center h-12.5 placeholder-blue-850 bg-white font-rubik"
                      ></input>
                     </div>
                     
                    </div>
                  </div>
                  <div className="justify-center items-center ">
                    <div className="flex justify-center items-center ml-89.5 mr-89.5 mt-8.75">
                      <button
                        type="submit"
                        className=" bg-blue-850 mr-4 text-white font-semibold text-2xl hover:shadow-2xl font-poppins h-10 w-40  "
                      >
                        Cancelar
                      </button>
                      <button
                        type="submit"
                        className=" bg-gray-250 text-white font-semibold text-2xl hover:shadow-2xl font-poppins h-10 w-40"
                      >
                        Guardar
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
    </>
  );
}
export default AddUser;
