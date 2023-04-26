import { Http } from "../Http";

export async function getHardwareList() {
  try {
    const { data } = await Http.get("/get_hardwares/");
    console.log("data >>", data)
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return { status: false, data: null };
  }
}

export async function getRecorderList() {
  try {
    const { data } = await Http.get("/get_recorders/");
    console.log("data >>", data)
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return { status: false, data: null };
  }
}

export async function createRecorder(recorder) {
  try {
    const { data } = await Http.post("/add_recorder/", recorder);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return {
      status: false,
      data: null,
      errorMessage: "No se pudo crear la grabadora",
    };
  }
}

export async function updateRecorder(recorder) {
  try {
    const { id_h_serial, ...recorderEdit } = recorder;
    const { data } = await Http.put(`/update_recorder/${id_h_serial}/`, recorderEdit);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return {
      status: false,
      data: null,
      errorMessage: "No se pudo actualizar el usuario",
    };
  }
}

export async function toggleActiveUser(user) {
  try {
    const { id_user } = user;
    const { data } = await Http.delete(`/delete_user/${id_user}/`);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return {
      status: false,
      data: null,
      errorMessage: "No se pudo actualizar el usuario",
    };
  }
}
