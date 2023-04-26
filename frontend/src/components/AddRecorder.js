import React, { useState } from "react";
import { toast } from "react-toastify";

import closeimg from "../images/06.Contacto/x.png";
import LoadingModal from "./LoadingModal";
import { createRecorder } from "../services/recorder";

function AddRecorder({ close, addRecorderList, hardwareList }) {
  const [isLoading, setLoading] = useState(false);

  const [recorder, setRecorder] = useState({
    h_serial: "",
    id_hardware: "",
  });
  const handleInput = (e) => {
    const { name, value } = e.target;

    setRecorder((recorder) => ({ ...recorder, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const { status, data, errorMessage } = await createRecorder(recorder);

    setLoading(false);
    if (!status) {
      toast.error(errorMessage);
      return;
    }

    addRecorderList(data.recorder);
    setRecorder({
      h_serial: "",
      id_hardware: "",
    });
    toast.success("Grabadora creada!");
  };

  return (
    <>
      <div className="fixed inset-0 z-50 flex items-center justify-center overflow-x-hidden overflow-y-auto outline-none focus:outline-none">
        <div className="relative w-auto max-w-3xl mx-auto my-6">
          <div className="flex items-center justify-center">
            <div className="bg-yellow-550 justify-center w-263.75 h-119.5">
              <div className="items-center justify-center">
                <div className="flex w-263.75 justify-end items-end ">
                  <button
                    onClick={close}
                    className="inline-flex items-end justify-end px-4 py-2 rounded-md hover:text-gray-500 hover:shadow-2xl focus:outline-none focus:shadow-lg"
                  >
                    <img className="" src={closeimg} alt="" />
                  </button>
                </div>
                <div className="justify-center text-4xl font-extrabold text-center font-poppins text-blue-850 mb-11">
                  <h1>Agregar grabadora</h1>
                </div>
                <form onSubmit={handleSubmit}>
                  <div className="flex items-end justify-center ">
                    <div className="">
                      <div className="flex items-center justify-end">
                        <label className="mr-2 text-2xl font-bold font-poppins text-blue-850">
                          Hardware:
                        </label>
                        <select
                          required
                          name="id_hardware"
                          value={recorder.id_hardware}
                          onChange={handleInput}
                          className="block w-171.25 h-12.25 font-rubik text-xl text-center mt-4 bg-white border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                        >
                          <option
                            value=""
                            className="text-xl text-center font-rubik"
                          >
                            Seleccionar
                          </option>
                          {(hardwareList || []).map((hardware) => (
                            <option
                              value={hardware.id_hardware}
                              className="text-xl text-center font-rubik"
                            >
                              {hardware.description}
                            </option>
                          ))}
                        </select>
                      </div>
                      <div className="inline-flex items-center justify-end w-full ">
                        <label className="mt-2 mr-2 text-2xl font-bold text-center font-poppins text-blue-850">
                          Serial:
                        </label>
                        <input
                          type="text"
                          name="h_serial"
                          required
                          value={recorder.h_serial}
                          onChange={handleInput}
                          className="mt-4 w-171.25 text-xl  h-12.5 placeholder-blue-850 text-center bg-white font-rubik"
                        ></input>
                      </div>
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
      <div className="fixed inset-0 z-40 bg-black opacity-25"></div>
      {isLoading && <LoadingModal />}
    </>
  );
}
export default AddRecorder;
