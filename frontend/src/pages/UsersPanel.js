import React, { useEffect, useState } from "react";
import Head from "../components/Head";
import AdministratorNavbar from "../components/AdministratorNavbar";
import imgbanner from "../images/02.banner 1/imgBanner.jpg";
import Footer from "../components/Footer";
import UserTable from "../components/UserTable";
import AddUser from "../components/AddUser";
import { getUsersList } from "../services/user";

require("typeface-poppins");
require("typeface-rubik");

function UserPanel() {
  const userRole = localStorage.getItem("rolename");

  const [showModal, setShowModal] = useState(false);
  const [userList, setUserList] = useState([]);

  const openModal = () => setShowModal(true);

  const closeModal = () => setShowModal(false);

  const getUsers = async () => {
    try {
      const { data } = await getUsersList();
      setUserList(data.users);
    } catch (error) {}
  };

  const addUserList = (user) => {
    setUserList((users) => [...users, user]);
  };

  const updateUserList = (user) => {
    setUserList((users) =>
      (users || []).map((u) => (u.id_user !== user.id_user ? u : { ...user }))
    );
  };

  useEffect(() => {
    getUsers();
  }, []);

  return (
    <>
      <header className="sticky top-0 z-30 bg-white">
        <Head />
        <AdministratorNavbar />
      </header>

      <main>
        <div className="flex items-center justify-center">
          <div>
            <img src={imgbanner} alt="" />
          </div>
          <div className="absolute self-center justify-center ">
            <div className="space-y-3">
              <h1 className="text-center font-extrabold font-poppins text-4.5xl text-white">
                {userRole},
              </h1>
              <h1 className="text-center font-extrabold font-poppins  text-4.5xl text-white">
                Usuarios
              </h1>
            </div>
          </div>
        </div>

        <div className="flex items-center justify-center mt-5 mb-3 ">
          <button
            onClick={openModal}
            className="w-87.75 bg-blue-250 text-white h-10.75 font-semibold text-2xl font-poppins"
          >
            Agregar usuario
          </button>
        </div>

        <div className="h-full">
          <UserTable userList={userList} updateUserList={updateUserList} />
        </div>

        {showModal && (
          <AddUser
            className="z-50"
            close={closeModal}
            addUserList={addUserList}
          />
        )}
      </main>

      <Footer />
    </>
  );
}

export default UserPanel;
