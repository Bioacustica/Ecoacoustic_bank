// CustomDocumentationComponent.js|jsx

import React from 'react';

export function CustomDocumentationComponent() {
 


  return (
    
    <div >
      <div className='flex items-center font-extrabold text-3xl  justify-center text-blue-500'>
      <h1 >Filtro de etiquetado</h1>
      </div>
      <br/>
      <code>
        Autor: Alejandro Piedrahita Carvajal
      </code>
      <br/>
      <hr/>
      <br/>
      <h3 className='font-bold'>Descripcion</h3>
      <div className='flex items-center justify-start'>
      <p>
        Este componente hace referencia al filtro de etiquetado para usuarios logeados con sus credenciales.
      </p>
      </div>
      
      <br/>
      <h3 className='font-bold'>Funciones</h3>
      <p>
       No cuenta con ninguna funcion
      </p>
      <br/>
      <h3 className='font-bold'>Variables</h3>
      <p>
       No cuenta con ninguna variable de entrada o salida
      </p>
      <br/>
      <h3 className='font-bold'>Codigo</h3>
      <br/>

      
      <pre  className='border-2'>{
        <code className='w-139 h- justify-center'>{
        `
        <div>
        
        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850 content-center">Ciudades</span>
              <select
              name="ciudad"
              onChange={event=>this.valueToState(event.target)}
                disabled
                className="block w-full border border-blue-850 rounded-md bg-white  shadow-lg 
                focus:border-indigo-200 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 
                mt-1 h-7.75"
              >
                <option value={null}>seleccionar</option>
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
              <span className="text-blue-850 content-center">Hábitat</span>
              <select className="block  border border-blue-850 w-full mt-1 rounded-md bg-white
                shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 
                focus:ring-opacity-50mt-1 h-7.75">
                <option value={null}>seleccionar</option>
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
              <span className="text-blue-850 content-center">Municipio</span>
              <select
                disabled
                className="block w-full rounded-md bg-white border border-blue-850 shadow-lg 
                focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                 h-7.75 mt-1"
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
              <span className="text-blue-850 content-center">Evento</span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg
               focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 
               mt-1 h-7.75">
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
            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850 content-center">Tipo de carcasa</span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg 
              focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 
              mt-1 h-7.75">
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

            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850 content-center">
                Tipo de micrófono
              </span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg 
              focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 mt-1 
              h-7.75">
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

            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850 content-center">
                Método de etiquetado
              </span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg 
              focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 
              h-7.75 mt-1">
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
              <span className="text-blue-850 content-center">
                Software de etiquetado
              </span>
              <select className="block w-full rounded-md bg-white border border-blue-850 shadow-lg 
              focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 
              mt-1 h-7.75">
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
            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850 content-center">
                Tipo de grabadora
              </span>
              <select className="block w-full mt-1 rounded-md bg-white border border-blue-850 
              shadow-lg focus:border-indigo-300 focus:ring focus:ring-indigo-200 
              focus:ring-opacity-50 h-7.75">
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
            

            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850">Fecha de inicio</span>
              <input
                type="date"
                className="mt-1 block w-full h-7.75 rounded-md border border-blue-850 shadow-lg 
                focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850">Fecha final</span>
              <input
                type="date"
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg 
                focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <span className="text-blue-850">Elevación mínima</span>
              <input
                type="text"
                className="mt-1 block w-full h-7.75 rounded-md border border-blue-850 shadow-lg 
                focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />

            </label>
          </div>
        </div>

        <div className="flex justify-center items-center content-center mb-8.5">
          <div className="flex w-341.5 justify-center items-center">
            <label className="block text-center w-54.25 mr-15.666">
              <span className="text-blue-850">Elevación máxima</span>
              <input
                type="text"
                className="mt-1 block w-full rounded-md border border-blue-850 h-7.75 shadow-lg 
                focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </label>

            <label className="block text-center w-54.25">
              <br />
              <button className="block font-semibold font-poppins text-white bg-gray-250 
              hover:shadow-lg hover:opacity-70 w-54.25 h-7.75 ">
                Buscar
              </button>
            </label>
          </div>
        </div>

        <div className="flex justify-center items-center mb-32">
          <div className="w-341.5 h-132.25">
            <PrivateLabelTable />
          </div>
        </div>

        <div className="flex items-center justify-center">
          <nav
            className="relative z-0 inline-flex rounded-md shadow-sm -space-x-px"
            aria-label="Pagination"
          >
            <a
              href="#"
              className="relative inline-flex items-center px-2 py-2 rounded-l-md border 
              border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
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
                  d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 
                  1 0 010-1.414l4-4a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            </a>
            {/* Current: "z-10 bg-indigo-50 border-indigo-500 text-indigo-600", Default: 
          "bg-white border-gray-300 text-gray-500 hover:bg-gray-50" */}
            <a
              href="#"
              aria-current="page"
              className="z-10 bg-green-450 border-green-450 text-white relative 
              inline-flex items-center px-4 py-2 border text-sm font-medium"
            >
              1
            </a>
            <a
              href="#"
              className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 
              relative inline-flex items-center px-4 py-2 border text-sm font-medium"
            >
              2
            </a>

            <span className="relative inline-flex items-center px-4 py-2 border 
            border-gray-300 bg-white text-sm font-medium text-gray-700">
              ...
            </span>
            <a
              href="#"
              className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 
              relative inline-flex items-center px-4 py-2 border text-sm font-medium"
            >
              10
            </a>
            <a
              href="#"
              className="relative inline-flex items-center px-2 py-2 rounded-r-md border 
              border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
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
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4
                   4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            </a>
          </nav>
        </div>
      </div>
    `}
</code>

}</pre>
    </div>
  );
  
}

