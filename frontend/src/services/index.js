import { ContactService } from "./contact/Contacto_Service";
import { optionsList, get, post } from "./filters/Filters_Services";
import { LoginService } from "./login/Login_Service";

import axios from "axios";
const FormData = require("form-data");
const fs = require("fs");

export async function sendMenssage({ subject, from_email, message }) {
  try {
    const formData = new FormData();
    formData.append("subject", subject);
    formData.append("from_email", from_email);
    formData.append("message", message);
    const { data } = await ContactService("contactanos/", formData);
    return true;
  } catch (error) {
    //alert("Algo salio mal")
    return false;
  }
}

export async function sendCredentialsData({ email, password }) {
  try {
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);
    const { data } = await LoginService("login/", formData);
    window.localStorage.setItem("token", data.access);
    window.localStorage.setItem("refresh_token", data.refresh);
    window.localStorage.setItem("username", data.username);
    window.localStorage.setItem("rol", data.roles);
    return { status: true, data: data.status };
  } catch (error) {
    //alert("Algo salio mal")
    return { status: false, data: null };
  }
}

export async function formList() {
  try {
    const { data } = await optionsList("lista_filtros/");

    return { status: true, data: data };
  } catch (error) {
    //alert("Algo salio mal")
    return { status: false, data: null };
  }
}

export async function fetch_audios(Items) {
  try {
    const options = {
      method: "POST",
      url: "http://localhost:8000/public-records/",
      headers: { "Content-Type": "application/json" },
      data: {
        ...Items,
      },
    };

    const { data } = await axios.request(options);

    return data;
  } catch (error) {
    //alert("Algo salio mal")
    return { status: false, data: null };
  }
}
