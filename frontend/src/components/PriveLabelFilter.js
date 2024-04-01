import React, { useState } from "react";
import { Component } from "react";
import { formList, fetch_audios, downloadAudiosZip } from "../services";
import PrivateLabelTable from "./PrivateLabelTable";
import { saveAs } from 'file-saver';

require("typeface-poppins");
require("typeface-rubik");
class PrivateLabel extends Component {
  /*const [stado, setCredentials] = useState({
    email: "",
    password: "",
  });*/

  state = {
    metodo_etiquetado: [],
    tipo_grabadora: [],
    ciudades: [], //Deshabilitada
    eventos: [],
    habitats: [], //Deshabilitada
    municipios: [],
    software: [],
    tipo_case: [],
    tipo_microfono: [],
    downloadCSV: false,
    downloadAudios: false,
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
      "min_date": null,
      "max_date": null,
      "min_elevation": null,
      "max_elevation": null,
    },
    List_Audio: {},
  };

  componentDidMount = async () => {
    const response = await formList();

    this.setState({
      eventos: response.data.evento,
      habitats: response.data.habitat,
      ciudades: response.data.ciudad,
      tipo_grabadora: response.data.Tipo_de_grabadora,
      tipo_case: response.data.tipo_de_case,
      tipo_microfono: response.data.tipo_de_micro,
      metodo_etiquetado: response.data.Metodo_etiquetado,
      software: response.data.software_etiquetado,
      municipio: response.data.municipio,
    });
  };
  
  valueToState = ({ name, value }) => {
    this.setState((state) => {
      return { ...state, filters: { ...state.filters, [name]: value ?? "" } };
    });
  };



  publicAudio = async () => {
    const List_Audio = await fetch_audios(this.state.filters);

    this.setState((state) => {
      return { ...state, List_Audio };
    });
  };

  downloadCSV = async () => {
    new Promise((resolve, reject) => {
      if (this.state.downloadCSV) {
        let data = "Id,Nombre,Fecha,Hábitat,Departamento,Municipio,Ciudad,Elevación,Formato,Tipo de micrófono,Método de etiquetado,Tipo de grabadora,Software de etiquetado,Tipo de carcasa\n"
        this.state.List_Audio.results.forEach(audio => {
          data += `${audio.id_record},${audio.fingerprint_},${audio.date_record_},${audio.habitat_},${audio.departamento_},${audio.ciudad_},${audio.ciudad_},${audio.elevation},${audio.formato_},${audio.microphone},${audio.metodo_etiquetado_},${audio.tipo_grabadora_},${audio.software_etiquetado_},${audio.case_}\n`
        });
        const enlaceDescarga = document.createElement('a');
        enlaceDescarga.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(data);
        enlaceDescarga.target = '_blank';
        enlaceDescarga.download = 'archivo.csv';
        document.body.appendChild(enlaceDescarga);
        enlaceDescarga.click();
        document.body.removeChild(enlaceDescarga);
      }
      resolve()
    }).then(async () => {
      if(this.state.downloadAudios) {
        const { data } = await downloadAudiosZip()
        const blob = new Blob([data], { type: 'application/zip' });
        saveAs(blob, 'audios.zip');
      }
    })


  }

  render() {
    return (
      <div>
        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">Country</span>
              <select
                disabled
                name="ciudad"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full border border-blue-850 rounded-md bg-white  shadow-lg focus:border-indigo-200 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75"
              >
                <option value="">choose</option>
                {this.state.ciudades.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">Habitat</span>
              <select
                name="habitat"
                onChange={(event) => this.valueToState(event.target)}
                className="block  border border-blue-850 w-full mt-1 rounded-md bg-white  shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50mt-1 h-7.75">
                <option value="">choose</option>
                {this.state.habitats.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">Municipality</span>
              <select
                disabled
                name="municipio"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75 mt-1"
              >
                <option value="">choose</option>
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
              <span className="content-center text-blue-850">Event</span>
              <select 
                name="evento"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option value="">choose</option>
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
            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">
                Case
              </span>
              <select 
                name="tipo de case"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option value="">choose</option>
                {this.state.tipo_case.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">
                Microphone
              </span>
              <select 
                name="tipo de micro"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option value="">choose</option>
                {this.state.tipo_microfono.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">
                Evidence
              </span>
              <select 
                name="metodo etiquetado"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75 mt-1">
                <option value="">choose</option>
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
                Software
              </span>
              <select 
                name="software"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 h-7.75">
                <option value="">choose</option>
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
            <label className="block text-center w-54.25 mr-15.666">
              <span className="content-center text-blue-850">
                Hardware
              </span>
              <select 
                name="tipo de grabadora"
                onChange={(event) => this.valueToState(event.target)}
                className="block w-full mt-1 rounded-md bg-white border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 h-7.75">
                <option value="">choose</option>
                {this.state.tipo_grabadora.map((elemento) =>
                  elemento.map((event) => (
                    <option key={event} value={event}>
                      {event}
                    </option>
                  ))
                )}
              </select>
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850">Start date</span>
              <input
                name="min_date"
                type="date"
                onChange={(event) => this.valueToState(event.target)}
                className="mt-1 block w-full h-7.75 rounded-md border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850">End date</span>
              <input
                name="max_date"
                type="date"
                onChange={(event) => this.valueToState(event.target)}
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <span className="text-blue-850">Minimum elevation</span>
              <input
                name="min_elevation"
                type="text"
                onChange={(event) => this.valueToState(event.target)}
                className="mt-1 block w-full h-7.75 rounded-md border border-blue-850 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850">Maximum elevation</span>
              <input
                name="max_elevation"
                type="text"
                onChange={(event) => this.valueToState(event.target)}
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <br />
              <button
                onClick={this.publicAudio}
                className="block font-semibold font-poppins text-white bg-gray-250 hover:shadow-lg hover:opacity-70 w-54.25 h-7.75 ">
                Search
              </button>
            </label>
          </div>
        </div>
        
        {(this.state.List_Audio.results || []).length > 0 && (
          <div className="flex justify-center items-center content-center mb-8.5">
            <div className="flex w-341.5 justify-center items-center">
              <button
              disabled={!this.state.downloadAudios && !this.state.downloadAudios}
                onClick={this.downloadCSV}
                className="block font-semibold font-poppins text-white bg-gray-250 hover:shadow-lg hover:opacity-70 w-54.25 h-7.75 ">
                Download
              </button>

              <label className="block  text-center w-54.25 ">
                <br />
                <div className="flex">
                  <input
                    className="w-7.75 h-7.75 ml-2 text-white mr-2"
                    type="checkbox"
                    checked={this.state.downloadAudios}
                    onChange={(e) => this.setState((state) => ({...state, downloadAudios: e.target.checked }))}
                  />
                  <label className="block  mb-2 font-semibold text-2xl font-poppins text-white bg-blue-250 w-45.5 h-7.75 ">
                    Audios
                  </label>
                </div>
                <div className="flex">
                  <input
                    className="w-7.75 h-7.75 ml-2 text-white mr-2"
                    type="checkbox"
                    checked={this.state.downloadCSV}
                    onChange={(e) => this.setState((state) => ({...state, downloadCSV: e.target.checked }))}
                  />
                  <label className="block  font-semibold font-poppins text-2xl text-white bg-blue-250 w-45.5 h-7.75 ">
                    CSV
                  </label>
                </div>
              </label>
            </div>
          </div>
        )}

        <div className="flex items-center justify-center mb-32">
          <div className="w-341.5">
            <PrivateLabelTable List_Audio={this.state.List_Audio} />
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
export default PrivateLabel;
