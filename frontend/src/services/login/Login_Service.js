import { Http } from "../Http";

export const LoginService=async(url,data)=>await Http.post(url,data)