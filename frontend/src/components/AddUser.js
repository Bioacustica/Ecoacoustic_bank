import React, { useState } from "react";
import { toast } from "react-toastify";

import closeimg from "../images/06.Contacto/x.png";
import { createUser } from "../services/user";
import LoadingModal from "./LoadingModal";

function AddUser({ close, addUserList }) {
  const [isLoading, setLoading] = useState(false);

  const [user, setUser] = useState({
    username: "",
    email: "",
    roles: "",
    password: "",
  });
  const handleInput = (e) => {
    const { name, value } = e.target;

    setUser((user) => ({ ...user, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const { status, data, errorMessage } = await createUser(user);

    setLoading(false);
    if (!status) {
      toast.error(errorMessage);
      return;
    }

    addUserList(data.user);
    setUser({
      username: "",
      email: "",
      roles: "",
      password: "",
    });
    toast.success("Usuario creado!");
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
                  <h1>Agregar usuario</h1>
                </div>
                <form onSubmit={handleSubmit}>
                  <div className="flex items-end justify-center ">
                    <div className="">
                      <div>
                        <div className="inline-flex items-center justify-end w-full ">
                          <label className="mr-2 text-2xl font-bold font-poppins text-blue-850">
                            Nombre:{" "}
                          </label>
                          <input
                            name="username"
                            type="text"
                            required
                            value={user.username}
                            onChange={handleInput}
                            className="placeholder-blue-850 bg-white text-center text-xl  w-171.25 h-12.5 font-rubik border-2  border-white border-opacity-100 "
                          />
                        </div>
                      </div>

                      <div className="inline-flex items-center justify-end w-full ">
                        <label className="mt-2 mr-2 text-2xl font-bold text-center font-poppins text-blue-850">
                          Mail:{" "}
                        </label>
                        <input
                          type="email"
                          name="email"
                          required
                          value={user.email}
                          onChange={handleInput}
                          className="mt-4 w-171.25 text-xl  h-12.5 placeholder-blue-850 text-center bg-white font-rubik"
                        ></input>
                      </div>

                      <div className="flex items-center justify-end">
                        <label className="mr-2 text-2xl font-bold font-poppins text-blue-850">
                          Rol:{" "}
                        </label>
                        <select
                          required
                          name="roles"
                          value={user.roles}
                          onChange={handleInput}
                          className="block w-171.25 h-12.25 font-rubik text-xl text-center mt-4 bg-white border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                        >
                          <option
                            value=""
                            className="text-xl text-center font-rubik"
                          >
                            Seleccionar
                          </option>
                          <option
                            value="admin"
                            className="text-xl text-center font-rubik"
                          >
                            Administrador
                          </option>
                          <option
                            value="registro"
                            className="text-xl text-center font-rubik"
                          >
                            Colaborador de registros
                          </option>
                          <option
                            value="etiquetado"
                            className="text-xl text-center font-rubik"
                          >
                            Colaborador de etiquetado
                          </option>
                          <option
                            value="usuario"
                            className="text-xl text-center font-rubik"
                          >
                            Usuario
                          </option>
                        </select>
                      </div>

                      <div className="inline-flex items-center justify-end w-full ">
                        <label className="mr-2 text-2xl font-bold text-center font-poppins text-blue-850">
                          Contraseña:{" "}
                        </label>
                        <input
                          type="password"
                          name="password"
                          required
                          value={user.password}
                          onChange={handleInput}
                          className="mt-4 w-171.25 text-center h-12.5 placeholder-blue-850 bg-white font-rubik"
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
export default AddUser;
