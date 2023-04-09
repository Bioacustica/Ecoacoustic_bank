import React, { useState } from "react";
import { toast } from "react-toastify";

import ModifyModal from "./ModifyModal";
import MoreInformationModal from "./MoreInformationModal";
import Toggle from "react-toggle";
import { toggleActiveUser } from "../services/user";
import LoadingModal from "./LoadingModal";

require("typeface-poppins");
require("typeface-rubik");
function UserTable({ userList, updateUserList }) {
  const [isLoading, setLoading] = useState(false);

  const [userEdit, setUserEdit] = useState({
    username: "",
    email: "",
    roles: "",
    password: "",
  });
  const [showModal, setShowModal] = useState(false);

  const openModal = (user) => {
    console.log("user :>> ", user);
    setUserEdit({ ...user, password: "" });
    setShowModal(true);
  };

  const closeModal = () => setShowModal(false);
  const toggleStateUser = async (user) => {
    setLoading(true);
    const { status, data, errorMessage } = await toggleActiveUser(user);
    setLoading(false);
    if (!status) {
      toast.error(errorMessage ?? "Error actualizando usuario");
      return;
    }
    updateUserList({ ...user, is_active: !user.is_active });
    toast.success(`Usuario actualizado!`);
  };
  // ("admin", "admin"),
  //       ("usuario", "usuario"),
  //       ("etiquetado", "etiquetado"),
  //       ("registro", "registro"),
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
                Nombre
              </td>
              <td className="border-2 font-rubik border-blue-850 w-80.25 text-base h-11.25 text-center">
                Email
              </td>
              <td className="border-2 font-rubik border-blue-850  w-48.5 text-base h-11.25  text-center">
                Rol
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
            {(userList || []).map((user) => (
              <tr className="" key={user.id_user}>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {user.id_user}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {user.username}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {user.email}
                </td>
                <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {user.roles}
                </td>
                {/* <td className="border-2 font-rubik font-light border-blue-850 text-base h-13.5 px-4 text-center">
                  {user.is_active ? "Activo" : "Inactivo"}
                </td> */}
                <td className="font-rubik font-light text-base h-13.5 ">
                  <button
                    onClick={() => openModal(user)}
                    className=" bg-yellow-400 font-semibold text-white  w-31.25 h-7.75 mx-3"
                  >
                    Modificar
                  </button>
                </td>
                <td className="font-rubik font-light text-base h-13.5 ">
                  <div className="flex mx-3 align-middle">
                    <Toggle
                      id="cheese-status"
                      icons={false}
                      defaultChecked={user.is_active}
                      onChange={(e) => toggleStateUser(user)}
                    />
                    <label htmlFor="cheese-status" className="ml-2">
                      {user.is_active ? "Inactivar" : "Activar"}
                    </label>
                  </div>
                  {/* <button className=" bg-blue-850 ml-2 font-semibold text-white  w-31.25 h-7.75">
                    Eliminar
                  </button> */}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {showModal && (
        <ModifyModal
          className="z-50"
          close={closeModal}
          userEdit={userEdit}
          updateUserList={updateUserList}
        />
      )}
      {isLoading && <LoadingModal />}
    </div>
  );
}

export default UserTable;
