import axios from 'axios'
import { ContactService } from "../services/contacto/Contacto";
const baseUrl = "http://localhost:8000"



export async function sendMenssage({subject,from_email,message}){

    try {
        const formData = new FormData();
    formData.append('subject', subject);
    formData.append('from_email', from_email);
    formData.append('message', message);
    const {data}=await ContactService("contactanos/",formData)
    console.log(data)
    return true
        
    } catch (error) {
    alert("Algo salio mal")
    return false 
    }
    
}