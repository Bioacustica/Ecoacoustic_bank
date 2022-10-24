
import { ContactService } from "./contact/Contacto_Service";
import { optionsList,get} from "./filters/Filters_Services";
import { LoginService } from './login/Login_Service';


const FormData = require('form-data');
const fs = require('fs');


export async function sendMenssage({subject,from_email,message}){

    try {
    const formData = new FormData();
    formData.append('subject', subject);
    formData.append('from_email', from_email);
    formData.append('message', message);
    const {data}=await ContactService("contactanos/",formData)
    return true
        
    } catch (error) {
    alert("Algo salio mal")
    return false 
    }
    
}

export async function sendCredentialsData({email,password}){
    
    try {
    const formData = new FormData();
    formData.append('email', email);
    formData.append('password', password);
    const {data}=await LoginService("login/",formData)
    window.localStorage.setItem("token", data.access);
     window.localStorage.setItem("refresh_token", data.refresh);
     window.localStorage.setItem("username", data.username);
     window.localStorage.setItem("rol", data.roles);
    return {status:true,data:data.status}
        
    } catch (error) {
    alert("Algo salio mal")
    return {status:false,data:null}
    }
    
}

export async function formList(){

    try {
    const {data}=await optionsList("lista_filtros/")

    return {status:true,data:data}
        
    } catch (error) {
    alert("Algo salio mal")
    return {status:false,data:null}
    }
    
}

export async function fetch_audios(){
    
    try{
        const {data}= await get ("public-records/",{data:{
        
        "catalogo":"AFGANISTAN",
        "habitat":"",
        "municipio":"",
        "evento":"",
        "tipo de case":"",
        "tipo de micro":"",
        "metodo etiquetado":"",
        "software":"",
        "tipo de grabadora":""
        }})

        return{status:true,data}
    } catch (error){
        alert("Algo salio mal")
        return {status:false,data:null}
         }

}
