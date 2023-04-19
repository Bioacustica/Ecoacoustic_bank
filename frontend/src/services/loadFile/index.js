import { Http } from "../Http";

export async function uploadMasterTableData(excelFile) {
  try {
    const formData = new FormData();
    formData.append("file", excelFile);

    const { data } = await Http.post("/load_master_tables/", formData);
    return { status: true, data: data };
  } catch (error) {
    //alert("Algo salio mal");
    return { status: false, data: null };
  }
}
