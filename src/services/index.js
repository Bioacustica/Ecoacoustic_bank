import axios from 'axios'
const baseUrl = "http://localhost:8000"



export async function sendMenssage(information){

try {
    await axios.post(`${baseUrl}/contactanos`,information).then(res=>{
        console.log(res)
        console.log(res.data)
    })
    console.log('error')
} catch (e) {
    console.log('Fail')
    console.log(e)
}
}