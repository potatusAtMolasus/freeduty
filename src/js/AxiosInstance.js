import axios from "axios";

const instance = axios.create({
  baseURL: 'http://b36b8f8b.ngrok.io'
})

export default instance;