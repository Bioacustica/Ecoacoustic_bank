import React, { Component } from "react";
import { formList } from "../services";
import PublicTable from "./PublicTable";

require("typeface-poppins");
require("typeface-rubik");

class PublicFilter extends Component {
  state = {
    metodo_etiquetado: [],
    tipo_grabadora: [],
    ciudad: [], //Deshabilitada
    evento: [],
    habitat: [], //Deshabilitada
    municipio: [],
    software: [],
    tipo_case: [],
    tipo_microfono: [],
  };
  componentDidMount = async () => {
    const response = await formList();
    console.log(response);
    this.setState({
      evento: response.data.evento,
      habitat: response.data.habitat,
      ciudad: response.data.ciudad,
    });
  };
  render() {
    return (
      <div>
        <div className="h-0.625 bg-blue-850 mx-auto w-37 mt-11.25  mb-3"></div>
        <div>
          <h1 className="text-center font-extrabold font-poppins text-4.5xl text-blue-850 mb-3">
            Filtros
          </h1>
        </div>
        <div className="h-0.625 bg-blue-850 mx-auto mb-11.25 w-37 "></div>

        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">Ciudades</span>
              <select
                disabled
                className="block w-full border border-blue-850 rounded-md bg-white  shadow-lg focus:border-indigo-200 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option>seleccionar</option>
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">Habitat</span>
              <select className="block  border border-blue-850 w-full mt-1 rounded-md bg-white  shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50mt-1 h-7.75">
                <option>seleccionar</option>
                {this.state.habitat.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">Municipio</span>
              <select
                disabled
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75 mt-1"
              >
                <option>seleccionar</option>
              </select>
            </label>

            <label className="block text-center w-54.25 ">
              <span className="text-blue-850 content-center">Evento</span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option value={null}>seleccionar</option>
                {this.state.evento.map((elemento) =>
                  elemento.map((event2) => (
                    <option key={event2} value={event2}>
                      {event2}
                    </option>
                  ))
                )}
              </select>
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">Tipo de case</span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option>seleccionar</option>
                <option>Medallo</option>
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">
                Tipo de microfono
              </span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option>seleccionar</option>
                <option>Medallo</option>
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">
                Metodo de etiquetado
              </span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75 mt-1">
                <option>seleccionar</option>
                {this.state.metodo_etiquetado.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 ">
              <span className="text-blue-850 content-center">
                Software de etiquetado
              </span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option>seleccionar</option>
                <option>Medallo</option>
              </select>
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850 content-center">
                Tipo de grabadora
              </span>
              <select className="block w-full mt-1 rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75">
                <option value={null}>seleccionar</option>
                <option>Medallo</option>
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850">Fecha de inicio</span>
              <input
                type="date"
                className="mt-1 block w-full h-7.75 rounded-md border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850">Fecha final</span>
              <input
                type="date"
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <span className="text-blue-850">Elevacion minima</span>
              <input
                type="text"
                className="mt-1 block w-full h-7.75 rounded-md border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-41.5">
              <span className="text-blue-850">Elevacion maxima</span>
              <input
                type="text"
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <br />
              <button className="block rounded-md font-semibold font-poppins text-white bg-green-550 hover:shadow-lg hover:opacity-70 w-54.25 h-7.75 ">
                Buscar
              </button>
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center mb-10.75">
          <div className="w-341.5 h-151.25 bg-gray-50 overflow-x-auto">
            <PublicTable />
          </div>
        </div>

        <div className="flex items-center justify-center">
          <nav
            className="relative z-0 inline-flex rounded-md shadow-sm -space-x-px"
            aria-label="Pagination"
          >
            <a
              href="#"
              className="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
            >
              <span className="sr-only">Previous</span>
              {/* Heroicon name: solid/chevron-left */}
              <svg
                className="h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fillRule="evenodd"
                  d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            </a>
            {/* Current: "z-10 bg-indigo-50 border-indigo-500 text-indigo-600", Default: "bg-white border-gray-300 text-gray-500 hover:bg-gray-50" */}
            <a
              href="#"
              aria-current="page"
              className="z-10 bg-green-450 border-green-450 text-white relative inline-flex items-center px-4 py-2 border text-sm font-medium"
            >
              1
            </a>
            <a
              href="#"
              className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"
            >
              2
            </a>

            <span className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
              ...
            </span>
            <a
              href="#"
              className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"
            >
              10
            </a>
            <a
              href="#"
              className="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
            >
              <span className="sr-only">Next</span>
              {/* Heroicon name: solid/chevron-right */}
              <svg
                className="h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fillRule="evenodd"
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            </a>
          </nav>
        </div>
      </div>
    );
  }
}
export default PublicFilter;
