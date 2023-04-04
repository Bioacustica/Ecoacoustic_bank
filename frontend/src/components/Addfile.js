import React, { useState } from "react";
import { uploadMasterTableData } from "../services/loadFile";
import closeimg from "../images/06.Contacto/x.png";
import Toggle from "react-toggle";
import LoadingModal from "./LoadingModal";

import "react-toggle/style.css";
function AddFile({ close }) {
  const [isLoading, setLoading] = useState(false);
  const [archivosT, setArchivosT] = useState(null);
  const [toggleUDAS, setToggleUDAS] = useState(false);
  const [okArchivosT, setOkArchivosT] = useState(false);
  const [archivosU, setArchivosU] = useState(null);

  const subirArchivosT = (e) => {
    setArchivosT(e?.[0] || null);
  };

  const subirArchivosU = (u) => {
    setArchivosU(u);
    console.log(u);
  };

  const sendFiles = async (e) => {
    e.preventDefault();
    setLoading(true);
    let okFileT = false;
    try {
      if (archivosT) {
        await uploadMasterTableData(archivosT);
        okFileT = true;
      }
    } catch (error) {}
    setLoading(false);
    setOkArchivosT(okFileT);
  };

  return (
    <>
      <div className="fixed inset-0 z-40 bg-black opacity-25"></div>

      <div className="fixed inset-0 z-50 flex items-center justify-center overflow-x-hidden overflow-y-auto outline-none focus:outline-none">
        <div className="relative w-auto max-w-3xl mx-auto my-6 flex items-center justify-center ">
          <div className="bg-yellow-550 justify-center w-263.75 h-119.5">
            <div className="flex w-263.75 justify-end items-end ">
              <button
                onClick={close}
                className="inline-flex items-end justify-end px-4 py-2 rounded-md hover:text-gray-500 hover:shadow-2xl focus:outline-none focus:shadow-lg"
              >
                <img className="" src={closeimg} alt="" />
              </button>
            </div>
            <div className="justify-center text-4xl font-extrabold text-center font-poppins text-blue-850 mb-11">
              <h1>Cargar Archivos</h1>
            </div>

            <form onSubmit={sendFiles}>
              <div className="flex items-end justify-center ">
                <div className="">
                  <div className="inline-flex items-center w-full ">
                    {okArchivosT && (
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth={1.5}
                        stroke="currentColor"
                        className="w-10 h-10 text-green-600"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                      </svg>
                    )}
                    <label className="mr-2 text-2xl font-bold text-center font-poppins text-blue-850">
                      Actualizar Tablas
                    </label>
                    <input
                      type="file"
                      onChange={(e) => subirArchivosT(e.target.files)}
                      className="placeholder-blue-850 bg-yellow-550 text-center text-xl my-auto h-12.5 font-rubik border-2  border-green border-opacity-0 "
                    ></input>
                  </div>
                  <div className="flex align-middle">
                    <Toggle
                      id="cheese-status"
                      icons={false}
                      defaultChecked={toggleUDAS}
                      onChange={(e) => setToggleUDAS(e.target.checked)}
                    />
                    <label htmlFor="cheese-status">
                      ¿Cargar audios remotamente?
                    </label>
                  </div>
                  <div>
                    <div className="inline-flex items-center w-full ">
                      <label className="mr-2 text-2xl font-bold font-poppins text-blue-850">
                        Cargar Udas
                      </label>
                      <input
                        type="file"
                        // multiple
                        onChange={(u) => subirArchivosU(u.target.files)}
                        className="placeholder-blue-850 bg-yellow-550 text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-green border-opacity-0 "
                      />
                    </div>
                  </div>
                  {toggleUDAS && (
                    <div>
                      <div className="inline-flex items-center w-full ">
                        <label className="mr-2 text-2xl font-bold font-poppins text-blue-850">
                          Cargar audios
                        </label>
                        <input
                          type="file"
                          multiple
                          // onChange={(u) => subirArchivosU(u.target.files)}
                          className="placeholder-blue-850 bg-yellow-550 text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-green border-opacity-0 "
                        />
                      </div>
                    </div>
                  )}
                </div>
              </div>
              <div className="items-center justify-center ">
                <div className="flex justify-center items-center ml-89.5 mr-89.5 mt-8.75">
                  <button
                    onClick={close}
                    className="w-40 h-10 mr-4 text-2xl font-semibold text-white bg-blue-850 hover:shadow-2xl font-poppins"
                  >
                    Cancelar
                  </button>
                  <button
                    type="submit"
                    className="w-40 h-10 text-2xl font-semibold text-white bg-gray-250 hover:shadow-2xl font-poppins"
                  >
                    Subir
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      {isLoading && <LoadingModal />}
    </>
  );
}
export default AddFile;
