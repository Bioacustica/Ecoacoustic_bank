import { Http } from "../Http";

export const ContactService=async(url,data)=>await Http.post(url,data)