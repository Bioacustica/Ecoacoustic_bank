import React, { useState } from "react";
import { toast } from "react-toastify";

import LoadingModal from "./LoadingModal";
import RecorderModifyModal from "./RecorderModifyModal";

require("typeface-poppins");
require("typeface-rubik");
function RecorderTable({ recorderList, updateRecorderList,hardwareList }) {
  const [isLoading, setLoading] = useState(false);

  const [recorderEdit, setRecorderEdit] = useState({
    h_serial: "",
    id_hardware: "",
  });
  const [showModal, setShowModal] = useState(false);

  const openModal = (user) => {
    setRecorderEdit({ ...user, password: "" });
    setShowModal(true);
  };

  const closeModal = () => setShowModal(false);
   
  return (
    <div className="flex items-center justify-center">
      <div className="overflow-x-auto ">
        <table className="border-2 border-collapse border-blue-850">
          <thead>
            <tr className="">
              <td className="border-2 font-rubik border-blue-850 text-base h-11.25 px-4 text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850 w-46.75 text-base h-11.25  text-center">
                Hardware
              </td>
              <td className="border-2 font-rubik border-blue-850 w-80.25 text-base h-11.25 text-center">
                Serial
              </td>
              <td
                colSpan={2}
                className="border-2 font-rubik border-blue-850  w-48.5 text-base h-11.25  text-center"
              >
                Acciones
              </td>
            </tr>
          </thead>

          <tbody>
            {(recorderList || []).map((recorder) => (
              <tr className="" key={recorder.id_h_serial}>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {recorder.id_h_serial}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {recorder.hardware}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {recorder.h_serial}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  <button
                    onClick={() => openModal(recorder)}
                    className=" bg-yellow-400 font-semibold text-white  w-31.25 h-7.75 mx-3"
                  >
                    Modificar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {showModal && (
        <RecorderModifyModal
          className="z-50"
          close={closeModal}
          recorderEdit={recorderEdit}
          updateRecorderList={updateRecorderList}
          hardwareList={hardwareList}
        />
      )}
      {isLoading && <LoadingModal />}
    </div>
  );
}

export default RecorderTable;
