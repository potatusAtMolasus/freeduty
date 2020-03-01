import axios from "axios";

const instance = axios.create({
  baseURL: 'http://17b8f12e.ngrok.io'
})

export default instance;