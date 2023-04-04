import { Http } from "../Http";

export async function getUsersList() {
  try {
    const { data } = await Http.get("/get_users/");
    console.log("data :>> ", data);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return { status: false, data: null };
  }
}

export async function createUser(user) {
  try {
    const { data } = await Http.post("/add_user/", user);
    console.log("data create:>> ", data);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return { status: false, data: null };
  }
}

export async function updateUser(user) {
  try {
    const { id_user, ...userEdit } = user;
    const { data } = await Http.put(`/update_user/${id_user}/`, userEdit);
    console.log("data update:>> ", data);
    return { status: true, data: data };
  } catch (error) {
    // alert("Algo salio mal");
    return { status: false, data: null };
  }
}
