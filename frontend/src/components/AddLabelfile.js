import React, { useRef, useState } from "react";
import { toast } from "react-toastify";

import { uploadLabelFile } from "../services/loadFile";
import closeimg from "../images/06.Contacto/x.png";
import Toggle from "react-toggle";
import LoadingModal from "./LoadingModal";

import "react-toggle/style.css";
function AddLabelFile({ close }) {
  const [isLoading, setLoading] = useState(false);
  const [archivo, setArchivo] = useState(null);
  const [okArchivo, setOkArchivo] = useState(false);
  const [errorArchivo, setErrorArchivo] = useState(false);
  const inputFileRef = useRef(null);

  const subirArchivo = (e) => {
    setArchivo(e?.[0] || null);
    setOkArchivo(false)
    setErrorArchivo(false)
  };

  const sendFiles = async (e) => {
    e.preventDefault();
    setLoading(true);
    let okFile = false;
    let logsContent = []

    if (archivo) {
      try {
        const { status, data } = await uploadLabelFile(archivo);

        if(!status) throw new Error("Error etiquetado")

        if(data.error) {
          logsContent = data.logs
          throw new Error("Error etiquetado")
        }

        toast.success(`Archivo de etiquetado Cargado!`);
        okFile = true;

        if (inputFileRef.current) {
          inputFileRef.current.value = '';
        }
      } catch (error) {
        setErrorArchivo(true)
        toast.error(`Archivo de etiquetado errores!`);
        
        const txtContent = logsContent.join("\n");
        if(txtContent.length > 0) {

          const downloadLinkTXT = document.createElement("a");
          const blobTXT = new Blob([txtContent], { type: "text/plain" });
          const urlTXT = URL.createObjectURL(blobTXT);
          downloadLinkTXT.href = urlTXT;
          downloadLinkTXT.download = "logs.txt";
          downloadLinkTXT.style.display = "none";
          document.body.appendChild(downloadLinkTXT);
          downloadLinkTXT.click();
          document.body.removeChild(downloadLinkTXT);
        }
      }
      setOkArchivo(okFile);
    }

    setLoading(false);
  };

  return (
    <>
      <div className="fixed inset-0 z-40 bg-black opacity-25"></div>

      <div className="fixed inset-0 z-50 flex items-center justify-center overflow-x-hidden overflow-y-auto outline-none focus:outline-none">
        <div className="relative flex items-center justify-center w-auto max-w-3xl mx-auto my-6 ">
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
              <h1>Upload Labelling</h1>
            </div>

            <form onSubmit={sendFiles}>
              <div className="flex items-end justify-center ">
                <div className="">
                  <div className="inline-flex items-center w-full ">
                    {okArchivo && (
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
                    {errorArchivo && (
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-10 h-10 text-red-600">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    )}
                    <label className="mr-2 text-2xl font-bold text-center font-poppins text-blue-850">
                      Upload file
                    </label>
                    <input
                      type="file"
                      ref={inputFileRef}
                      onChange={(e) => subirArchivo(e.target.files)}
                      className="placeholder-blue-850 bg-yellow-550 text-center text-xl my-auto h-12.5 font-rubik border-2  border-green border-opacity-0 "
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
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="w-40 h-10 text-2xl font-semibold text-white bg-gray-250 hover:shadow-2xl font-poppins"
                  >
                    Upload
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
export default AddLabelFile;
