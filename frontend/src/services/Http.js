import axios from "axios";

export const Http = axios.create({
  baseURL: "http://192.168.0.2:8000/",
  timeout: 10000,
  headers: {},
});

Http.interceptors.response.use(
  (resp) => {
    return resp;
  },
  (error) => {
    return Promise.reject(error);
  }
);
