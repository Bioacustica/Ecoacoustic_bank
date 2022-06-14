import React, {useState, useEffect}  from "react";
import MoreInformationModal from "./MoreInformationModal";
import axios from 'axios';
import { data } from "autoprefixer";
require("typeface-poppins");
require("typeface-rubik");
function PublicTable() {

  const columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const [showModal, setShowModal] = useState(false)

  const openModal=()=>setShowModal(true)

  const closeModal=()=>setShowModal(false)

 
  
 // const [post,setPost]=useState([]);

 // React.useEffect(async()=>{
 //   await axios.get(URLBase,{
 //     "catalogo":"",
 //     "habitat":"",
 //     "municipio":"",
 //     "evento":"",
 //     "tipo de case":"",
 //     "tipo de micro":"",
 //     "metodo etiquetado":"",
 //     "software":"",
 //     "tipo de grabadora":""
 //     }).then((response)=>{
 //     setPost(response.data)
 //   });
 // },[]);

 // if(!post)return null;

 // console.log(post)
  

  
  const [list, setList] = useState([]);
 
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get({
          url:"http://localhost:3000/public-records/"
          
     
          .then(list => setList(data))
        });
        
        setList(response.data);

        console.log(setList);
      } catch (error) {
        console.log(error);
      }
    };
  
     fetchData();
  }, []);

  if(!list)return null;

  
 // console.log(list.ciudad)
//  useEffect(() => {
//    const fetchData = async () => {
//      const { data } = await axios.get(
//        "http://localhost:8000/public-records/"
//        .then(res => res.json())
//     
//       .then(data => setData(data))
//      );
//  
//      console.log(data);
//    };
//  
//    fetchData();
 // }, []);





  return (
    <div className="flex">
      <div className="  border overflow-x-auto">
        <table className=" border border-collapse">
          <thead>
            <tr className="">
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Id
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Nombre
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Fecha
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Hábitat
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Departamento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Municipio
              </td>
              <td className="border-2 font-rubik border-blue-850 text-base h-12.75 px-4 text-center">
                Ciudad
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Elevación
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Evento
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Formato
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Tipo de micrófono
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Método de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Tipo de grabadora
              </td>
              <td className="border-2 font-rubik border-blue-850  text-base h-12.75 px-4 text-center">
                Software de etiquetado
              </td>
              <td className="border-2 font-rubik border-blue-850 text-base h-12.75 px-4 text-center">
                Tipo de carcasa
              </td>
            </tr>
          </thead>

          <tbody>
            {list.map((list) => (
              <tr className="">
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list.ciudad}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
                <td className="border-2 font-rubik border-blue-850 font-light text-base h-12.75 px-4 text-center">
                  {list}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="ml-8">
        <table>
          <thead>
            <tr className="">
              <td className=" font-rubik font-semibold text-base h-14 px-4 text-center"></td>
            </tr>
          </thead>
          <tbody>
            {columns.map((rowscounter) => (
              <tr>
                <td className="font-rubik font-light text-base h-12.75 ml-4">
                  <button 
                  onClick={openModal}
                  className=" bg-yellow-400 font-semibold text-xl text-white  w-31.25">
                    Más
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {showModal && <MoreInformationModal className="z-50" close={closeModal}/>}
      </div>
    </div>
  );
}

export default PublicTable;
