import axios from 'axios';
import React, {useState, useEffect}  from "react";
import PublicFilter from './PublicFilter';
function Filter_Public (){

    useEffect(() => {
        const fetchData = async () => {
          const { data } = await axios.get(
            "localhost:3000/lista_filtros/"
          );
      
          //console.log(data);
        };
      
        fetchData();
      }, []); 
}

 

function Table_Public(){
    useEffect(()=>{
     
     const fetchDota = async () => {
        const { dato } = await axios.get(
          "http://localhost:3000/public-records/"
        );
    
        console.log(dato);
      };
  
      
      fetchDota();
    },[]);

}

export default Filter_Public;Table_Public;
