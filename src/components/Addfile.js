import React,{useState}  from "react";

import closeimg from "../images/06.Contacto/x.png";

function AddFile({ close }) {

    const[archivosT,setArchivosT]=useState(null);

    const subirArchivosT=e=>{
     setArchivosT(e); 
      console.log(e)
    }
    const[archivosU,setArchivosU]=useState(null);

    const subirArchivosU=u=>{
     setArchivosU(u); 
      console.log(u)
    }
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
                  <h1>Cargar Archivos</h1>
                </div>

                <form>
                  <div className="flex justify-center items-end ">
                    <div className="">
                      <div>
                        <div className="items-center inline-flex justify-end w-full ">
                        <label className="font-poppins font-bold text-blue-850 text-2xl mr-2">
                        Cargar Udas
                        </label>
                        <input
                          type="file"
                        
                    
                          required
                          multiple onChange={(u)=>subirArchivosU(u.target.files)}
                          className="placeholder-blue-850 bg-yellow-550 text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-green border-opacity-0 "
                        />
                        </div>
                        
                      </div>

                     
                     <div className="items-center inline-flex justify-end w-full ">
                     <label className="font-poppins text-center font-bold text-blue-850 text-2xl mr-2">
                        Actualizar Tablas
                        </label>
                     <input
                        type="file"
                      
                        required
                        multiple onChange={(e)=>subirArchivosT(e.target.files)}
                        className="placeholder-blue-850 bg-yellow-550 text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-green border-opacity-0 "
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
                        Subir 
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
export default AddFile;
