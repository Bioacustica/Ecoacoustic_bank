import React, { Children, useEffect, useRef, useState } from "react";
import AddFile from "../components/Addfile";
import ContactModal from "./ContactModal";
import AddLabelFile from "./AddLabelfile";

const NavbarItem = ({ item }) => {
  return item.render ? (
    <div className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white">
      {item.render()}
    </div>
  ) : (
    <a
      href={item.path}
      className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
    >
      {(item.label || "").toUpperCase()}
    </a>
  );
};

function AdministratorNavbar() {
  const username = window.localStorage.getItem("username");
  const userRole = localStorage.getItem("rol");

  const [showFile, setShowFile] = useState(false);
  const [showDropdown, setShowDropdown] = useState(false);
  const [showHomeDropdown, setShowHomeDropdown] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [showLabelModal, setShowLabelModal] = useState(false);

  const openModal = () => setShowModal(true);
  const closeModal = () => setShowModal(false);

  const openLabelModal = () => setShowLabelModal(true);
  const closeLabelModal = () => setShowLabelModal(false);

  const dropdownRef = useRef(null);
  const homeDropdownRef = useRef(null);

  useEffect(() => {
    document.addEventListener("click", handleClickOutside);
    document.addEventListener("click", handleClickOutsideHomeItem);
    return () => {
      document.removeEventListener("click", handleClickOutside);
      document.removeEventListener("click", handleClickOutsideHomeItem);
    };
  }, []);

  function handleClickOutside(event) {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
      setShowDropdown(false);
    }
  }

  function handleClickOutsideHomeItem(event) {
    if (
      homeDropdownRef.current &&
      !homeDropdownRef.current.contains(event.target)
    ) {
      setShowHomeDropdown(false);
    }
  }

  const openFile = () => setShowFile(true);
  const closeFile = () => setShowFile(false);

  const HOME = {
    path: "#",
    label: "HOME",
    children: [
      { path: "/", label: "Home" },
      { path: "/#sobre-nosotros", label: "About us" },
      { path: "/#visualizacion", label: "Summary" },
      { path: "https://github.com/Bioacustica/Ecoacoustic_bank/wiki", label: "Wiki" },
      // { path: "/#filtros", label: "Filtros" },
      { path: "#", label: "Contact", render: function () { return <button onClick={openModal}>{username ? this.label : this.label.toUpperCase() }</button> }},
    ],
    render: function () {
      return (
        <div className="relative flex dropdown" ref={homeDropdownRef}>
          <button
            onClick={() => setShowHomeDropdown((show) => !show)}
            className="inline-flex items-center px-4 text-white rounded"
          >
            <span className="mr-1">{this.label.toUpperCase()}</span>
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
              showHomeDropdown ? "block" : "hidden"
            } w-40 pt-8 text-gray-700 dropdown-menu`}
          >
            {this.children.map((child, i) => (
              <li key={child.label}>
                <a
                  href={child.path}
                  className={`block px-4 py-2 whitespace-no-wrap bg-white border-2 ${
                    i === 0 && "rounded-t"
                  } ${
                    i === this.children.length - 1 && "rounded-b"
                  } border-zinc-500 hover:bg-gray-100`}
                >
                  {child.render ? child.render() : child.label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      );
    },
  };

  const UPLOAD_AUDIO = {
    path: "#",
    label: "SUBIR AUDIOS",
    render: () => <button onClick={openFile}>UPLOAD</button>,
  };

  const FILTERS = {
    path: "/admin-label-filter",
    label: "QUERIES",
  };

  const LABELED = {
    path: "#",
    label: "ETIQUETADO",
    render: () => <button onClick={openLabelModal}>LABELLING</button>,
  };

  const RECORDER = {
    path: "/recorder-panel",
    label: "RECORDERS",
  };

  const USERS = {
    path: "/user-panel",
    label: "USERS",
  };

  const MAP = {
    path: "#",
    label: "MAP",
  };

  const METADATA = {
    path: "#",
    label: "SUMMARY",
  };
  const navbarRole = {
    admin: [HOME, UPLOAD_AUDIO, FILTERS, LABELED, RECORDER, USERS, MAP, METADATA],
    registro: [HOME, UPLOAD_AUDIO, FILTERS, RECORDER, MAP, METADATA],
    etiquetado: [HOME, FILTERS, MAP, METADATA],
    usuario: [HOME, FILTERS, MAP, METADATA],
    unknown: [...HOME.children],
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("username");
    localStorage.removeItem("rol");
    localStorage.removeItem("rolename");

    window.location.href = "/";
  };

  return (
    <div className="flex justify-center bg-green-450">
      <nav className="flex items-center w-9/12 justify-evenly h-11">
        {(navbarRole[userRole || "unknown"] || []).map((navbarItem) => (
          <NavbarItem key={navbarItem.label} item={navbarItem} />
        ))}
        {!username ? (
          <a
            href="/log-in"
            className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
          >
            LOG IN
          </a>
        ) : (
          <a
            href="#"
            className="content-center text-white border-b-2 hover:text-white hover:text-whithe border-green-450 hover:border-b-2 hover:border-white"
          >
            <div className="relative flex dropdown" ref={dropdownRef}>
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
                } w-40 pt-8 text-gray-700 dropdown-menu`}
              >
                <li className="">
                  <button
                    onClick={() => handleLogout()}
                    className="block px-4 py-2 whitespace-no-wrap bg-white border-2 rounded border-zinc-500 hover:bg-gray-100 "
                  >
                    Log out
                  </button>
                </li>
              </ul>
            </div>
          </a>
        )}
      </nav>
      {showFile && <AddFile className="z-50" close={closeFile} />}
      {showModal && <ContactModal close={closeModal} />}
      {showLabelModal && <AddLabelFile close={closeLabelModal} />}

    </div>
  );
}

export default AdministratorNavbar;
