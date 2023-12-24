import React, { useState, useRef } from "react";
import { toast } from "react-toastify";

import { uploadMasterTableData, uploadUdasData } from "../services/loadFile";
import closeimg from "../images/06.Contacto/x.png";
import Toggle from "react-toggle";
import LoadingModal from "./LoadingModal";

import "react-toggle/style.css";
function AddFile({ close }) {
  const [isLoading, setLoading] = useState(false);
  const [archivosT, setArchivosT] = useState(null);
  const [toggleUDAS, setToggleUDAS] = useState(false);
  const [okArchivosT, setOkArchivosT] = useState(false);
  const [okArchivosU, setOkArchivosU] = useState(false);
  const [errorArchivosT, setErrorArchivosT] = useState(false);
  const [errorArchivosU, setErrorArchivosU] = useState(false);
  const [archivosU, setArchivosU] = useState(null);
  const [usbSelected, setUsbSelected] = useState("");
  const [usbOptions, setUsbOptions] = useState([]);
  const inputTFileRef = useRef(null);
  const inputUFileRef = useRef(null);

  const subirArchivosT = (e) => {
    setArchivosT(e?.[0] || null);
    setOkArchivosT(false)
    setErrorArchivosT(false)
  };

  const subirArchivosU = (u) => {
    setArchivosU(u?.[0] || null);
    setOkArchivosU(false)
    setErrorArchivosU(false)
  };

  const sendFiles = async (e) => {
    e.preventDefault();
    setLoading(true);
    let okFileT = false;
    let okFileU = false;
    if (archivosT) {
      let logsContentT = []
      try {
        const { status , data } = await uploadMasterTableData(archivosT);
        logsContentT = data.logs
        if(!status) throw new Error("Error MasterTable")
        //if(data.error) {
        //  logsContentT = data.logs
        //  throw new Error("Error MasterTable")
        //}
        setArchivosT(null)

        toast.success(`Archivo MasterTable Cargado!`);
        okFileT = true;

      } catch (error) {
        setErrorArchivosT(true)
        toast.error(`Archivo MasterTable tuvo errores!`);
      }
      // Descargar archivo TXT
      const txtContent = logsContentT.join("\n");
      const downloadLinkTXT = document.createElement("a");
      const blobTXT = new Blob([txtContent], { type: "text/plain" });
      const urlTXT = URL.createObjectURL(blobTXT);
      downloadLinkTXT.href = urlTXT;
      downloadLinkTXT.download = "logs_MasterTable.txt";
      downloadLinkTXT.style.display = "none";
      document.body.appendChild(downloadLinkTXT);
      downloadLinkTXT.click();
      document.body.removeChild(downloadLinkTXT);
      setOkArchivosT(okFileT);
    }
    
    if(archivosU) {
      let xlsxContent = ""
      let logsContent = []
      try {

        const { status, data } = await uploadUdasData(archivosU, usbSelected)
        if(!status) throw new Error("Error Udas")
        if(data.error) {
          xlsxContent = data.xlsx
          logsContent = data.logs
          throw new Error("Error Udas")
        }

        if(data.response) {
          setLoading(false);
          setUsbOptions(data.response)
          setUsbSelected(data.response[0])
          return
        } 
        
        setUsbOptions([])
        setUsbSelected("")
        setArchivosU(null)
        if (inputUFileRef.current) {
          inputUFileRef.current.value = '';
        }
        toast.success(`Archivo UDAS Cargado!`);
        okFileU = true
      } catch (error) {
        setErrorArchivosU(true)
        toast.error(`Archivo UDAS tuvo errores!`);
        new Promise(function (resolve, reject) {
          const base64ContentXLSX = xlsxContent;
          const downloadLinkXLSX = document.createElement("a");
          downloadLinkXLSX.href = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64," + base64ContentXLSX;
          downloadLinkXLSX.download = "MasterTablesGenerada_v1.xlsx";
          downloadLinkXLSX.style.display = "none";
          document.body.appendChild(downloadLinkXLSX);
          downloadLinkXLSX.click();
          document.body.removeChild(downloadLinkXLSX);
          resolve()
          
        }).then(() => {
          // Descargar archivo TXT
          const txtContent = logsContent.join("\n");
          const downloadLinkTXT = document.createElement("a");
          const blobTXT = new Blob([txtContent], { type: "text/plain" });
          const urlTXT = URL.createObjectURL(blobTXT);
          downloadLinkTXT.href = urlTXT;
          downloadLinkTXT.download = "logs.txt";
          downloadLinkTXT.style.display = "none";
          document.body.appendChild(downloadLinkTXT);
          downloadLinkTXT.click();
          document.body.removeChild(downloadLinkTXT);
        })
      }
      setOkArchivosU(okFileU);
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
                    {errorArchivosT && (
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-10 h-10 text-red-600">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                    )}
                    <label className="mr-2 text-2xl font-bold text-center font-poppins text-blue-850">
                      Actualizar Tablas
                    </label>
                    <input
                      type="file"
                      ref={inputTFileRef}
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
                      {okArchivosU && (
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
                      {errorArchivosU && (
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-10 h-10 text-red-600">
                          <path strokeLinecap="round" strokeLinejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      )}
                      <label className="mr-2 text-2xl font-bold font-poppins text-blue-850">
                        Cargar Udas
                      </label>
                      <input
                        type="file"
                        ref={inputUFileRef}
                        // multiple
                        onChange={(u) => subirArchivosU(u.target.files)}
                        className="placeholder-blue-850 bg-yellow-550 text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-green border-opacity-0 "
                      />
                    </div>
                  </div>
                  {
                  usbOptions.length > 0 && (
                      <>
                      <span>Seleccione la memoria usb: </span>
                      <select value={usbSelected} onChange={(e) => setUsbSelected(e.target.value)}>
                        {usbOptions.filter(usbname => usbname).map((usbname) => (
                          <option key={usbname} type="radio" value={usbname}>{usbname}</option>
                        ))}
                      </select>
                      {console.log({usbSelected})}
                      </>
                  )}

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
