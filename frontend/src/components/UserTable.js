import React, { useState } from "react";
import ModifyModal from "./ModifyModal";
import MoreInformationModal from "./MoreInformationModal";

require("typeface-poppins");
require("typeface-rubik");
function UserTable({ userList, updateUserList }) {
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

  // ("admin", "admin"),
  //       ("usuario", "usuario"),
  //       ("etiquetado", "etiquetado"),
  //       ("registro", "registro"),
  return (
    <div className="flex items-center justify-center ">
      <div className=" overflow-x-auto w-193.5">
        <table className=" border-2 border-collapse border-blue-850">
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
              <tr className="">
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
                    className=" bg-yellow-400 font-semibold text-white  w-31.25 h-7.75"
                  >
                    Modificar
                  </button>
                </td>
                <td className="font-rubik font-light text-base h-13.5 ">
                  <button className=" bg-blue-850 ml-2 font-semibold text-white  w-31.25 h-7.75">
                    Eliminar
                  </button>
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
    </div>
  );
}

export default UserTable;
