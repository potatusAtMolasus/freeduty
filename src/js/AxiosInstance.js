import axios from "axios";

const instance = axios.create({
  baseURL: 'http://63f0c113.ngrok.io'
})

export default instance;