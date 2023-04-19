import { Http } from "../Http";

export async function getUsersList() {
  try {
    const { data } = await Http.get("/get_users/");
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return { status: false, data: null };
  }
}

export async function createUser(user) {
  try {
    const { data } = await Http.post("/add_user/", user);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return {
      status: false,
      data: null,
      errorMessage: "No se pudo crear el usuario",
    };
  }
}

export async function updateUser(user) {
  try {
    const { id_user, ...userEdit } = user;
    const { data } = await Http.put(`/update_user/${id_user}/`, userEdit);
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
