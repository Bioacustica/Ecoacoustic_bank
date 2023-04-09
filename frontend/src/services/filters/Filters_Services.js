import { Http } from "../Http";

export const optionsList=async(url)=>await Http.get(url)

export const get =async(url,data={})=>await Http.get(url,data)

export const post =async(url,data={})=>await Http.post(url,data)