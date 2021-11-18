import axios from "axios";

export const Http= axios.create({
    baseURL:'http://localhost:8000/',
    timeout: 10000,
    headers: {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
      }, 
    

})

Http.interceptors.response.use((resp) => {
    console.log("entro en el interceptor");
    return resp;
  },
  (error) => {
    console.log("error");
    return Promise.reject(error);
  })