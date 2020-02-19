import axios from "axios";

const instance = axios.create({
  baseURL: 'http://1cf015d6.ngrok.io'
})

export default instance;