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


export async function uploadUdasData(excelFile, usbSelected) {
  try {
    const formData = new FormData();
    formData.append("file", excelFile);
    formData.append("usbSelected", usbSelected);

    const { data } = await Http.post("/load_udas/", formData);
    return { status: true, data: data };
  } catch (error) {
    //alert("Algo salio mal");
    return { status: false, data: null };
  }
}

export async function uploadLabelFile(file) {
  try {
    const formData = new FormData();
    formData.append("file", file);

    const { data } = await Http.post("/load_labelfile/", formData);
    return { status: true, data: data };
  } catch (error) {
    //alert("Algo salio mal");
    return { status: false, data: null };
  }
}