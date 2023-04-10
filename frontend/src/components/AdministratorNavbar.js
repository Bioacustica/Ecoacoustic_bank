import React, { useEffect, useRef, useState } from "react";
import AddFile from "../components/Addfile";

function AdministratorNavbar() {
  const [showFile, setShowFile] = useState(false);
  const [showDropdown, setShowDropdown] = useState(false);
  const openFile = () => setShowFile(true);

  const closeFile = () => setShowFile(false);
  const username = window.localStorage.getItem("username");

  const dropdownRef = useRef(null);

  useEffect(() => {
    document.addEventListener("click", handleClickOutside);
    return () => {
      document.removeEventListener("click", handleClickOutside);
    };
  }, []);

  function handleClickOutside(event) {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
      setShowDropdown(false);
    }
  }

  return (
    <div className="flex justify-center bg-green-450">
      <nav className="flex items-center w-9/12 justify-evenly h-11">
        <a
          href="/"
          className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
        >
          INICIO
        </a>
        <a
          href="#"
          className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
        >
          <button onClick={openFile}>SUBIR AUDIOS</button>
        </a>
        <a
          href="/admin-label-filter"
          className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
        >
          FILTROS
        </a>
        <a
          href="/user-panel"
          className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
        >
          USUARIOS
        </a>
        <a
          href="#"
          className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
        >
          MAPA
        </a>
        <a
          href="#"
          className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
        >
          VISUALIZACIÓN DE METADATOS
        </a>
        <div className="p-10">
          <div className="relative inline-block dropdown" ref={dropdownRef}>
            <button
              onClick={() => setShowDropdown((show) => !show)}
              className="inline-flex items-center px-4 text-white rounded"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.5}
                stroke="currentColor"
                className="w-6 h-6"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>

              <span className="mr-1">{username.toUpperCase()}</span>
              <svg
                className="w-4 h-4 fill-current"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />{" "}
              </svg>
            </button>
            <ul
              className={`absolute ${
                showDropdown ? "block" : "hidden"
              } w-40 pt-1 text-gray-700 dropdown-menu`}
            >
              <li className="">
                <button
                  onClick={() => (window.location.href = "/")}
                  className="block px-4 py-2 whitespace-no-wrap bg-white border-2 rounded border-zinc-500 hover:bg-gray-100 "
                >
                  Cerrar sesión
                </button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      {showFile && <AddFile className="z-50" close={closeFile} />}
    </div>
  );
}

export default AdministratorNavbar;
