import React, { useState } from "react";
import { sendMenssage } from "../services";
import closeimg from "../images/06.Contacto/x.png";

require("typeface-poppins");
require("typeface-rubik");

function ContactModal({ close }) {
  const [success, setSuccess] = useState(null);

  const [mensaje, setMensaje] = useState({
    subject: "",
    from_email: "",
    message: "",
  });
  const handleChange = (event) => {
    setMensaje({
      ...mensaje,
      [event.target.name]: event.target.value,
    });
  };

  const sendData = async (e, mensaje) => {
    e.preventDefault();
    const response = await sendMenssage(mensaje);

    response ? setSuccess(true) : setSuccess(false);
  };

  return (
    <>
      <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
        <div className="relative w-auto my-6 mx-auto max-w-3xl">
          {/*content*/}
          <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            {/* ACA EMPIEZA EL FORMULARIO*/}
            <form onSubmit={(e) => sendData(e, mensaje)}>
              <div className="flex justify-center items-center ">
                <div className="w-263.75 h-148.5 bg-blue-250 rounded-lg">
                  <div className="flex w-263.75 justify-end items-end mb-2">
                    <button
                      onClick={close}
                      className="rounded-md p-4 inline-flex justify-end items-end hover:text-gray-500 hover:bg-blue-100 focus:outline-none focus:shadow-lg"
                    >
                      <img className="" src={closeimg} alt="" />
                    </button>
                  </div>

                  <div className="flex ">
                    <div className="ml-12 w-1/2">
                      <h1 className="text-left font-extrabold font-poppins text-5.5xl text-blue-850">
                        Contacto
                      </h1>
                      <div className="mt-10">
                        <h1 className="text-left font-semibold font-poppins text-2.5xl text-blue-850">
                        Nombre de contacto UdeA
                        </h1>
                        <h1 className="text-left font-semibold font-poppins text-2.5xl text-blue-850">
                          contactoUdeA@udea.edu.co
                        </h1>
                        <h1 className="text-left italic font-rubik text-2.5xl text-blue-850">
                          Universidad de Antioquia
                        </h1>
                      </div>

                      <div className="mt-13.25">
                        <h1 className="text-left font-semibold font-poppins text-2.5xl text-blue-850">
                          Nombre de contacto ITM
                        </h1>
                        <h1 className="text-left font-semibold font-poppins text-2.5xl text-blue-850">
                          contactoITM@itm.edu.co
                        </h1>
                        <h1 className="text-left italic font-rubik text-2.5xl text-blue-850">
                          ITM Institución Universitaria
                        </h1>
                      </div>
                      {success && (
                        <div>
                          <h2 className="text-left font-semibold font-poppins mt-3 text-2.5xl text-blue-900">
                            Mensaje enviado con exito
                          </h2>
                        </div>
                      )}

                      {success === false && (
                        <div>
                          <h2 className="text-left font-semibold font-poppins mt-3 text-xl text-red-600">
                            Error al enviar el mensaje, intentelo nuevamente.
                          </h2>
                        </div>
                      )}
                    </div>

                    <div className="mr-12 w-1/2 ">
                      <input
                        name="subject"
                        type="text"
                        onChange={handleChange}
                        placeholder="Nombre"
                        required
                        className="placeholder-blue-850 bg-white p-3 w-126.75 h-17.25 font-poppins font-semibold rounded-lg border-2 text-4xl  border-white border-opacity-100 "
                      />

                      <input
                        name="from_email"
                        type="text"
                        onChange={handleChange}
                        required
                        placeholder="Correo"
                        className="placeholder-blue-850 mt-5 bg-white p-3 w-126.75 h-17.25 font-poppins font-semibold rounded-lg text-4xl  border-2 border-white border-opacity-100 "
                      />

                      <textarea
                        className="w-126.75 px-3 mt-5 py-2 placeholder-blue-850 placer font-poppins resize-none border-2 text-4xl font-semibold rounded-lg h-52 border-opacity-100 focus:outline-none "
                        rows="10"
                        name="message"
                        onChange={handleChange}
                        placeholder="Mensaje"
                        required
                      ></textarea>
                    </div>
                  </div>

                  <div className="flex h-28 justify-center items-center">
                    <button
                      type="submit"
                      className=" bg-blue-850 text-3xl text-white font-semibold hover:shadow-2xl font-poppins h-14.25 py-2 px-4 w-48  rounded"
                    >
                      Enviar
                    </button>
                  </div>
                </div>
              </div>
            </form>

            {/* ACA TERMINA EL FORMULARIO*/}
          </div>
        </div>
      </div>
      <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
    </>
  );
}
export default ContactModal;
