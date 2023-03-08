import { Http } from "../Http";

export async function uploadMasterTableData(excelFile) {
  try {
    const formData = new FormData();
    formData.append("excel_file", excelFile);

    const { data } = await Http.post("/load_master_tables", formData);
    console.log("data :>> ", data);
    return { status: true, data: data };
  } catch (error) {
    alert("Algo salio mal");
    return { status: false, data: null };
  }
}
