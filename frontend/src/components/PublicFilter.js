import React, { useState } from "react";
import { Component } from "react";
import { findRenderedDOMComponentWithClass } from "react-dom/test-utils";
import { formList, fetch_audios } from "../services";
import PublicTable from "./PublicTable";

require("typeface-poppins");
require("typeface-rubik");
class PublicFilter extends Component {
  /*const [stado, setCredentials] = useState({
    email: "",
    password: "",
  });*/

  state = {
    metodo_etiquetado: [],
    tipo_grabadora: [],
    ciudades: [],
    eventos: [],
    habitats: [],
    municipios: [],
    software: [],
    tipo_case: [],
    tipo_microfono: [],
    filters: {
      catalogo: "",
      habitat: "",
      municipio: "",
      evento: "",
      "tipo de case": "",
      "tipo de micro": "",
      "metodo etiquetado": "",
      software: "",
      "tipo de grabadora": "",
    },
    List_Audio: {},
  };

  valueToState = ({ name, value }) => {
    this.setState((state) => {
      return { ...state, filters: { ...state.filters, [name]: value } };
    });
    //console.log(name,value);
  };

  // componentDidMount = async () => {
  //   const response = await formList();
  //   //console.log(response);
  //   this.setState({
  //     eventos: response.data.evento,
  //     habitats: response.data.habitat,
  //     ciudades: response.data.ciudad,
  //     tipo_grabadora: response.data.Tipo_de_grabadora,
  //     tipo_case: response.data.tipo_de_case,
  //     tipo_microfono: response.data.tipo_de_micro,
  //     metodo_etiquetado: response.data.Metodo_etiquetado,
  //     software: response.data.software_etiquetado,
  //     municipios: response.data.municipio,
  //   });
  // };

  publicAudio = async () => {
    const List_Audio = await fetch_audios(this.state.filters);

    this.setState((state) => {
      return { ...state, List_Audio };
    });
  };
  render() {
    return (
      <div>
        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-41.5">
              <span className="content-center text-blue-850">Ciudades</span>
              <select
                name="ciudad"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full border border-blue-850 rounded-md bg-white  shadow-lg focus:border-indigo-200 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option value="">seleccionar</option>
                {this.state.ciudades.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="content-center text-blue-850">Hábitat</span>
              <select
                name="habitat"
                onChange={(event) => this.valueToState(event.target)}
                className="block  border border-blue-850 w-full mt-1 rounded-md bg-white  shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50mt-1 h-7.75"
              >
                <option value="">seleccionar</option>
                {this.state.habitats.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="content-center text-blue-850">Municipio</span>
              <select
                name="municipio"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75 mt-1"
              >
                <option value={null}>seleccionar</option>
                {this.state.municipios.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 ">
              <span className="content-center text-blue-850">Evento</span>
              <select
                name="evento"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option value={null}>seleccionar</option>
                {this.state.eventos.map((elemento) =>
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
              <span className="content-center text-blue-850">
                Tipo de carcasa
              </span>
              <select
                name="tipo de case"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option value={null}>seleccionar</option>
                {this.state.tipo_case.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="content-center text-blue-850">
                Tipo de micrófono
              </span>
              <select
                name="tipo de micro"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option value={null}>seleccionar</option>
                {this.state.tipo_microfono.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-41.5">
              <span className="content-center text-blue-850">
                Método de etiquetado
              </span>
              <select
                name="metodo etiquetado"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75 mt-1"
              >
                <option value={null}>seleccionar</option>
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
              <span className="content-center text-blue-850">
                Software de etiquetado
              </span>
              <select
                name="software"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option value={null}>seleccionar</option>
                {this.state.software.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
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
              <span className="content-center text-blue-850">
                Tipo de grabadora
              </span>
              <select
                name="tipo de grabadora"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full mt-1 rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75"
              >
                <option value={null}>seleccionar</option>
                {this.state.tipo_grabadora.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
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
              <span className="text-blue-850">Elevación mínima</span>
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
              <span className="text-blue-850">Elevación máxima</span>
              <input
                type="text"
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <br />

              <button
                onClick={this.publicAudio}
                className="block  font-semibold font-poppins text-white bg-green-550 hover:shadow-lg hover:opacity-70 w-54.25 h-7.75 "
              >
                Buscar
              </button>
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center mb-10.75">
          <div className="w-341.5 h-151.25">
            <PublicTable />
          </div>
        </div>

        <div className="flex items-center justify-center">
          <nav
            className="relative z-0 inline-flex -space-x-px rounded-md shadow-sm"
            aria-label="Pagination"
          >
            <a
              href="#"
              className="relative inline-flex items-center px-2 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-l-md hover:bg-gray-50"
            >
              <span className="sr-only">Previous</span>
              {/* Heroicon name: solid/chevron-left */}
              <svg
                className="w-5 h-5"
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
              className="relative z-10 inline-flex items-center px-4 py-2 text-sm font-medium text-white border bg-green-450 border-green-450"
            >
              1
            </a>
            <a
              href="#"
              className="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 hover:bg-gray-50"
            >
              2
            </a>

            <span className="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300">
              ...
            </span>
            <a
              href="#"
              className="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 hover:bg-gray-50"
            >
              10
            </a>
            <a
              href="#"
              className="relative inline-flex items-center px-2 py-2 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-r-md hover:bg-gray-50"
            >
              <span className="sr-only">Next</span>
              {/* Heroicon name: solid/chevron-right */}
              <svg
                className="w-5 h-5"
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
